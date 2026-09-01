from pathlib import Path
from bs4 import BeautifulSoup
import re, sys

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
    if src and not src.startswith(('data:', 'http://', 'https://')):
        target = path.parent / src.split('?', 1)[0].split('#', 1)[0]
        if not target.exists():
            errors.append(f'missing image asset: {src}')

for a in s.find_all('a', href=True):
    href = a['href']
    if href.startswith('#') and href != '#' and not s.find(id=href[1:]):
        errors.append(f'broken internal link: {href}')

# Prompt OS has one source of truth: published prompts/PROMPTS.md.
prompt_source = path.parent / 'prompts' / 'PROMPTS.md'
if not prompt_source.exists():
    errors.append('canonical prompts/PROMPTS.md missing from staged site')
else:
    prompt_text = prompt_source.read_text(encoding='utf-8')
    found = set(re.findall(r'^##\s+(P\d{2})\b', prompt_text, flags=re.M))
    expected = {f'P{i:02d}' for i in range(18)}
    for pid in sorted(expected - found):
        errors.append(f'missing canonical prompt: {pid}')

if 'prompt-grid' not in html or "fetch('prompts/PROMPTS.md')" not in html:
    errors.append('canonical prompt runtime loader missing')
if 'g-697fac8775c081919387509ec73c69a5-extractor-adn-visual-v2' not in html:
    errors.append('Extractor ADN Visual v2 link missing')
if 'execCommand' not in html and 'navigator.clipboard' not in html:
    errors.append('copy engine missing')

# Portable executable-system sources must ship with Pages.
for rel in [
    'templates/visual-dna.template.json', 'templates/DESIGN.template.md',
    'skills/visual-brand-system/SKILL.md', 'adapters/CODEX.md',
    'adapters/CLAUDE_CODE.md', 'adapters/HIGGSFIELD_SUPERCOMPUTER.md'
]:
    if not (path.parent / rel).exists():
        errors.append(f'missing published source: {rel}')

print(f'QA: {path} | images={len(s.find_all("img"))} canonical_prompts=18 errors={len(errors)}')
for error in errors:
    print('ERROR:', error)
raise SystemExit(1 if errors else 0)
