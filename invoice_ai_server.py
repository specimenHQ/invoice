#!/usr/bin/env python3
from __future__ import annotations
import json, os, sys, urllib.error, urllib.request, webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parent
HTML_FILE=ROOT/"invoice-ai-prompt-generator.html"; ENV_FILE=ROOT/".env"; MAX_BODY_BYTES=2_000_000

def load_dotenv(path:Path)->None:
    if not path.exists(): return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line=raw.strip()
        if not line or line.startswith("#") or "=" not in line: continue
        k,v=line.split("=",1); k=k.strip(); v=v.strip().strip('"').strip("'")
        if k and k not in os.environ: os.environ[k]=v
load_dotenv(ENV_FILE)
HOST="127.0.0.1"; PORT=int(os.getenv("INVOICE_AI_PORT","8777"))
OLLAMA_URL=os.getenv("OLLAMA_URL","http://127.0.0.1:11434").strip().rstrip("/")
OLLAMA_MODEL=os.getenv("OLLAMA_MODEL","qwen3:8b").strip() or "qwen3:8b"
SYSTEM_INSTRUCTIONS="""You are the prompt-writing engine inside a graphic-novel panel generator. Return only one finished image-generation prompt. No commentary, Markdown fences, alternatives, analysis, or explanations. Preserve binding metadata, exact gradient code, RGB target, gradient position, and delta. Keep one visual job per panel. Do not introduce future-stage imagery. Maintain black-on-black distinctions through ink density, matte/gloss contrast, pressure, texture, and restrained tonal separation rather than bright highlights. When requested, end with a line beginning exactly 'Negative prompt:'. Use concrete image-model language and avoid hype."""

def reply(h,status,payload):
    data=json.dumps(payload,ensure_ascii=False).encode(); h.send_response(status); h.send_header("Content-Type","application/json; charset=utf-8"); h.send_header("Content-Length",str(len(data))); h.send_header("Cache-Control","no-store"); h.end_headers(); h.wfile.write(data)

def build_input(p):
    amap={"generate":"Write the strongest finished image prompt.","darker":"Rewrite it substantially darker and more black-on-black.","simpler":"Reduce clutter and keep one visual job.","more_printed":"Make it physically printed, inked, etched, matte, and tactile rather than digital.","continuity":"Strengthen continuity with the panel stage and narrative progression.","precision":"Increase concrete visual precision while remaining restrained."}
    parts=[f"Mode: {p.get('mode','book')}",f"Operation: {amap.get(p.get('action'),amap['generate'])}",f"Preserve final negative prompt: {'yes' if p.get('preserve_negative',True) else 'no'}",f"Strict continuity: {'yes' if p.get('strict_continuity',True) else 'no'}"]
    if str(p.get('brief') or '').strip(): parts.append("User brief:\n"+str(p['brief']).strip())
    if p.get('metadata'): parts.append("Binding panel metadata:\n"+json.dumps(p['metadata'],ensure_ascii=False,indent=2))
    if str(p.get('current_prompt') or '').strip(): parts.append("Current prompt:\n"+str(p['current_prompt']).strip())
    return "\n\n".join(parts)

def call_ollama(p):
    model=str(p.get('model') or '').strip() or OLLAMA_MODEL
    prompt=f"{SYSTEM_INSTRUCTIONS}\n\n{build_input(p)}"
    body=json.dumps({"model":model,"prompt":prompt,"stream":False}).encode()
    req=urllib.request.Request(f"{OLLAMA_URL}/api/generate",data=body,headers={"Content-Type":"application/json"},method="POST")
    try:
        with urllib.request.urlopen(req,timeout=180) as r: parsed=json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        detail=e.read().decode(errors="replace")
        raise RuntimeError(f"Ollama API error {e.code}: {detail}")
    except urllib.error.URLError as e:
        raise RuntimeError(f"Could not reach Ollama at {OLLAMA_URL}. Start Ollama and install the model, for example: ollama pull {model}")
    text=str(parsed.get("response") or "").strip()
    if not text: raise RuntimeError("Ollama returned no prompt text.")
    return text,model

class Handler(BaseHTTPRequestHandler):
    def log_message(self,fmt,*args): print("[INVOICE AI] "+fmt%args)
    def do_GET(self):
        path=self.path.split('?',1)[0]
        if path=="/api/status":
            return reply(self,200,{"ok":True,"provider":"ollama","model":OLLAMA_MODEL,"ollama_url":OLLAMA_URL})
        if path in {"/","/index.html","/invoice-ai-prompt-generator.html"}:
            if not HTML_FILE.exists(): return self.send_error(404,"HTML file missing")
            data=HTML_FILE.read_bytes(); self.send_response(200); self.send_header("Content-Type","text/html; charset=utf-8"); self.send_header("Content-Length",str(len(data))); self.send_header("Cache-Control","no-store"); self.end_headers(); self.wfile.write(data); return
        self.send_error(404,"Not found")
    def do_POST(self):
        if self.path.split('?',1)[0]!="/api/generate": return self.send_error(404,"Not found")
        try: length=int(self.headers.get("Content-Length","0"))
        except: return reply(self,400,{"error":"Invalid content length."})
        if length<=0 or length>MAX_BODY_BYTES: return reply(self,413,{"error":"Request is empty or too large."})
        try:
            p=json.loads(self.rfile.read(length).decode())
            prompt,model=call_ollama(p)
            reply(self,200,{"prompt":prompt,"model":model,"provider":"ollama"})
        except (json.JSONDecodeError,UnicodeDecodeError,ValueError) as e: reply(self,400,{"error":str(e)})
        except RuntimeError as e: reply(self,502,{"error":str(e)})
        except Exception as e: reply(self,500,{"error":f"Unexpected server error: {e}"})

def main():
    if not HTML_FILE.exists(): print(f"Missing {HTML_FILE}"); sys.exit(1)
    url=f"http://{HOST}:{PORT}"; srv=ThreadingHTTPServer((HOST,PORT),Handler)
    print("="*64); print("INVOICE AI Prompt Generator"); print("Open:",url); print("Provider: ollama"); print("Model:",OLLAMA_MODEL); print("Ollama URL:",OLLAMA_URL); print("Keep this window open. Ctrl+C stops the server."); print("="*64)
    try: webbrowser.open(url)
    except: pass
    try: srv.serve_forever()
    except KeyboardInterrupt: print("\nStopping server.")
    finally: srv.server_close()
if __name__=="__main__": main()
