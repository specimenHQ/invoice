import fs from 'node:fs';
import crypto from 'node:crypto';
import { execFileSync } from 'node:child_process';
import os from 'node:os';
import path from 'node:path';

const want = {
  archive: '5d8cb5b023b6d90de22e144b7a68e5750664be58cfa5095c22db6f9d42e5dad5',
  index: 'c6aff53f498c7a1bca6f6b158ee39c585009dafee4fee30f2ab22c07a3906d3d',
};
const sha = p => crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const must = (cond, msg) => { if (!cond) throw new Error(msg); };
const text = p => fs.readFileSync(p, 'utf8');

for (const p of [
  'CURRENT-STATE.md', 'LOCAL-ASSETS.md',
  'mobile-source/capacitor.config.json',
  'mobile-source/android/app/build.gradle',
  'mobile-source/android/app/src/main/java/com/bill/invoice/MainActivity.java'
]) must(fs.existsSync(p), `missing ${p}`);

const cap = JSON.parse(text('mobile-source/capacitor.config.json'));
must(cap.appId === 'com.bill.invoice', 'wrong appId');
must(cap.appName === 'INVOICE', 'wrong appName');
const gradle = text('mobile-source/android/app/build.gradle');
must(/versionCode\s+1728\b/.test(gradle), 'wrong versionCode');
must(/versionName\s+"b17\.28"/.test(gradle), 'wrong versionName');
const state = text('CURRENT-STATE.md');
must(state.includes(want.archive), 'archive hash missing from CURRENT-STATE');
must(state.includes(want.index), 'index hash missing from CURRENT-STATE');

const archive = process.env.INVOICE_B1728_ARCHIVE || 'invoice-apk-project_b17.28.zip';
if (fs.existsSync(archive)) {
  must(sha(archive) === want.archive, 'local archive hash mismatch');
  console.log('OK local archive:', archive);
} else console.log('LOCAL archive not present; manifest recorded.');

const index = process.env.INVOICE_B1728_INDEX;
if (index && fs.existsSync(index)) {
  must(sha(index) === want.index, 'local b17.28 index hash mismatch');
  const html = text(index);
  const scripts = [...html.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/gi)].map(m => m[1]);
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'invoice-b1728-'));
  try {
    scripts.forEach((body, i) => {
      const f = path.join(dir, `inline-${i + 1}.js`);
      fs.writeFileSync(f, body);
      execFileSync(process.execPath, ['--check', f], { stdio: 'pipe' });
    });
    console.log(`OK current index + ${scripts.length} inline scripts`);
  } finally { fs.rmSync(dir, { recursive: true, force: true }); }
} else console.log('LOCAL current index not supplied; set INVOICE_B1728_INDEX to verify it.');

console.log('INVOICE b17.28 checkpoint metadata verified.');
