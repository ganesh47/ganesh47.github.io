const form = document.querySelector('#search-form');
const query = document.querySelector('#search-query');
const topic = document.querySelector('#search-topic');
const status = document.querySelector('#search-status');
const results = document.querySelector('#search-results');
let engine, pending;
let requestId = 0;
function restore() {
  const params = new URLSearchParams(location.search);
  query.value = params.get('q') || ''; topic.value = params.get('topic') || '';
}
function updateURL() {
  const params = new URLSearchParams();
  if (query.value.trim()) params.set('q', query.value.trim());
  if (topic.value) params.set('topic', topic.value);
  const url = location.pathname + (params.size ? '?' + params : '');
  if (url !== location.pathname + location.search) history.pushState({}, '', url);
}
function excerptNode(excerpt) {
  const fragment = new DOMParser().parseFromString(excerpt, 'text/html');
  const output = document.createDocumentFragment();
  function append(node, target) {
    if (node.nodeType === Node.TEXT_NODE) target.append(document.createTextNode(node.textContent));
    else if (node.nodeType === Node.ELEMENT_NODE) {
      const next = node.tagName === 'MARK' ? document.createElement('mark') : target;
      if (next !== target) target.append(next);
      node.childNodes.forEach(child => append(child, next));
    }
  }
  fragment.body.childNodes.forEach(node => append(node, output)); return output;
}
async function search() {
  const id = ++requestId, term = query.value.trim(); results.replaceChildren(); delete status.dataset.query;
  if (!term && !topic.value) { status.textContent = 'Enter a word or phrase, or select a topic.'; return; }
  status.textContent = 'Searching…';
  try {
    engine ||= import('../../pagefind/pagefind.js');
    const pagefind = await engine;
    const response = await pagefind.search(term || null, { filters: topic.value ? { Topic: topic.value } : {} });
    const data = await Promise.all(response.results.slice(0, 30).map(result => result.data()));
    if (id !== requestId) return;
    status.dataset.query = term;
    status.textContent = response.results.length ? `${response.results.length} article${response.results.length === 1 ? '' : 's'} found${response.results.length > 30 ? '; showing the first 30. Refine your search for more specific results.' : '.'}` : 'No articles found. Try fewer words, a different phrase or all topics.';
    for (const item of data) {
      const article = document.createElement('article'); article.className = 'search-result';
      const heading = document.createElement('h2'), link = document.createElement('a');
      link.href = item.url; link.textContent = item.meta.title; heading.append(link); article.append(heading);
      const date = document.createElement('p'); date.className = 'row-date';
      const parsed = new Date(item.meta.date);
      date.textContent = !Number.isNaN(parsed.valueOf()) ? parsed.toLocaleDateString('en-GB', { day:'numeric',month:'short',year:'numeric',timeZone:'Asia/Kolkata' }) : '';
      article.append(date);
      const excerpt = document.createElement('p'); excerpt.append(excerptNode(item.excerpt)); article.append(excerpt); results.append(article);
    }
  } catch (error) {
    if (id !== requestId) return;
    status.textContent = 'Search could not load. Please reload, or browse the topics and writing pages.';
    console.error('Notebook search unavailable', error); engine = undefined;
  }
}
form.addEventListener('submit', event => { event.preventDefault(); clearTimeout(pending); updateURL(); search(); });
query.addEventListener('input', () => { clearTimeout(pending); pending = setTimeout(() => { updateURL(); search(); }, 220); });
topic.addEventListener('change', () => { clearTimeout(pending); updateURL(); search(); });
form.addEventListener('reset', event => { event.preventDefault(); clearTimeout(pending); query.value = ''; topic.value = ''; updateURL(); search(); query.focus(); });
window.addEventListener('popstate', () => { clearTimeout(pending); restore(); search(); });
restore(); search();
