/* Service worker — cache-first PWA (édition Memphis).
   ⚠️ RÈGLE : à CHAQUE mise à jour de l'app, AUGMENTEZ le numéro de CACHE.
   Le bump IS le mécanisme de mise à jour pour les utilisateurs. */
const CACHE = 'cqm-v10';
const FICHIERS = [
  './',
  './index.html',
  './manifest.json',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/icon-maskable-512.png',
  './img/especes/chanterelle.jpg',
  './img/especes/chanterelle-tube.jpg',
  './img/especes/cepe.jpg',
  './img/especes/bolet-bai.jpg',
  './img/especes/pied-mouton.jpg',
  './img/especes/morille.jpg',
  './img/especes/pleurote.jpg',
  './img/especes/coprin.jpg',
  './img/especes/lepiote.jpg',
  './img/especes/amanite-rougissante.jpg',
  './img/especes/bolet-amer.jpg',
  './img/especes/tue-mouches.jpg',
  './img/especes/panthere.jpg',
  './img/especes/entolome.jpg',
  './img/especes/paxille.jpg',
  './img/especes/fausse-chanterelle.jpg',
  './img/especes/phalloide.jpg',
  './img/especes/vireuse.jpg',
  './img/especes/galerine.jpg',
  './img/especes/gyromitre.jpg',
  './img/especes/lepiote-brunatre.jpg'
];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(FICHIERS)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(cles => Promise.all(cles.filter(c => c !== CACHE).map(c => caches.delete(c))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  const url = new URL(e.request.url);
  // API et requêtes avec clé : jamais de cache (résultats frais, clé jamais stockée)
  if (url.hostname.endsWith('wikimedia.org') || url.hostname.endsWith('googleapis.com') || url.search.includes('key=')) return;
  e.respondWith(
    caches.match(e.request).then(reponse => reponse || fetch(e.request).then(r => {
      const copie = r.clone();
      caches.open(CACHE).then(c => c.put(e.request, copie)).catch(() => {});
      return r;
    }).catch(() => caches.match('./index.html')))
  );
});
