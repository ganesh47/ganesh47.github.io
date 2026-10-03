"""Exclude repeated series maps from indexing without changing article prose."""
from pathlib import Path
import re, json, subprocess

for path in Path('_site/blog').glob('*/index.html'):
    source = path.read_text()
    def exclude(match):
        text = re.sub('<[^>]*>', '', match[1]).strip()
        if text.startswith(('Series:', 'Series map:', 'Part-1')) or re.match(r'^Part \d+ of (the series|\d+)', text):
            return '<p data-pagefind-ignore>' + match[1] + '</p>'
        return match[0]
    path.write_text(re.sub(r'<p>(.*?)</p>', exclude, source, flags=re.S))
Path('_site/.nojekyll').touch()
revision = subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
assert re.fullmatch('[0-9a-f]{40}', revision)
Path('_site/build-revision.json').write_text(json.dumps({'source_sha':revision,'theme_sha':'7c68402e079564981274be1d07da0387e3ebdf97','search':'pagefind-1.4.0'},indent=2)+'\n')
