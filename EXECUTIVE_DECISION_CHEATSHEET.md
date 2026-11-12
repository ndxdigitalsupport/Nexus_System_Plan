# NEXUS ECOSYSTEM — 1-PAGE EXECUTIVE DECISION CHEATSHEET
**Target:** Quick 2-Minute Review for Oum Naro & Department Leads  
**Accompanying Document:** `NEXUS_ECOSYSTEM_AUDIT_AND_BRAND_GUIDEBOOK.docx`

---

## 1. AT-A-GLANCE PRIORITIZATION MATRIX

| Priority | Property | Current Status | Primary Bottleneck | Immediate Action Required | Owner |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **P0** | **Nexus Commerce** | Live (`nexuscommerce.asia`) | Islanded; no cross-links to Nexus Finance. | Add global nav bar; link merchant setup to PayWay/KHQR. | Product / Ecom |
| **P0** | **Nexus AiOS** | Live (`nexus-aios-ashy.vercel.app`) | Temporary Vercel URL; missing Telegram OAuth. | Map `aios.nexus.asia`; add Telegram Login Widget. | DevOps / Fullstack |
| **P0** | **Nexus Pro CRM** | Live (`nexus-crm-liard.vercel.app`) | Temporary Vercel URL; isolated invoicing. | Map `crm.nexus.asia`; link billing to Nexus Finance. | DevOps / Backend |
| **P1** | **Nexus Digital (Agency)** | Live (`nexusintelligence-agency...`) | Temporary Vercel URL; products not in portfolio. | Map `nexusintelligence.asia`; showcase AiOS & CRM as case studies. | Marketing / Web |
| **P1** | **Nexus Affiliate** | Live (`nexus-digital-affiliates...`) | Temporary Vercel URL. | Map `affiliates.nexus.asia`; recruit initial 50 partners. | Growth Lead |
| **P2** | **Nexus Finance** | Live (`nexusfinance.asia`) | Pre-launch / Lead capture only. | Develop merchant dashboard; integrate with Commerce. | FinTech Dev |
| **P2** | **Talently Careers** | Live (`talentlycareers.site`) | Operates completely independent of Vertex. | Cross-promote mid-level roles with Vertex Partners C-suite. | HR / Talent |
| **P2** | **Nexus AI Consulting** | Live (`www.nexusaipro.site`) | No direct calendar booking widget. | Add Cal.com / Calendly booking for enterprise demos. | Sales Lead |
| **P2** | **Vertex Partners** | Live (`vertexpartners.asia`) | Standalone WordPress site. | Maintain Singapore executive positioning; link to Talently. | Managing Director |

---

## 2. ANTICIPATED EXECUTIVE QUESTIONS & DIRECT ANSWERS

When Oum Naro reviews the Word document, he will likely ask these three questions. Here are your direct answers:

### Q1: "How much will the domain migration cost and how long will it take?"
* **Cost:** **$0 extra.** We already own or can map subdomains under `nexus.asia`. Let's Encrypt SSL certificates are free and automated via Vercel and Cloudflare.
* **Timeline:** **1 to 2 hours of engineering time.** Cloudflare DNS records propagate in minutes, and Vercel automatically sets up 301 redirects to preserve existing links.

### Q2: "Which product should we push first to generate immediate revenue?"
* **Recommendation: Nexus Commerce & Nexus AiOS.**
  * *Commerce:* High immediate demand from Cambodian merchants (Telegram shops + PayWay/KHQR setup fees).
  * *AiOS:* Solves the #1 headache of local SME business owners (daily staff reporting). Low customer acquisition cost via Telegram.

### Q3: "Why keep Vertex Partners under a different brand name instead of Nexus?"
* **Strategic Rationale:** Vertex Partners represents **Singapore-based C-Suite executive search and institutional HR consulting** for large corporations (DBS, Singtel, CapitaLand). Keeping Vertex as an executive advisory arm preserves high-end corporate trust, while Nexus serves as the cutting-edge tech, AI, and SaaS engine.

---

## 3. WHAT THE DEVELOPERS NEED TO DO ON MONDAY MORNING

1. **Task 1 (15 mins):** Drop `<script src="nexus-global-bar.js" defer></script>` into all 9 site templates.
2. **Task 2 (30 mins):** Add CNAME records in Cloudflare for `aios`, `crm`, and `affiliates` pointing to `cname.vercel-dns.com`.
3. **Task 3 (1 hour):** Import `nexus-tokens.css` to standardize the brand colors across Next.js and Tailwind repos.

