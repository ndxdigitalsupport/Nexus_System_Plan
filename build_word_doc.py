import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=120, bottom=120, left=160, right=160):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def add_header(doc, text, level=1):
    h = doc.add_heading(text, level=level)
    h.paragraph_format.space_before = Pt(16)
    h.paragraph_format.space_after = Pt(6)
    run = h.runs[0]
    if level == 1:
        run.font.size = Pt(17)
        run.font.color.rgb = RGBColor(15, 23, 42) # Slate 900
        run.font.bold = True
    elif level == 2:
        run.font.size = Pt(13)
        run.font.color.rgb = RGBColor(124, 92, 252) # Tech Violet
        run.font.bold = True
    elif level == 3:
        run.font.size = Pt(11)
        run.font.color.rgb = RGBColor(43, 59, 255) # Cobalt
        run.font.bold = True
    return h

def create_styled_table(doc, headers, data, col_widths=None):
    table = doc.add_table(rows=len(data) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    # Header Row
    hdr_cells = table.rows[0].cells
    for i, title in enumerate(headers):
        hdr_cells[i].text = title
        set_cell_background(hdr_cells[i], "0F172A") # Deep Navy / Slate
        set_cell_margins(hdr_cells[i], top=140, bottom=140, left=160, right=160)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        for run in p.runs:
            run.font.bold = True
            run.font.size = Pt(9.5)
            run.font.color.rgb = RGBColor(255, 255, 255)

    # Data Rows
    for r_idx, row_data in enumerate(data):
        row_cells = table.rows[r_idx + 1].cells
        bg_color = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate(row_data):
            row_cells[c_idx].text = str(val)
            set_cell_background(row_cells[c_idx], bg_color)
            set_cell_margins(row_cells[c_idx], top=110, bottom=110, left=160, right=160)
            p = row_cells[c_idx].paragraphs[0]
            for run in p.runs:
                run.font.size = Pt(9)
                run.font.color.rgb = RGBColor(51, 65, 85)

    if col_widths:
        for row in table.rows:
            for c_idx, width in enumerate(col_widths):
                row.cells[c_idx].width = Inches(width)

    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="6" w:space="0" w:color="CBD5E1"/>'
        f'<w:bottom w:val="single" w:sz="8" w:space="0" w:color="94A3B8"/>'
        f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>'
        f'<w:insideV w:val="none"/>'
        f'<w:left w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)
    doc.add_paragraph().paragraph_format.space_after = Pt(6)
    return table

def add_callout(doc, text, title="STRATEGIC EXECUTIVE DIRECTIVE"):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    cell = table.rows[0].cells[0]
    cell.width = Inches(6.5)
    set_cell_background(cell, "F5F3FF") # Violet soft tint
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)

    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:left w:val="single" w:sz="24" w:space="0" w:color="7C5CFC"/>'
        f'<w:top w:val="none"/>'
        f'<w:bottom w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)

    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(4)
    run_t = p.add_run(f"★ {title}\n")
    run_t.font.bold = True
    run_t.font.size = Pt(10)
    run_t.font.color.rgb = RGBColor(124, 92, 252)

    run_b = p.add_run(text)
    run_b.font.size = Pt(9.5)
    run_b.font.color.rgb = RGBColor(51, 65, 85)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

doc = Document()

# Page Margins
for section in doc.sections:
    section.top_margin = Inches(0.9)
    section.bottom_margin = Inches(0.9)
    section.left_margin = Inches(0.9)
    section.right_margin = Inches(0.9)

# HEADER COVER BLOCK
p_meta = doc.add_paragraph()
r_badge = p_meta.add_run("NEXUS GROUP INTERNATIONAL · EXECUTIVE AUDIT & DESIGN SYSTEM")
r_badge.font.bold = True
r_badge.font.size = Pt(9)
r_badge.font.color.rgb = RGBColor(124, 92, 252)

p_title = doc.add_paragraph()
p_title.paragraph_format.space_before = Pt(4)
p_title.paragraph_format.space_after = Pt(8)
r_title = p_title.add_run("Nexus Ecosystem Master Audit,\nBrand Guidebook & Digital Portfolio")
r_title.font.bold = True
r_title.font.size = Pt(24)
r_title.font.color.rgb = RGBColor(15, 23, 42)

p_sub = doc.add_paragraph()
p_sub.paragraph_format.space_after = Pt(14)
r_sub = p_sub.add_run("Complete operational inspection across 9 live web properties, UX/UI analysis, authentication architecture, bilingual branding, and future development roadmap.")
r_sub.font.size = Pt(11)
r_sub.font.color.rgb = RGBColor(100, 116, 139)

# Metadata Table
meta_headers = ["Document Version", "Target Reviewer", "Ecosystem Scope", "Preparation Date"]
meta_data = [["1.1.0 (Executive Edition)", "Oum Naro & Leadership Team", "9 Live Properties (6 Products + 3 Services)", "November 2026"]]
create_styled_table(doc, meta_headers, meta_data, [1.6, 1.8, 2.1, 1.2])

# SECTION 1: EXECUTIVE SUMMARY
add_header(doc, "1. Executive Summary & Ecosystem Overview", level=1)
p_intro = doc.add_paragraph(
    "Following executive instructions, an in-depth technical and UX/UI inspection was performed across all "
    "nine (9) active web properties within the Nexus ecosystem. The organization operates under two distinct pillars: "
    "Pillar 1 focuses on digital software products (primarily Telegram-native tools and SaaS platforms tailored for Cambodian SMEs and regional markets), "
    "while Pillar 2 encompasses professional services (AI agency engineering, enterprise consulting, and Singapore-based executive search)."
)
p_intro.paragraph_format.space_after = Pt(8)

kpi_headers = ["Metric", "Status", "Operational Context"]
kpi_data = [
    ["Total Live Web Properties", "9 Active Sites", "100% HTTP 200 uptime across all surveyed endpoints."],
    ["Digital Products Pillar", "6 Properties", "AiOS, CRM, Commerce, Finance, Affiliate, Talently Careers."],
    ["Professional Services Pillar", "3 Properties", "Nexus Digital (Intelligence), AI Consulting, Vertex Partners."],
    ["Telegram Bot Integrations", "5 Active Bots", "@nexuscrm_official_bot, @ndxdigital_support, @nexusdigital_affiliates_bot, @talently_job_alerts_bot, @DanLP18."],
    ["Primary Design Rating", "9.3 / 10 Average", "High modern UI maturity; responsive layouts, dark modes, and native Khmer localization."]
]
create_styled_table(doc, kpi_headers, kpi_data, [2.0, 1.5, 3.2])

add_callout(
    doc,
    "The core finding of this audit is that while each property possesses world-class visual design and strong standalone functionality, "
    "the properties currently operate as isolated islands. Furthermore, four (4) properties still operate on temporary *.vercel.app subdomains. "
    "Unifying these domains under *.nexus.asia and injecting a shared ecosystem navigation header (nexus-global-bar.js) will immediately multiply brand equity and cross-sell conversions.",
    title="KEY AUDIT FINDING & STRATEGIC OPPORTUNITY"
)

# SECTION 2: DIGITAL PRODUCTS AUDIT (6 PROPERTIES)
add_header(doc, "2. Pillar 1: Digital Products & Platforms Audit", level=1)

products_audit = [
    {
        "name": "1. Nexus AiOS",
        "url": "https://nexus-aios-ashy.vercel.app/",
        "target_url": "https://aios.nexus.asia",
        "category": "Digital Product (Executive AI Operating System)",
        "tech": "Next.js 14, React, Tailwind CSS",
        "ux": "Sleek dark obsidian (#101014) and tech violet (#7C5CFC) palette. Bilingual Khmer/English toggle.",
        "auth": "Active /login and /signup pages with tiered starter, growth, and enterprise plan selection.",
        "connections": "Isolated island. Does not link to Nexus CRM or Nexus Digital.",
        "action": "Migrate from Vercel subdomain to aios.nexus.asia; integrate Telegram OAuth Login Widget."
    },
    {
        "name": "2. Nexus Pro CRM",
        "url": "https://nexus-crm-liard.vercel.app/",
        "target_url": "https://crm.nexus.asia",
        "category": "Digital Product (Vertical B2B Professional Services CRM)",
        "tech": "Next.js 14, React, Tailwind CSS",
        "ux": "Clean slate SaaS design (#0F172A, #3B82F6). Highly legible tables for proposals, invoices, and contracts.",
        "auth": "Dual login portals: /portal (Client Portal) and /dashboard/login (Firm Staff Login).",
        "connections": "Linked to official Telegram bot (@nexuscrm_official_bot). No cross-links to Nexus Finance.",
        "action": "Migrate to crm.nexus.asia; connect invoice payment links directly to Nexus Finance KHQR gateway."
    },
    {
        "name": "3. NEXUS Commerce",
        "url": "https://nexuscommerce.asia/",
        "target_url": "https://nexuscommerce.asia (Active)",
        "category": "Digital Product (Telegram Social Commerce & Mini-Shops)",
        "tech": "Responsive HTML5, Tailwind CSS",
        "ux": "High energy retail palette: Electric Indigo (#4338CA) & Coral (#E1251B). Live interactive demo stores.",
        "auth": "Platform access at app.nexuscommerce.asia; merchant assistance via @ndxdigital_support.",
        "connections": "Custom domain active. Integrated with ABA PayWay and Bakong KHQR checkout flows.",
        "action": "Add global ecosystem header; enable 1-click merchant onboarding via Telegram bot."
    },
    {
        "name": "4. Nexus Finance",
        "url": "https://nexusfinance.asia/",
        "target_url": "https://nexusfinance.asia (Active)",
        "category": "Digital Product / FinTech Gateway",
        "tech": "Modern Web, Custom CSS, Kantumruy Pro & Koulen Khmer Fonts",
        "ux": "Modern FinTech styling: Deep Navy (#0F172A), Mint/Cyan (#00D4BE), and Gold accents.",
        "auth": "Pre-launch / waitlist lead generation via CTA forms and direct Telegram inquiry.",
        "connections": "Custom domain active. Connected to official Nexus Digital Facebook & LinkedIn social pages.",
        "action": "Build out interactive merchant dashboard; unify settlement APIs with Nexus Commerce & CRM."
    },
    {
        "name": "5. Nexus Affiliate",
        "url": "https://nexus-digital-affiliates.vercel.app/join.html",
        "target_url": "https://affiliates.nexus.asia",
        "category": "Digital Product (Performance Partner Network)",
        "tech": "Modern HTML5/CSS, Material Symbols",
        "ux": "High-conversion landing page: Royal Blue (#0066FF) and Gold badges with interactive earnings calculator.",
        "auth": "Partner sign-in via index.html; automated Telegram partner bot (@nexusdigital_affiliates_bot).",
        "connections": "Promotes Nexus digital suite; payouts handled directly via ABA Bank accounts.",
        "action": "Migrate to affiliates.nexus.asia; embed live referral link generator directly inside the web portal."
    },
    {
        "name": "6. Talently Careers",
        "url": "https://talentlycareers.site/",
        "target_url": "https://talentlycareers.site (or talently.asia)",
        "category": "Digital Product (Cambodia Job Board & Marketplace)",
        "tech": "HTML5, Plus Jakarta Sans, Inter, Material Symbols",
        "ux": "Modern hiring platform layout: Emerald (#10B981) and Vibrant Blue (#3B82F6).",
        "auth": "Dual portal pathways: Candidate Sign-in (login.html), Candidate Dashboard, and Employer Post-a-Job.",
        "connections": "Custom domain active. Automated job notifications delivered via @talently_job_alerts_bot.",
        "action": "Position as the operational talent pipeline for Vertex Partners executive search clients."
    }
]

for p in products_audit:
    add_header(doc, p["name"], level=2)
    t_headers = ["Audit Dimension", "Evaluation Details"]
    t_data = [
        ["Current Live URL", p["url"]],
        ["Target Production URL", p["target_url"]],
        ["Product Category", p["category"]],
        ["Technology Stack", p["tech"]],
        ["UX / UI & Localization", p["ux"]],
        ["Login & Authentication", p["auth"]],
        ["Ecosystem Connections", p["connections"]],
        ["Recommended Next Action", p["action"]]
    ]
    create_styled_table(doc, t_headers, t_data, [2.0, 4.7])

# SECTION 3: SERVICES AUDIT (3 PROPERTIES)
add_header(doc, "3. Pillar 2: Nexus Services & Consulting Audit", level=1)

services_audit = [
    {
        "name": "7. Nexus Digital (Nexus Intelligence Agency)",
        "url": "https://nexusintelligence-agency.vercel.app/",
        "target_url": "https://nexusintelligence.asia",
        "category": "Professional Service (AI Agency, Web Development & Growth)",
        "tech": "Next.js 14, React, Tailwind CSS",
        "ux": "Futuristic agency aesthetic: Deep Midnight Violet (#2A1E5C), Electric Blue (#2B3BFF), lavender glow.",
        "auth": "Direct client intake workflows; sticky Telegram sales chat widget connected to leadership (@DanLP18).",
        "connections": "Serves as the foundational development agency that created the digital products suite.",
        "action": "Move to apex domain nexusintelligence.asia; feature AiOS, CRM, and Commerce in case studies."
    },
    {
        "name": "8. Nexus AI Consulting",
        "url": "https://www.nexusaipro.site/",
        "target_url": "https://nexusaipro.site (Active)",
        "category": "Professional Service (Enterprise AI Platform & Advisory)",
        "tech": "Tailwind CSS, React, Interactive Demo App (app.html)",
        "ux": "Silicon Valley SaaS aesthetic (Linear/Apple style) with dark mode, amber accents, and glowing badges.",
        "auth": "Direct interactive web trial accessible via app.html with enterprise consultation inquiry forms.",
        "connections": "Custom domain active. Positions high-end AI workflow memory and reasoning models for scale-ups.",
        "action": "Integrate scheduling calendar (Calendly/Cal.com) directly on landing page for enterprise demo booking."
    },
    {
        "name": "9. Vertex Partners",
        "url": "https://vertexpartners.asia/",
        "target_url": "https://vertexpartners.asia (Active)",
        "category": "Professional Service (Executive Management & HR Search)",
        "tech": "WordPress, Elementor, Tailwind styling, Google Fonts (Roboto Slab, Montserrat, Playfair)",
        "ux": "Tier-1 executive consulting aesthetic: Corporate Navy (#0F172A), Sapphire (#046BD2), and Crimson (#CF2E2E).",
        "auth": "Corporate consultation booking and client inquiry contact forms.",
        "connections": "Custom domain active. Headquarters in Singapore with APAC-wide executive recruitment network.",
        "action": "Establish direct cross-linking with Talently Careers for mid-tier vs C-suite hiring funnels."
    }
]

for s in services_audit:
    add_header(doc, s["name"], level=2)
    t_headers = ["Audit Dimension", "Evaluation Details"]
    t_data = [
        ["Current Live URL", s["url"]],
        ["Target Production URL", s["target_url"]],
        ["Service Category", s["category"]],
        ["Technology Stack", s["tech"]],
        ["UX / UI Assessment", s["ux"]],
        ["Conversion & Auth Flow", s["auth"]],
        ["Ecosystem Synergy", s["connections"]],
        ["Recommended Next Action", s["action"]]
    ]
    create_styled_table(doc, t_headers, t_data, [2.0, 4.7])

# SECTION 4: CROSS-ECOSYSTEM CONNECTIONS
add_header(doc, "4. Cross-Ecosystem Analysis & Connections Matrix", level=1)

matrix_headers = ["Property", "UX/UI Score", "Auth / Login Status", "Telegram Bot / Link", "Domain Status"]
matrix_data = [
    ["1. AiOS", "9.5 / 10", "Active (/login, /signup)", "Direct in-app reporting", "Needs aios.nexus.asia"],
    ["2. Nexus Pro CRM", "9.0 / 10", "Dual (/portal, /dashboard)", "@nexuscrm_official_bot", "Needs crm.nexus.asia"],
    ["3. Commerce", "9.2 / 10", "Web app (app.nexus...)", "@ndxdigital_support", "Production .asia Active"],
    ["4. Finance", "8.8 / 10", "Pre-launch / Lead Form", "@ndxdigital_support", "Production .asia Active"],
    ["5. Affiliate", "9.0 / 10", "Partner Login (index.html)", "@nexusdigital_affiliates_bot", "Needs affiliates.nexus.asia"],
    ["6. Talently", "9.3 / 10", "Dual (Candidate/Employer)", "@talently_job_alerts_bot", "Production .site Active"],
    ["7. Digital Agency", "9.8 / 10", "Project Intake", "@DanLP18 (Leadership)", "Needs nexusintelligence.asia"],
    ["8. AI Consulting", "9.6 / 10", "Live Trial (app.html)", "Direct Web Demo", "Production .site Active"],
    ["9. Vertex Partners", "9.1 / 10", "Corporate Inquiry", "Email & Web Form", "Production .asia Active"]
]
create_styled_table(doc, matrix_headers, matrix_data, [1.5, 1.0, 1.6, 1.3, 1.3])

# SECTION 5: INTERNAL BRANDED GUIDEBOOK
add_header(doc, "5. Internal Branded Guidebook (Design System & Standards)", level=1)

add_header(doc, "5.1 Standardized Corporate Naming Hierarchy", level=2)
doc.add_paragraph(
    "• Level 1: Parent Conglomerate — Nexus Group International / Nexus Holdings\n"
    "• Level 2A: Digital Products — Nexus AiOS™, Nexus CRM™, Nexus Commerce™, Nexus Finance™, Nexus Partner Network™\n"
    "• Level 2B: Professional Services — Nexus Intelligence Agency™, Nexus AI Enterprise™\n"
    "• Level 2C: Regional Human Capital & Advisory — Vertex Partners Singapore™, Talently by Vertex™"
)

add_header(doc, "5.2 Color Palette Specifications (HEX, RGB & Usage)", level=2)
color_headers = ["Color Name", "HEX Code", "RGB Values", "Primary Usage & Application"]
color_data = [
    ["Nexus Tech Violet", "#7C5CFC", "RGB(124, 92, 252)", "AiOS, Primary CTAs, Brand Glow, Main Technology Identity."],
    ["Electric Cobalt", "#2B3BFF", "RGB(43, 59, 255)", "Nexus Digital Agency, High-converting action buttons."],
    ["FinTech Mint/Cyan", "#00D4BE", "RGB(0, 212, 190)", "Nexus Finance, Payment Trust Badges, Security Indicators."],
    ["Commerce Coral Red", "#E1251B", "RGB(225, 37, 27)", "Nexus Commerce, Retail Action, PayWay Checkout Harmony."],
    ["Success Emerald", "#10B981", "RGB(16, 185, 129)", "Talently Careers, Live Status Badges, Candidate Verification."],
    ["Corporate Sapphire", "#046BD2", "RGB(4, 107, 210)", "Vertex Partners Singapore, Institutional Advisory Pedigree."],
    ["Obsidian Dark", "#101014", "RGB(16, 16, 20)", "Global Dark Mode Background, High-contrast surface."],
    ["Surface Crisp Light", "#F6F6FA", "RGB(246, 246, 250)", "Clean Light Mode card backgrounds and divider borders."]
]
create_styled_table(doc, color_headers, color_data, [1.5, 1.0, 1.3, 2.9])

add_header(doc, "5.3 Bilingual Typography Pairing System", level=2)
type_headers = ["Script / Language", "Heading & Display Font", "Body & UI Font", "Design Rules"]
type_data = [
    ["English (Latin)", "Plus Jakarta Sans (600/700/800)", "Inter (400/500/600)", "Modern, geometric, ultra-legible across high-DPI displays."],
    ["Khmer (ភាសាខ្មែរ)", "Koulen or Kantumruy Pro (Bold)", "Kantumruy Pro (Regular/Medium)", "Matches Latin weight proportions; eliminates clipping on vowel signs."],
    ["Financials & Metrics", "Space Grotesk (Bold)", "Space Grotesk (Regular)", "Monospace clarity for USD/KHR balances, KHQR data, and code."]
]
create_styled_table(doc, type_headers, type_data, [1.3, 1.8, 1.8, 1.8])

# SECTION 6: FUTURE UPDATE ROADMAP
add_header(doc, "6. Digital Asset Packaging & Future Update Roadmap", level=1)

roadmap_headers = ["Implementation Phase", "Focus Area", "Technical Tasks & Deliverables", "Target Timeline"]
roadmap_data = [
    [
        "Phase 1: Immediate",
        "Domain Consolidation",
        "Migrate AiOS, CRM, Affiliate, and Agency from *.vercel.app to *.nexus.asia apex domains. Provision Cloudflare SSL.",
        "Week 1 - 2"
    ],
    [
        "Phase 2: Immediate",
        "Ecosystem Navigation Bar",
        "Embed nexus-global-bar.js across all 9 web properties to cross-sell services and resolve site isolation.",
        "Week 2"
    ],
    [
        "Phase 3: High Priority",
        "Unified Nexus SSO (Pass)",
        "Implement single sign-on across AiOS, CRM, and Commerce using Telegram OAuth + Phone OTP authentication.",
        "Week 3 - 4"
    ],
    [
        "Phase 4: Strategic",
        "Financial Engine Unification",
        "Connect Nexus Commerce and Nexus CRM billing pipelines directly to the Nexus Finance KHQR payment hub.",
        "Month 2"
    ]
]
create_styled_table(doc, roadmap_headers, roadmap_data, [1.3, 1.4, 3.0, 1.0])

output_path = r"c:\Users\Asus\Desktop\Help 2\NEXUS_ECOSYSTEM_AUDIT_AND_BRAND_GUIDEBOOK.docx"
doc.save(output_path)
print(f"Successfully updated: {output_path}")
