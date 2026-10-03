"""Route, metadata, prose and internal-link gates against the deployed baseline."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote, urljoin
import hashlib, json, re, sys
import xml.etree.ElementTree as ET

ROOT = Path('_site')
FIXTURE = Path('tests/fixtures/baseline.json')
baseline = json.loads(FIXTURE.read_text())
ORIGIN = 'https://ganesh47.github.io'

class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(); self.ids=[]; self.links=[]; self.canonical=None; self.h1=0; self.giscus=[]
        self.feed(source)
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag=='h1': self.h1+=1
        if tag=='a' and a.get('href'): self.links.append(a['href'])
        if tag=='link' and a.get('rel')=='canonical': self.canonical=a.get('href')
        if tag=='script' and a.get('src')=='https://giscus.app/client.js': self.giscus.append(a)

def pages(root):
    return {'/'+str(p.relative_to(root)).replace('index.html',''):Page(p.read_text()) for p in root.rglob('*.html') if 'pagefind/' not in str(p)}

def broken(root, documents):
    errors=set()
    for route, page in documents.items():
        for href in page.links:
            u=urlsplit(urljoin(ORIGIN+route,href))
            if u.scheme not in ('http','https') or u.netloc!='ganesh47.github.io': continue
            target=unquote(u.path)
            if any(target.startswith(p) for p in baseline['known_project_routes']): continue
            if target in documents:
                if u.fragment and unquote(u.fragment) not in documents[target].ids: errors.add(route+'|'+href)
            elif not (root/target.lstrip('/')).is_file(): errors.add(route+'|'+href)
    return errors

if len(sys.argv)>1 and sys.argv[1]=='--record-baseline':
    root=Path(sys.argv[2]); baseline['known_broken_links']=sorted(broken(root,pages(root)))
    FIXTURE.write_text(json.dumps(baseline,indent=2)+'\n')
    print('Recorded',len(baseline['known_broken_links']),'pre-existing broken internal links.');sys.exit()

docs=pages(ROOT); failures=[]
for route, canonical in baseline['canonical'].items():
    if route not in docs: failures.append('Missing original route '+route)
    elif docs[route].canonical!=canonical: failures.append('Changed canonical '+route)
for source,digest in baseline['post_sha256'].items():
    if hashlib.sha256(Path(source).read_bytes()).hexdigest()!=digest: failures.append('Changed article source '+source)
for ident in baseline['tag_ids']:
    if ident not in docs['/tags/'].ids: failures.append('Missing legacy tag fragment '+ident)
for route,page in docs.items():
    if page.h1!=1: failures.append(f'{route}: expected one h1, got {page.h1}')
    if len(page.ids)!=len(set(page.ids)): failures.append('Duplicate fragment IDs '+route)
    if route.startswith('/blog/'):
        if len(page.giscus)!=1: failures.append('Expected one Giscus embed '+route)
        else:
            g=page.giscus[0]
            expected={'data-mapping':'url','data-repo':'ganesh47/ganesh47.github.io','data-repo-id':'R_kgDOM_0m6Q','data-category-id':'DIC_kwDOM_0m6c4Co1Zg'}
            for key,value in expected.items():
                if g.get(key)!=value: failures.append(f'{route}: incorrect {key}')
        source=(ROOT/route.lstrip('/')/'index.html').read_text()
        if 'lunr-store' in source or 'lunr.min' in source: failures.append('Redundant search engine '+route)
feed=ET.parse(ROOT/'feed.xml')
ids=[x.text for x in feed.findall('.//{http://www.w3.org/2005/Atom}entry/{http://www.w3.org/2005/Atom}id')]
if set(ids)!=set(baseline['feed_ids']): failures.append('RSS entry URL identities changed')
sitemap=ET.parse(ROOT/'sitemap.xml')
locations={x.text for x in sitemap.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')}
for route in baseline['canonical']:
    if route!='/404.html' and ORIGIN+route not in locations: failures.append('Missing sitemap URL '+route)
current_broken=broken(ROOT,docs)
new_broken=current_broken-set(baseline['known_broken_links'])
failures.extend('New broken link '+x for x in sorted(new_broken))
for path in ('Agents.md','AGENTS.md','README.md','package.json','Gemfile.lock','tests','scripts','.github'):
    if (ROOT/path).exists(): failures.append('Maintenance file published '+path)
discovery=json.loads(Path('_data/discovery.json').read_text())
if set(discovery)!={r for r in docs if r.startswith('/blog/')}: failures.append('Discovery metadata does not cover every article')
summary={'html_routes':len(docs),'original_routes_preserved':len(baseline['canonical']),'article_sources_unchanged':len(baseline['post_sha256']),'legacy_tag_fragments':len(baseline['tag_ids']),'remaining_preexisting_broken_links':len(current_broken),'new_broken_links':len(new_broken),'failures':failures}
Path('validation-results').mkdir(exist_ok=True)
Path('validation-results/site-check.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
sys.exit(bool(failures))
