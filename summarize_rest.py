import json

with open('inspection_report.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for name in ['Ecommerce', 'Nexusfinance', 'Nexus Affiliate', 'Talently Careers']:
    info = data[name]
    print('='*60)
    print("PROPERTY: " + name)
    print("URL: " + str(info.get('url')) + " | Final: " + str(info.get('final_url')))
    print("Title: " + str(info.get('title')))
    desc = info.get('meta', {}).get('description') or info.get('meta', {}).get('og:description')
    print("Description: " + str(desc))
    print("Frameworks: " + ", ".join(info.get('frameworks', [])))
    print("Headings:")
    for tag, h in info.get('headings', [])[:8]:
        print(f"  [{tag}] {h}")
    print("Login/Auth Links: " + str(info.get('login_links')))
    print("Nexus Ecosystem Cross-links: " + str(info.get('nexus_links')))
    print("Colors: " + str(info.get('hex_colors')[:10]))
    print("Top Links:")
    for l in info.get('top_links', [])[:8]:
        print(f"  -> {l.get('text')} ({l.get('href')})")
    print("Sample Text:")
    print("  " + " | ".join(info.get('sample_content', [])[:10]))

