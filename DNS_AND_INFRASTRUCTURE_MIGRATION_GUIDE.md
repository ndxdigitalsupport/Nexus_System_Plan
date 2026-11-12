# NEXUS ECOSYSTEM — DNS & APEX DOMAIN MIGRATION RUNBOOK
**Target:** DevOps, Infrastructure Engineers & Oum Naro  
**Objective:** Migrate 4 temporary `*.vercel.app` deployments to authoritative `*.nexus.asia` apex domains  
**DNS Provider Recommended:** Cloudflare (with DNS Proxy / CNAME Flattening)

---

## 1. TARGET DOMAIN ARCHITECTURE MAP

```
Primary Apex Domain: nexus.asia (or nexusgroup.asia)
DNS Management: Cloudflare Nameservers (e.g., alex.ns.cloudflare.com)
SSL/TLS Mode: Full (Strict) — Automatic Let's Encrypt Provisioning
```

| Subdomain / URL | Target Service | Current Origin URL | DNS Record Type | Target Value | Proxy Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`aios.nexus.asia`** | Nexus AiOS | `nexus-aios-ashy.vercel.app` | `CNAME` | `cname.vercel-dns.com` | DNS Only (Grey Cloud) during cert generation, then Proxied |
| **`crm.nexus.asia`** | Nexus Pro CRM | `nexus-crm-liard.vercel.app` | `CNAME` | `cname.vercel-dns.com` | DNS Only / Proxied |
| **`affiliates.nexus.asia`**| Nexus Affiliate | `nexus-digital-affiliates...` | `CNAME` | `cname.vercel-dns.com` | DNS Only / Proxied |
| **`nexusintelligence.asia`**| Nexus Digital Agency | `nexusintelligence-agency...` | `CNAME` / `A` | `76.76.21.21` (Apex) & `cname.vercel-dns.com` (www) | Proxied (Orange Cloud) |

---

## 2. STEP-BY-STEP EXECUTION PROTOCOL

### Step 1: Add Custom Domain in Vercel Dashboard
For each project (`AiOS`, `CRM`, `Affiliates`, `Nexus Digital`):
1. Log in to **[vercel.com](https://vercel.com/)** and select the respective project.
2. Navigate to: **Settings** → **Domains**.
3. Type the target domain (e.g., `aios.nexus.asia`) and click **Add**.
4. Vercel will prompt you with the required DNS record (typically `cname.vercel-dns.com`).

---

### Step 2: Configure Records in Cloudflare / DNS Manager
1. Log in to your Cloudflare dashboard for `nexus.asia`.
2. Go to **DNS** → **Records** → **Add Record**.
3. Enter the following records:

```dns
; ==============================================================================
; CLOUDFLARE DNS CONFIGURATION (BIND FORMAT)
; ==============================================================================

; Nexus AiOS
aios            300    IN    CNAME    cname.vercel-dns.com.

; Nexus Pro CRM
crm             300    IN    CNAME    cname.vercel-dns.com.

; Nexus Affiliate Partner Network
affiliates      300    IN    CNAME    cname.vercel-dns.com.

; Nexus Digital Intelligence Flagship Agency (Root Apex Domain)
@               300    IN    A        76.76.21.21
www             300    IN    CNAME    cname.vercel-dns.com.
```

---

### Step 3: SSL Verification & 301 Redirect Enactment
1. Once Cloudflare propagates (typically 2 to 5 minutes), Vercel will display a **Valid Configuration** green checkmark.
2. In Vercel Project Settings, enable **"Redirect from *.vercel.app to custom domain"**.
3. Any visitors navigating to `nexus-aios-ashy.vercel.app` will be automatically 301 permanently redirected to `aios.nexus.asia`, preserving SEO backlink authority and existing links.

---

## 3. VERIFICATION & HEALTH CHECK SCRIPT

Run this quick test in your terminal to verify DNS propagation and HTTP response:

```bash
# Test DNS CNAME resolution
nslookup aios.nexus.asia

# Test HTTP 301 redirect from old Vercel URL
curl -I https://nexus-aios-ashy.vercel.app

# Test HTTP 200 on new apex domain
curl -I https://aios.nexus.asia
```

