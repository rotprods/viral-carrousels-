from pathlib import Path
from bs4 import BeautifulSoup
import sys

path = Path(sys.argv[1] if len(sys.argv) > 1 else '_site/index.html')
html = path.read_text(encoding='utf-8')
s = BeautifulSoup(html, 'html.parser')
errors = []

ids = [x.get('id') for x in s.find_all(attrs={'id': True})]
for item in sorted(set(ids)):
    if ids.count(item) > 1:
        errors.append(f'duplicate id: {item}')

for img in s.find_all('img'):
    src = img.get('src', '')
    if not img.get('alt'):
        errors.append('image missing alt')
    if src.startswith('data:image/gif') and 'R0lGODlhAQABA' in src:
        errors.append('transparent 1x1 placeholder detected')
    if not src.startswith('data:'):
        target = path.parent / src
        if not target.exists():
            errors.append(f'missing image asset: {src}')

for a in s.find_all('a', href=True):
    href = a['href']
    if href.startswith('#') and href != '#' and not s.find(id=href[1:]):
        errors.append(f'broken internal link: {href}')

for i in range(18):
    pid = f'prompt-p{i:02d}'
    if not s.find(id=pid):
        errors.append(f'missing prompt: P{i:02d}')

if 'g-697fac8775c081919387509ec73c69a5-extractor-adn-visual-v2' not in html:
    errors.append('Extractor ADN Visual v2 link missing')

if 'execCommand' not in html and 'navigator.clipboard' not in html:
    errors.append('copy engine missing')

print(f'QA: {path} | images={len(s.find_all("img"))} prompts=18 errors={len(errors)}')
for error in errors:
    print('ERROR:', error)
raise SystemExit(1 if errors else 0)
