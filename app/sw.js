/* CACHE must be bumped on every publish, or installed phones keep serving
   the previous build from cache and you debug a version that isn't live. */
const CACHE = 'invoice-b8';
const ASSETS = ['./','./index.html','./manifest.webmanifest',
  './icon-192.png','./icon-512.png','./icon-1024.png'];
self.addEventListener('install', e => { self.skipWaiting();
  e.waitUntil(caches.open(CACHE).then(c=>c.addAll(ASSETS)).catch(()=>{})); });
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks=>Promise.all(
    ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim())); });
self.addEventListener('fetch', e => {
  if (e.request.method!=='GET') return;
  e.respondWith(fetch(e.request).then(r=>{ const c=r.clone();
      caches.open(CACHE).then(k=>k.put(e.request,c)).catch(()=>{}); return r; })
    .catch(()=>caches.match(e.request).then(r=>r||caches.match('./index.html')))); });
