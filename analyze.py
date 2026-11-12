import urllib.request
import ssl
import re
from html.parser import HTMLParser
import json
import os

urls = {
    'AiOS': 'https://nexus-aios-ashy.vercel.app/',
    'CRM': 'https://nexus-crm-liard.vercel.app/',
    'Ecommerce': 'https://nexuscommerce.asia/',
    'Nexusfinance': 'https://nexusfinance.asia/',
    'Nexus Affiliate': 'https://nexus-digital-affiliates.vercel.app/join.html',
    'Talently Careers': 'https://talentlycareers.site/',
    'Nexus Digital': 'https://nexusintelligence-agency.vercel.app/',
    'Ai Consulting': 'https://www.nexusaipro.site/',
    'Business Consultant': 'https://vertexpartners.asia/'
}

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

class DetailedParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ''
        self.in_title = False
        self.meta = {}
        self.links = []
        self.headings = []
        self.current_tag = ''
        self.current_attrs = {}
        self.text_chunks = []
        self.scripts = []
        self.stylesheets = []
        self.buttons = []
        self.inputs = []
        self.forms = []
        self.current_a = None

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        attrs_dict = dict(attrs)
        self.current_attrs = attrs_dict

        if tag == 'title':
            self.in_title = True
        elif tag == 'meta':
            name = attrs_dict.get('name') or attrs_dict.get('property')
            content = attrs_dict.get('content')
            if name and content:
                self.meta[name] = content
        elif tag == 'a':
            self.current_a = {
                'href': attrs_dict.get('href', ''),
                'text': '',
                'class': attrs_dict.get('class', '')
            }
        elif tag == 'button':
            self.buttons.append({
                'type': attrs_dict.get('type', ''),
                'class': attrs_dict.get('class', '')
            })
        elif tag == 'input':
            self.inputs.append({
                'type': attrs_dict.get('type', ''),
                'placeholder': attrs_dict.get('placeholder', ''),
                'name': attrs_dict.get('name', '')
            })
        elif tag == 'form':
            self.forms.append({
                'action': attrs_dict.get('action', ''),
                'method': attrs_dict.get('method', '')
            })
        elif tag == 'link':
            rel = attrs_dict.get('rel', '')
            href = attrs_dict.get('href', '')
            if 'stylesheet' in rel and href:
                self.stylesheets.append(href)
        elif tag == 'script':
            src = attrs_dict.get('src', '')
            if src:
                self.scripts.append(src)

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
        elif tag == 'a' and self.current_a:
            self.links.append(self.current_a)
            self.current_a = None
        self.current_tag = ''
        self.current_attrs = {}

    def handle_data(self, data):
        cleaned = data.strip()
        if not cleaned:
            return
        if self.in_title:
            self.title += " " + cleaned
        elif self.current_a is not None:
            self.current_a['text'] += (" " + cleaned if self.current_a['text'] else cleaned)
        elif self.current_tag in ['h1', 'h2', 'h3', 'h4']:
            self.headings.append((self.current_tag, cleaned))
        elif self.current_tag not in ['script', 'style']:
            self.text_chunks.append(cleaned)

results = {}
os.makedirs('scraped_pages', exist_ok=True)

for name, url in urls.items():
    print(f"Scraping {name} ({url})...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=20) as resp:
            content_bytes = resp.read()
            html = content_bytes.decode('utf-8', errors='ignore')
            final_url = resp.geturl()

            safe_name = re.sub(r'[^a-zA-Z0-9_-]', '_', name)
            with open(f"scraped_pages/{safe_name}.html", "w", encoding="utf-8") as f:
                f.write(html)

            parser = DetailedParser()
            parser.feed(html)

            # Extract color schemes
            hex_colors = list(set(re.findall(r'#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b', html)))
            # Extract rgb/rgba
            rgb_colors = list(set(re.findall(r'rgba?\([^)]+\)', html)))

            # Check framework signatures
            frameworks = []
            if '__NEXT_DATA__' in html or '/_next/' in html:
                frameworks.append('Next.js')
            if 'react' in html.lower() or '_react' in html:
                frameworks.append('React')
            if 'vue' in html.lower():
                frameworks.append('Vue')
            if 'tailwind' in html.lower() or 'text-' in html and 'bg-' in html:
                frameworks.append('Tailwind CSS')
            if 'bootstrap' in html.lower():
                frameworks.append('Bootstrap')
            if 'webflow' in html.lower():
                frameworks.append('Webflow')
            if 'framer' in html.lower():
                frameworks.append('Framer')

            # Identify login/auth mentions
            login_links = [l for l in parser.links if any(w in l['href'].lower() or w in l['text'].lower() for w in ['login', 'signin', 'sign-in', 'auth', 'portal', 'dashboard', 'register', 'signup', 'sign-up'])]

            # Inter-site links (links to other nexus properties)
            nexus_mentions = [l for l in parser.links if any(domain in l['href'].lower() for domain in ['nexus', 'talently', 'vertex'])]

            results[name] = {
                'url': url,
                'final_url': final_url,
                'title': parser.title.strip(),
                'meta': parser.meta,
                'frameworks': frameworks,
                'headings': parser.headings[:20],
                'login_links': login_links,
                'nexus_links': nexus_mentions,
                'all_links_count': len(parser.links),
                'top_links': parser.links[:25],
                'forms_count': len(parser.forms),
                'inputs': parser.inputs[:10],
                'hex_colors': [f"#{c}" for c in hex_colors[:25]],
                'stylesheets': parser.stylesheets,
                'scripts': parser.scripts[:15],
                'sample_content': parser.text_chunks[:30]
            }
    except Exception as e:
        results[name] = {
            'url': url,
            'error': str(e)
        }

with open('inspection_report.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2)

print("Inspection completed successfully!")

