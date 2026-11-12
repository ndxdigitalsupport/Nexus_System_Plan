import json

with open('inspection_report.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for name, info in data.items():
    print('='*60)
    print(f"PROPERTY: {name}")
    print(f"URL: {info.get('url')} | Final: {info.get('final_url')}")
    print(f"Title: {info.get('title')}")
    print(f"Description: {info.get('meta', {}).get('description') or info.get('meta', {}).get('og:description')}")
    print(f"Frameworks: {', '.join(info.get('frameworks', []))}")
    print(f"Headings:")
    for tag, h in info.get('headings', [])[:6]:
        print(f"  [{tag}] {h}")
    print(f"Login/Auth Links: {info.get('login_links')}")
    print(f"Nexus Ecosystem Cross-links: {info.get('nexus_links')}")
    print(f"Colors: {info.get('hex_colors')[:10]}")
    print(f"Top Links:")
    for l in info.get('top_links', [])[:8]:
        print(f"  -> {l.get('text')} ({l.get('href')})")
    print(f"Sample Text:")
    print("  " + " | ".join(info.get('sample_content', [])[:8]))

