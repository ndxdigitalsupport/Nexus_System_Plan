/**
 * NEXUS ECOSYSTEM — GLOBAL UNIVERSAL HEADER
 * Drop this single script tag into any of the 9 web properties:
 * <script src="nexus-global-bar.js" defer></script>
 * Automatically injects the unified ecosystem navigation bar.
 */

(function() {
  if (document.getElementById('nexus-global-bar-container')) return;

  const style = document.createElement('style');
  style.textContent = `
    #nexus-global-bar-container {
      position: relative;
      z-index: 999999;
      width: 100%;
      background: #0B0B10;
      border-bottom: 1px solid #1E1E28;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
      font-size: 12px;
      color: #9494A8;
      box-sizing: border-box;
    }
    .nexus-bar-inner {
      max-width: 1300px;
      margin: 0 auto;
      padding: 6px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
    }
    .nexus-bar-left {
      display: flex;
      align-items: center;
      gap: 14px;
      overflow-x: auto;
      white-space: nowrap;
      scrollbar-width: none;
    }
    .nexus-bar-left::-webkit-scrollbar {
      display: none;
    }
    .nexus-bar-brand {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-weight: 700;
      color: #FFFFFF;
      text-decoration: none;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      font-size: 11px;
    }
    .nexus-bar-brand-badge {
      background: #7C5CFC;
      color: #fff;
      padding: 1px 6px;
      border-radius: 4px;
      font-size: 10px;
    }
    .nexus-bar-divider {
      color: #2E2E3E;
    }
    .nexus-bar-links {
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .nexus-bar-link {
      color: #8E8EA0;
      text-decoration: none;
      transition: color 0.2s ease;
      font-weight: 500;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }
    .nexus-bar-link:hover {
      color: #FFFFFF;
    }
    .nexus-bar-link.active {
      color: #7C5CFC;
      font-weight: 700;
    }
    .nexus-bar-right {
      display: flex;
      align-items: center;
      gap: 12px;
      white-space: nowrap;
    }
    .nexus-bar-bot-btn {
      background: rgba(124, 92, 252, 0.15);
      border: 1px solid rgba(124, 92, 252, 0.35);
      color: #A78BFA;
      padding: 3px 10px;
      border-radius: 12px;
      text-decoration: none;
      font-weight: 600;
      font-size: 11px;
      transition: all 0.2s ease;
    }
    .nexus-bar-bot-btn:hover {
      background: #7C5CFC;
      color: #FFFFFF;
    }
  `;
  document.head.appendChild(style);

  const currentHost = window.location.hostname;

  const properties = [
    { name: 'AiOS', url: 'https://nexus-aios-ashy.vercel.app/', host: 'nexus-aios-ashy.vercel.app' },
    { name: 'CRM', url: 'https://nexus-crm-liard.vercel.app/', host: 'nexus-crm-liard.vercel.app' },
    { name: 'Commerce', url: 'https://nexuscommerce.asia/', host: 'nexuscommerce.asia' },
    { name: 'Finance', url: 'https://nexusfinance.asia/', host: 'nexusfinance.asia' },
    { name: 'Affiliates', url: 'https://nexus-digital-affiliates.vercel.app/join.html', host: 'nexus-digital-affiliates.vercel.app' },
    { name: 'Careers', url: 'https://talentlycareers.site/', host: 'talentlycareers.site' },
    { name: 'Digital Agency', url: 'https://nexusintelligence-agency.vercel.app/', host: 'nexusintelligence-agency.vercel.app' },
    { name: 'AI Advisory', url: 'https://www.nexusaipro.site/', host: 'nexusaipro.site' },
    { name: 'Vertex Partners', url: 'https://vertexpartners.asia/', host: 'vertexpartners.asia' }
  ];

  const linksHtml = properties.map(p => {
    const isActive = currentHost.includes(p.host);
    return `<a href="${p.url}" class="nexus-bar-link ${isActive ? 'active' : ''}" target="_blank">${p.name}</a>`;
  }).join('');

  const bar = document.createElement('div');
  bar.id = 'nexus-global-bar-container';
  bar.innerHTML = `
    <div class="nexus-bar-inner">
      <div class="nexus-bar-left">
        <a href="https://nexusintelligence-agency.vercel.app/" class="nexus-bar-brand" target="_blank">
          <span class="nexus-bar-brand-badge">⬡</span>
          <span>NEXUS ECOSYSTEM</span>
        </a>
        <span class="nexus-bar-divider">|</span>
        <div class="nexus-bar-links">
          ${linksHtml}
        </div>
      </div>
      <div class="nexus-bar-right">
        <a href="https://t.me/DanLP18" target="_blank" class="nexus-bar-bot-btn">💬 Nexus Support</a>
      </div>
    </div>
  `;

  document.body.insertAdjacentElement('afterbegin', bar);
})();

