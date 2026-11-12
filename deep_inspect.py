import os
import re
import glob

# Check if BeautifulSoup is installed, else regex
html_files = glob.glob('scraped_pages/*.html')

for fpath in sorted(html_files):
    name = os.path.basename(fpath).replace('.html', '')
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # fonts in links
    font_links = re.findall(r'href=[\'"]([^\'"]*fonts\.googleapis\.com[^\'"]*)[\'"]', html)
    font_families = re.findall(r'family=([a-zA-Z0-9+:,;]+)', "".join(font_links))
    
    # inline font families
    inline_fonts = re.findall(r'font-family:\s*([^;\'"}\n]+)', html, re.I)
    
    # title
    title = re.search(r'<title>(.*?)</title>', html, re.I | re.S)
    title_str = title.group(1).strip() if title else 'No title'
    
    # forms/inputs
    forms = re.findall(r'<form[^>]*>', html, re.I)
    inputs = re.findall(r'<input[^>]*>', html, re.I)
    buttons = re.findall(r'<button[^>]*>(.*?)</button>', html, re.I | re.S)
    
    print(f"=== {name} ===")
    print(f"Title: {title_str}")
    print(f"Google Fonts: {font_families}")
    print(f"Inline Fonts: {list(set(inline_fonts))[:5]}")
    print(f"Forms count: {len(forms)}, Inputs count: {len(inputs)}, Buttons count: {len(buttons)}")
    
    # check telegram links
    telegram_links = re.findall(r'https?://t\.me/[^\s\'"<>]+', html)
    print(f"Telegram links: {list(set(telegram_links))}")
    print()
