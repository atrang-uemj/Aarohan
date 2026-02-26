import re

with open('e:/AArohan/html_chunk.txt', 'r', encoding='utf-8') as f:
    html_chunk = f.read()

with open('e:/AArohan/js_chunk.txt', 'r', encoding='utf-8') as f:
    js_chunk = f.read()

with open('e:/AArohan/dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace HTML options
content = re.sub(
    r'<div class="custom-optgroup">Central Institutions.*?College Outside Jaipur</span>\s*</div>',
    html_chunk.strip(),
    content,
    flags=re.DOTALL
)

# Replace JS object
content = re.sub(
    r'const COLLEGE_DOMAINS = \{.*?\};',
    js_chunk.strip(),
    content,
    flags=re.DOTALL
)

with open('e:/AArohan/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Injected successfully!')
