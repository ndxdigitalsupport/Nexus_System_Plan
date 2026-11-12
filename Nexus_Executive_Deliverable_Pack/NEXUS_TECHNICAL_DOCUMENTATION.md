# NEXUS ECOSYSTEM — COMPLETE TECHNICAL SYSTEM SPECIFICATION & ARCHITECTURE
**Document Generated via:** DocGen Engine (`.agent/skills/docgen`)  
**Version:** 1.0.0 (Production Release)  
**Classification:** Internal Engineering & Operations  
**Framework:** Diátaxis Compliant (Tutorials, How-To Guides, Reference, Explanation)

---

## 1. EXPLANATION: SYSTEM ARCHITECTURE & TOPOLOGY

The Nexus Ecosystem operates on a distributed multi-tenant architecture designed for low-latency delivery across Southeast Asia (Cambodia focus) and APAC. It bridges Web3/FinTech rails (Bakong KHQR, ABA PayWay), conversational interfaces (Telegram Bots & Mini-Apps), and modern web SaaS applications.

### 1.1 High-Level Architecture Diagram (C4 Component Model)

```mermaid
flowchart TD
    subgraph Clients["Client Access Layers"]
        Browser["Desktop & Mobile Web Browsers"]
        TgUser["Telegram Client / Mini Apps"]
        Partner["Affiliate / API Clients"]
    end

    subgraph Edge["Edge & Ingress Layer (Cloudflare / Vercel Edge)"]
        ApexDNS["Nexus Global DNS (*.nexus.asia)"]
        GlobalBar["Global Ecosystem Header (nexus-global-bar.js)"]
    end

    subgraph Apps["Application Layer (Next.js & Modern Web)"]
        AiOS["Nexus AiOS<br/>(aios.nexus.asia)"]
        CRM["Nexus Pro CRM<br/>(crm.nexus.asia)"]
        Ecom["Nexus Commerce<br/>(nexuscommerce.asia)"]
        Fin["Nexus Finance<br/>(nexusfinance.asia)"]
        Aff["Nexus Affiliate<br/>(affiliates.nexus.asia)"]
        Tal["Talently Careers<br/>(talentlycareers.site)"]
        Agency["Nexus Digital<br/>(nexusintelligence.asia)"]
        AIPro["Nexus AI Consulting<br/>(nexusaipro.site)"]
        Vertex["Vertex Partners<br/>(vertexpartners.asia)"]
    end

    subgraph TelegramLayer["Telegram Bot & Webhook Fabric"]
        BotAiOS["AiOS Engine Bot"]
        BotCRM["@nexuscrm_official_bot"]
        BotSupport["@ndxdigital_support"]
        BotAff["@nexusdigital_affiliates_bot"]
        BotTalent["@talently_job_alerts_bot"]
        DirectChat["@DanLP18 Executive Chat"]
    end

    subgraph PaymentLayer["Financial & Settlement Rails"]
        PayWay["ABA PayWay Gateway"]
        KHQR["NBC Bakong KHQR (USD / KHR)"]
    end

    Clients --> Edge
    Edge --> Apps
    Apps <--> TelegramLayer
    Apps <--> PaymentLayer
```

---

## 2. REFERENCE: SERVICE SPECIFICATIONS & ROUTE DIRECTORY

### 2.1 Digital Products Matrix

| Product Name | Current Live URL | Target Production URL | Framework | Primary Authentication | External Integrations |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Nexus AiOS** | `nexus-aios-ashy.vercel.app` | `aios.nexus.asia` | Next.js 14, Tailwind | Credentials, `/login`, `/signup` | Telegram Bot API, OpenAI/Claude |
| **Nexus Pro CRM** | `nexus-crm-liard.vercel.app` | `crm.nexus.asia` | Next.js 14, Tailwind | `/portal` (Clients), `/dashboard/login` | `@nexuscrm_official_bot`, KHQR |
| **Nexus Commerce** | `nexuscommerce.asia` | `nexuscommerce.asia` | HTML5, Tailwind | Merchant Web App (`app.nexuscommerce.asia`) | ABA PayWay, KHQR, `@ndxdigital_support` |
| **Nexus Finance** | `nexusfinance.asia` | `nexusfinance.asia` | HTML5, Custom CSS | Pre-launch Waitlist Form | PayWay, KHQR, Bakong Open API |
| **Nexus Affiliate** | `nexus-digital-affiliates...` | `affiliates.nexus.asia` | HTML5, Material UI | `index.html` (Partner Sign-in) | `@nexusdigital_affiliates_bot`, ABA Cashout |
| **Talently Careers** | `talentlycareers.site` | `talentlycareers.site` | HTML5, Material Icons | `login.html`, `candidate.html`, `employer.html` | `@talently_job_alerts_bot`, Resume Parser |

### 2.2 Professional Services Matrix

| Service Name | Current Live URL | Target Production URL | Framework | Conversion Model | Contact Channel |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Nexus Digital (Agency)** | `nexusintelligence-agency...` | `nexusintelligence.asia` | Next.js 14, Tailwind | Direct Project Intake | `@DanLP18` (Direct Executive Telegram) |
| **Nexus AI Consulting** | `www.nexusaipro.site` | `nexusaipro.site` | Tailwind, React | Interactive Trial (`app.html`) | Web Demo / Consultation Form |
| **Vertex Partners** | `vertexpartners.asia` | `vertexpartners.asia` | WordPress, Tailwind | Executive Consultation Booking | Corporate Contact Forms & Email |

---

## 3. HOW-TO GUIDES: IMPLEMENTATION & RUNBOOKS

### 3.1 How-To: Deploy the Universal Ecosystem Navigation Bar
To resolve the "island" problem and link all 9 properties with zero backend refactoring:

1. Copy [`nexus-global-bar.js`](file:///c:/Users/Asus/Desktop/Help%202/nexus-global-bar.js) into your project's `public/` directory or host it on a CDN.
2. In your HTML `<head>` or before the closing `</body>` tag, add:
   ```html
   <script src="https://cdn.nexus.asia/nexus-global-bar.js" defer></script>
   ```
3. For Next.js (`layout.tsx` or `_app.tsx`):
   ```tsx
   import Script from 'next/script';

   export default function RootLayout({ children }: { children: React.ReactNode }) {
     return (
       <html lang="en">
         <body>
           <Script src="/nexus-global-bar.js" strategy="beforeInteractive" />
           {children}
         </body>
       </html>
     );
   }
   ```
4. The bar automatically detects the active domain and highlights the active service in `#7C5CFC` purple.

---

### 3.2 How-To: Configure Custom Apex Domains on Vercel & Cloudflare
For the 4 properties running on `*.vercel.app` (AiOS, CRM, Affiliate, Agency):

1. **In Cloudflare / DNS Provider:**
   * Add CNAME Record:
     ```
     Type: CNAME
     Name: aios
     Target: cname.vercel-dns.com
     Proxy Status: Proxied (or DNS Only)
     ```
   * Repeat for `crm`, `affiliates`, and `agency` (or root `nexusintelligence.asia`).
2. **In Vercel Project Dashboard:**
   * Navigate to: **Project Settings** → **Domains**.
   * Add `aios.nexus.asia`.
   * Vercel will verify the DNS record and automatically provision a Let's Encrypt SSL certificate within 60 seconds.

---

### 3.3 How-To: Handle Dual-Currency Bakong KHQR Payments (USD / KHR)
Both Nexus Commerce and Nexus CRM process payments via the National Bank of Cambodia (NBC) KHQR standard:

```mermaid
sequenceDiagram
    autonumber
    actor Customer as Customer / Client
    participant App as Nexus Platform (Commerce/CRM)
    participant Engine as KHQR Generation Engine
    participant Bakong as NBC Bakong / ABA Bank

    Customer->>App: Initiates Checkout / Invoicing
    App->>Engine: Request KHQR Payload (Amount, Currency: USD/KHR, BillNumber)
    Engine->>Engine: Generate EMVCo Compliant String (CRC16 Checksum)
    Engine-->>App: Return KHQR QR Image & Deep Link
    App-->>Customer: Display Dynamic QR Code
    Customer->>Bakong: Scan & Pay via Mobile Banking App
    Bakong->>App: Instant Payment Notification (IPN Webhook)
    App->>App: Mark Invoice / Order as "PAID"
    App-->>Customer: Payment Confirmation Notification
```

---

## 4. REFERENCE: ENVIRONMENT VARIABLES & SECRET MANIFEST

Maintain this master template across projects:

```ini
# ==============================================================================
# NEXUS ECOSYSTEM — ENVIRONMENT SPECIFICATION
# ==============================================================================

# Core App Settings
NODE_ENV=production
NEXT_PUBLIC_APP_ENV=production
NEXT_PUBLIC_ECOSYSTEM_DOMAIN="nexus.asia"

# Telegram Bot API Tokens
TELEGRAM_BOT_TOKEN="bot123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ"
TELEGRAM_WEBHOOK_SECRET="super-secret-webhook-key-here"
NEXT_PUBLIC_TELEGRAM_SUPPORT_HANDLE="@ndxdigital_support"

# NBC Bakong KHQR & PayWay Integration
ABA_PAYWAY_MERCHANT_ID="ecXXXXXX"
ABA_PAYWAY_API_KEY="your-aba-payway-api-key"
ABA_PAYWAY_API_URL="https://checkout.ababank.com/api/payment-gateway/v1"
BAKONG_MERCHANT_ID="merchant@devb"
BAKONG_ACQUIRING_BANK="ABA"

# Single Sign-On & JWT Tokens
NEXUS_SSO_JWT_SECRET="your-jwt-secret-min-32-chars"
NEXTAUTH_SECRET="your-nextauth-secret-key"
NEXTAUTH_URL="https://crm.nexus.asia"

# Database & KV Store (Supabase / Postgres / Redis)
DATABASE_URL="postgresql://postgres:password@db.supabase.co:5432/postgres"
REDIS_URL="rediss://default:token@upstash.io:6379"
```

---

## 5. TUTORIAL: DEVELOPER ONBOARDING (QUICKSTART)

### Step 1: Clone and Install Shared Design System
```bash
# Clone the repository
git clone https://github.com/nexus-holdings/nexus-ecosystem.git
cd nexus-ecosystem

# Link standardized design tokens
cp c:/Users/Asus/Desktop/Help\ 2/nexus-tokens.css ./styles/nexus-tokens.css
```

### Step 2: Test Ecosystem Integration Locally
Verify that `nexus-global-bar.js` loads properly and that local routes respond to the shared token variables:
```bash
npm install
npm run dev
# Open http://localhost:3000 to verify the top bar renders cleanly.
```

---
*Generated by Antigravity DocGen Skill. Validated for production deployment.*

