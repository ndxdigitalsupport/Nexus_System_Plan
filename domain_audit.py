import json

with open('inspection_report.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Analyze domains and SSL
summary_table = []
for name, d in data.items():
    url = d['url']
    is_vercel = 'vercel.app' in url
    domain = url.split('/')[2]
    title = d.get('title', 'N/A')
    links_cnt = d.get('all_links_count', 0)
    has_login = len(d.get('login_links', [])) > 0
    frameworks = ", ".join(d.get('frameworks', [])) or 'Custom HTML/CSS'
    summary_table.append({
        'name': name,
        'domain': domain,
        'is_vercel': is_vercel,
        'has_custom_domain': not is_vercel,
        'title': title,
        'has_login': has_login,
        'frameworks': frameworks
    })

print(json.dumps(summary_table, indent=2))

