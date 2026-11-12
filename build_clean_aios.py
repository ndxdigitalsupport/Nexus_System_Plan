# -*- coding: utf-8 -*-
import os

html_code = """<!DOCTYPE html>
<html lang="en" data-type="software">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="page-type" content="software">
  <meta name="site-kind" content="software">
  <title>Nexus AiOS — The Autonomous Operating System for High-Growth Founders</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../nexus-tokens.css">
  <style>
    :root {
      --bg: #040209;
      --surface: #090614;
      --card: #0D0A1C;
      --card-inner: #130F26;
      --card-border: rgba(124, 92, 252, 0.22);
      --card-border-subtle: rgba(255, 255, 255, 0.07);
      --card-hover: rgba(124, 92, 252, 0.45);
      
      --text-main: #FFFFFF;
      --text-sub: #9E9EBA;
      --text-muted: #646482;

      --violet: #7C5CFC;
      --violet-light: #A78BFA;
      --violet-bright: #C4B5FD;
      --violet-glow: rgba(124, 92, 252, 0.35);
      --cobalt: #2B3BFF;
      --emerald: #10B981;
      --emerald-light: #6EE7B7;
      --amber: #F59E0B;

      --font-display: 'Plus Jakarta Sans', sans-serif;
      --font-body: 'Inter', sans-serif;
      --font-mono: 'Space Grotesk', monospace;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }

    body {
      background-color: var(--bg);
      color: var(--text-main);
      font-family: var(--font-body);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
      background-image: 
        radial-gradient(circle at 80% 5%, rgba(124, 92, 252, 0.18) 0%, transparent 50%),
        radial-gradient(circle at 15% 45%, rgba(43, 59, 255, 0.12) 0%, transparent 45%),
        radial-gradient(circle at 80% 80%, rgba(124, 92, 252, 0.14) 0%, transparent 55%);
      background-attachment: fixed;
    }

    /* GLOBAL ECOSYSTEM BAR */
    .nexus-global-bar {
      background: rgba(4, 2, 9, 0.96);
      backdrop-filter: blur(20px);
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding: 7px 36px;
      font-size: 11px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      color: var(--text-sub);
      position: sticky;
      top: 0;
      z-index: 1000;
      font-family: var(--font-display);
    }
    .nexus-global-bar a { color: var(--text-sub); text-decoration: none; margin-left: 16px; transition: color 0.2s; font-weight: 500; }
    .nexus-global-bar a:hover, .nexus-global-bar a.active { color: #fff; font-weight: 700; }
    .nexus-global-bar a.active { color: var(--violet-light); }

    /* NAVBAR */
    .navbar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 14px 48px;
      background: rgba(4, 2, 9, 0.88);
      backdrop-filter: blur(24px);
      border-bottom: 1px solid var(--card-border-subtle);
      position: sticky;
      top: 31px;
      z-index: 999;
    }
    .brand-group {
      display: flex;
      align-items: center;
      gap: 12px;
      font-family: var(--font-display);
      font-weight: 800;
      font-size: 1.25rem;
      letter-spacing: -0.03em;
      color: #fff;
      text-decoration: none;
    }
    .brand-icon {
      width: 34px;
      height: 34px;
      background: linear-gradient(135deg, var(--violet), var(--cobalt));
      border-radius: 9px;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 14px var(--violet-glow);
    }
    .brand-icon svg { width: 19px; height: 19px; fill: none; stroke: #fff; stroke-width: 2.2; }

    .nav-links { display: flex; align-items: center; gap: 28px; font-size: 0.88rem; font-weight: 600; }
    .nav-links a { color: var(--text-sub); text-decoration: none; transition: color 0.2s ease; }
    .nav-links a:hover { color: #fff; }

    .nav-actions { display: flex; align-items: center; gap: 14px; }
    .btn-login {
      color: #fff; text-decoration: none; font-size: 0.85rem; font-weight: 600;
      padding: 8px 16px; border-radius: 8px; transition: color 0.2s;
    }
    .btn-cta {
      background: linear-gradient(135deg, var(--violet), #6946FA);
      color: #fff;
      padding: 9px 22px;
      border-radius: 9999px;
      font-weight: 700;
      font-size: 0.85rem;
      text-decoration: none;
      box-shadow: 0 4px 18px var(--violet-glow);
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }
    .btn-cta:hover { transform: translateY(-1px); box-shadow: 0 6px 24px rgba(124, 92, 252, 0.55); }
    .btn-cta:active, .btn-login:active, button:active, .f-pill:active { transform: scale(0.975); }

    .container {
      max-width: 1260px;
      margin: 0 auto;
      padding: 0 32px;
    }

    /* =========================================================================
       SCREEN 1: FOUNDER COMMAND HERO (STRICT 100SVH)
       ========================================================================= */
    .hero-screen {
      min-height: calc(100svh - 105px);
      display: flex;
      align-items: center;
      padding: 32px 0;
      position: relative;
    }
    .hero-split-grid {
      display: grid;
      grid-template-columns: 5.2fr 5.8fr;
      gap: 48px;
      align-items: center;
      width: 100%;
    }

    .hero-pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(124, 92, 252, 0.12);
      border: 1px solid rgba(124, 92, 252, 0.32);
      padding: 6px 16px;
      border-radius: 9999px;
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--violet-light);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 20px;
    }
    .hero-pill .dot {
      width: 6px; height: 6px; border-radius: 50%;
      background: var(--emerald);
      box-shadow: 0 0 10px var(--emerald);
    }
    .hero-headline {
      font-family: var(--font-display);
      font-size: clamp(2.4rem, 3.8vw, 3.5rem);
      font-weight: 800;
      letter-spacing: -0.04em;
      line-height: 1.12;
      margin-bottom: 20px;
      text-wrap: balance;
      background: linear-gradient(180deg, #FFFFFF 30%, #A9A9C8 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .hero-headline span {
      background: linear-gradient(135deg, #C4B5FD 0%, #7C5CFC 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .hero-sub {
      font-size: 1.05rem;
      color: var(--text-sub);
      line-height: 1.6;
      margin-bottom: 28px;
      max-width: 50ch;
      text-wrap: pretty;
    }
    .hero-actions {
      display: flex;
      gap: 14px;
      margin-bottom: 28px;
      align-items: center;
      flex-wrap: wrap;
    }
    .hero-trust-row {
      display: flex;
      gap: 20px;
      font-size: 0.78rem;
      color: var(--text-muted);
      border-top: 1px solid var(--card-border-subtle);
      padding-top: 18px;
      font-variant-numeric: tabular-nums;
      flex-wrap: wrap;
    }
    .trust-pill { display: flex; align-items: center; gap: 6px; }

    /* FOUNDER BRIEFING CONSOLE (TACTILE STAGE WITH CONCENTRIC RADII) */
    .console-wrapper {
      position: relative;
    }
    .console-glow-underlay {
      position: absolute;
      inset: -20px;
      background: radial-gradient(circle at 60% 40%, rgba(124, 92, 252, 0.25) 0%, transparent 70%);
      filter: blur(30px);
      z-index: 0;
      pointer-events: none;
    }
    .hero-product-stage {
      position: relative;
      z-index: 1;
      background: var(--card);
      border: 1px solid var(--card-border);
      border-radius: 20px;
      padding: 22px;
      box-shadow: 0 25px 60px -15px rgba(0,0,0,0.85), 0 0 35px -5px rgba(124, 92, 252, 0.2);
    }
    .stage-chrome {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--card-border-subtle);
      padding-bottom: 12px;
      margin-bottom: 16px;
    }
    .traffic-lights {
      display: flex;
      gap: 6px;
      align-items: center;
    }
    .traffic-dot {
      width: 10px; height: 10px; border-radius: 50%;
    }
    .dot-red { background: #FF5F56; }
    .dot-yellow { background: #FFBD2E; }
    .dot-green { background: #27C93F; }

    .stage-title {
      font-size: 0.8rem;
      font-weight: 700;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 8px;
      letter-spacing: 0.02em;
    }
    .status-chip {
      font-family: var(--font-mono);
      font-size: 0.7rem;
      color: var(--violet-bright);
      background: rgba(124, 92, 252, 0.14);
      border: 1px solid rgba(124, 92, 252, 0.3);
      padding: 2px 8px;
      border-radius: 6px;
      font-weight: 700;
      font-variant-numeric: tabular-nums;
    }

    /* AUDIO DIGEST PLAYER (CONCENTRIC RADIUS 12PX = 20PX - 8PX) */
    .digest-player {
      background: var(--card-inner);
      border: 1px solid var(--card-border-subtle);
      border-radius: 12px;
      padding: 14px 16px;
      margin-bottom: 14px;
    }
    .player-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
      font-size: 0.74rem;
    }
    .waveform-wrap {
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .play-btn {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--violet), #6946FA);
      border: none;
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 4px 14px var(--violet-glow);
      transition: transform 0.15s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.15s;
      flex-shrink: 0;
    }
    .play-btn:hover {
      transform: scale(1.05);
      box-shadow: 0 6px 20px rgba(124, 92, 252, 0.6);
    }
    .play-btn:active { transform: scale(0.95); }

    .waveform-bars {
      display: flex;
      align-items: center;
      gap: 3px;
      height: 28px;
      flex: 1;
    }
    .wf-bar {
      width: 3px;
      background: var(--violet-light);
      border-radius: 3px;
      animation: pulseWave 1.2s ease-in-out infinite alternate;
      animation-play-state: paused;
    }
    @keyframes pulseWave {
      0% { height: 4px; opacity: 0.3; }
      100% { height: 26px; opacity: 1; }
    }

    .digest-time {
      font-family: var(--font-mono);
      font-size: 0.75rem;
      color: var(--text-sub);
      font-variant-numeric: tabular-nums;
      flex-shrink: 0;
    }
    .speed-pills {
      display: flex;
      gap: 4px;
      background: rgba(0,0,0,0.3);
      padding: 3px;
      border-radius: 6px;
      border: 1px solid var(--card-border-subtle);
    }
    .s-pill {
      font-family: var(--font-mono);
      font-size: 0.68rem;
      padding: 2px 6px;
      border-radius: 4px;
      background: transparent;
      border: none;
      color: var(--text-muted);
      cursor: pointer;
      font-weight: 700;
    }
    .s-pill.active { background: var(--violet); color: #fff; }

    /* TELEGRAM LIVE FEED */
    .tg-stream-box {
      background: var(--card-inner);
      border: 1px solid var(--card-border-subtle);
      border-radius: 12px;
      padding: 12px;
    }
    .feed-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .stream-item {
      padding: 8px 10px;
      border-radius: 8px;
      margin-bottom: 6px;
      background: rgba(0,0,0,0.25);
      border: 1px solid transparent;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .stream-item:last-child { margin-bottom: 0; }
    .stream-item:hover {
      background: rgba(124, 92, 252, 0.08);
      border-color: rgba(124, 92, 252, 0.25);
    }
    .stream-row {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .stream-avatar {
      width: 26px; height: 26px; border-radius: 50%;
      background: linear-gradient(135deg, var(--violet), var(--cobalt));
      color: #fff; font-weight: 700; font-size: 10px;
      display: flex; align-items: center; justify-content: center;
      flex-shrink: 0;
    }
    .stream-meta {
      flex: 1;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .stream-time {
      font-family: var(--font-mono);
      font-size: 0.68rem;
      color: var(--text-muted);
      font-variant-numeric: tabular-nums;
    }
    .stream-body {
      font-size: 0.76rem;
      color: var(--text-sub);
      margin-top: 3px;
    }
    .stream-detail-drawer {
      display: none;
      margin-top: 8px;
      padding: 8px 10px;
      background: rgba(0,0,0,0.5);
      border-left: 2px solid var(--violet);
      border-radius: 4px;
      font-size: 0.72rem;
      color: var(--violet-bright);
    }
    .stream-item.expanded .stream-detail-drawer {
      display: block;
    }

    /* =========================================================================
       SCREEN 2: ULTRA-CLEAN AUTONOMOUS ARCHITECTURE BENTO GRID (#bento)
       ========================================================================= */
    .bento-section {
      min-height: 100svh;
      padding: 80px 0 60px;
      border-top: 1px solid var(--card-border-subtle);
      scroll-margin-top: 80px;
    }
    .section-tag {
      font-size: 0.75rem;
      font-weight: 800;
      color: var(--violet-light);
      text-transform: uppercase;
      letter-spacing: 0.12em;
      margin-bottom: 8px;
    }
    .section-title {
      font-family: var(--font-display);
      font-size: clamp(2rem, 3.2vw, 2.7rem);
      font-weight: 800;
      letter-spacing: -0.03em;
      margin-bottom: 10px;
      text-wrap: balance;
    }
    .section-lead {
      color: var(--text-sub);
      font-size: 1.05rem;
      max-width: 50ch;
      margin-bottom: 32px;
      text-wrap: pretty;
    }

    .bento-grid {
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      gap: 18px;
    }
    .bento-card {
      background: var(--card);
      border: 1px solid var(--card-border-subtle);
      border-radius: 20px;
      padding: 22px;
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .bento-card:hover {
      border-color: var(--card-hover);
      box-shadow: 0 16px 36px -10px rgba(0,0,0,0.8), 0 0 25px -5px rgba(124, 92, 252, 0.2);
      transform: translateY(-2px);
    }
    .bento-card:active { transform: scale(0.985); }
    .col-7 { grid-column: span 7; }
    .col-5 { grid-column: span 5; }
    .col-4 { grid-column: span 4; }
    .col-12 { grid-column: span 12; }

    .bento-badge-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }
    .micro-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 0.7rem;
      font-weight: 700;
      color: var(--text-sub);
      text-transform: uppercase;
      letter-spacing: 0.06em;
    }
    .badge-dot {
      width: 6px; height: 6px; border-radius: 50%;
    }
    .badge-metric {
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--emerald);
      font-variant-numeric: tabular-nums;
    }
    .bento-card-title {
      font-size: 1.25rem;
      font-weight: 800;
      margin-bottom: 6px;
      letter-spacing: -0.02em;
      color: #FFFFFF;
    }
    .bento-card-sub {
      color: var(--text-sub);
      font-size: 0.86rem;
      line-height: 1.45;
      margin-bottom: 16px;
    }

    /* CARD 1: MINI TELEGRAM CHAT WIDGET */
    .tg-mini-chat {
      background: #17212B;
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 12px;
      padding: 12px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .tg-msg {
      display: flex;
      gap: 8px;
      align-items: flex-end;
    }
    .tg-msg.user-msg {
      justify-content: flex-end;
    }
    .tg-msg-avatar {
      width: 24px;
      height: 24px;
      border-radius: 50%;
      background: #2AABEE;
      color: #fff;
      font-size: 9px;
      font-weight: 800;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .tg-msg-bubble {
      background: #242F3D;
      border-radius: 10px 10px 10px 2px;
      padding: 8px 12px;
      font-size: 0.78rem;
      max-width: 82%;
    }
    .user-bubble {
      background: #2B5278;
      border-radius: 10px 10px 2px 10px;
      color: #fff;
    }
    .tg-sender {
      color: #64B5F6;
      font-size: 0.68rem;
      font-weight: 700;
      margin-bottom: 2px;
    }
    .tg-time {
      font-size: 0.65rem;
      color: #94A3B8;
      text-align: right;
      margin-top: 3px;
      font-family: var(--font-mono);
    }
    .checks { color: #64B5F6; margin-left: 3px; }

    /* CARD 2: RADAR ALERT WIDGET */
    .radar-widget {
      background: var(--card-inner);
      border: 1px solid var(--card-border-subtle);
      border-radius: 12px;
      padding: 12px;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .radar-alert-pill {
      display: flex;
      align-items: center;
      gap: 10px;
      background: rgba(245, 158, 11, 0.08);
      border: 1px solid rgba(245, 158, 11, 0.25);
      border-radius: 8px;
      padding: 8px 12px;
    }
    .radar-pulse-ring {
      width: 14px;
      height: 14px;
      border-radius: 50%;
      background: rgba(245, 158, 11, 0.2);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .radar-pulse-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--amber);
      box-shadow: 0 0 8px var(--amber);
    }
    .radar-alert-info { flex: 1; }
    .radar-alert-title {
      font-size: 0.78rem;
      font-weight: 700;
      color: #FDE68A;
    }
    .radar-alert-sub {
      font-size: 0.7rem;
      color: var(--text-sub);
    }
    .radar-action-pill {
      display: flex;
      align-items: center;
      gap: 8px;
      background: rgba(16, 185, 129, 0.08);
      border: 1px solid rgba(16, 185, 129, 0.25);
      border-radius: 8px;
      padding: 8px 12px;
      font-size: 0.76rem;
      color: var(--emerald-light);
      font-weight: 600;
    }

    /* CARD 3: SYNC TELEMETRY BOX */
    .sync-telemetry-box {
      background: var(--card-inner);
      border: 1px solid var(--card-border-subtle);
      border-radius: 12px;
      padding: 12px;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .sync-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.78rem;
      padding: 4px 0;
      border-bottom: 1px solid rgba(255,255,255,0.04);
    }
    .sync-row:last-child { border-bottom: none; }
    .sync-label { color: var(--text-sub); }
    .sync-val { font-weight: 700; color: #fff; font-variant-numeric: tabular-nums; }

    /* CARD 4: DUAL CURRENCY CARD */
    .currency-card-widget {
      background: var(--card-inner);
      border: 1px solid var(--card-border-subtle);
      border-radius: 12px;
      padding: 12px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .curr-line {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .curr-tag {
      font-size: 0.7rem;
      font-weight: 700;
      color: var(--text-muted);
      font-family: var(--font-mono);
    }
    .curr-amount {
      font-family: var(--font-mono);
      font-size: 0.92rem;
      font-weight: 700;
      color: #fff;
      font-variant-numeric: tabular-nums;
    }
    .curr-status {
      font-size: 0.68rem;
      color: var(--emerald);
      display: flex;
      align-items: center;
      gap: 5px;
      margin-top: 4px;
      font-weight: 600;
    }
    .status-indicator {
      width: 5px; height: 5px; border-radius: 50%;
      background: var(--emerald);
    }

    /* CARD 5: MINI AUDIO CARD */
    .audio-mini-card {
      background: var(--card-inner);
      border: 1px solid var(--card-border-subtle);
      border-radius: 12px;
      padding: 12px 14px;
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .mini-play-circle {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--violet), var(--cobalt));
      display: flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      flex-shrink: 0;
      box-shadow: 0 2px 10px var(--violet-glow);
    }
    .mini-wave-bars {
      display: flex;
      align-items: center;
      gap: 3px;
      flex: 1;
      height: 24px;
    }
    .m-bar {
      width: 3px;
      background: var(--violet-light);
      border-radius: 2px;
    }
    .mini-duration {
      font-family: var(--font-mono);
      font-size: 0.74rem;
      color: var(--text-sub);
      font-variant-numeric: tabular-nums;
    }

    /* CARD 6: CLEAN PIPELINE STRIP */
    .clean-pipeline-strip {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
      background: var(--card-inner);
      border: 1px solid var(--card-border-subtle);
      border-radius: 12px;
      padding: 14px;
    }
    .pipeline-step {
      display: flex;
      flex-direction: column;
      gap: 2px;
    }
    .step-num {
      font-family: var(--font-mono);
      font-size: 0.68rem;
      font-weight: 700;
      color: var(--violet-bright);
    }
    .step-title {
      font-size: 0.85rem;
      font-weight: 700;
      color: #fff;
    }
    .step-desc {
      font-size: 0.72rem;
      color: var(--text-sub);
    }

    /* =========================================================================
       SCREEN 3: FOUNDER ROI CALCULATOR (#roi)
       ========================================================================= */
    .roi-section {
      min-height: 100svh;
      padding: 80px 0 60px;
      border-top: 1px solid var(--card-border-subtle);
      scroll-margin-top: 80px;
    }
    .roi-card {
      background: var(--card);
      border: 1px solid var(--card-border);
      border-radius: 20px;
      padding: 36px;
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 40px;
      align-items: center;
      box-shadow: 0 25px 60px -15px rgba(0,0,0,0.85);
    }
    .slider-group { margin-bottom: 24px; }
    .slider-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.88rem;
      font-weight: 600;
      margin-bottom: 10px;
      color: var(--text-main);
    }
    .slider-val {
      font-family: var(--font-mono);
      font-weight: 700;
      color: var(--violet-light);
      background: rgba(124, 92, 252, 0.12);
      padding: 3px 10px;
      border-radius: 6px;
      font-size: 0.82rem;
    }
    input[type=range] {
      -webkit-appearance: none;
      width: 100%;
      height: 6px;
      background: rgba(255,255,255,0.08);
      border-radius: 6px;
      outline: none;
    }
    input[type=range]::-webkit-slider-thumb {
      -webkit-appearance: none;
      width: 20px;
      height: 20px;
      border-radius: 50%;
      background: var(--violet-light);
      cursor: pointer;
      box-shadow: 0 0 12px var(--violet);
      transition: transform 0.1s;
    }
    input[type=range]::-webkit-slider-thumb:hover { transform: scale(1.15); }

    .roi-display-box {
      background: var(--card-inner);
      border: 1px solid var(--card-border-subtle);
      border-radius: 14px;
      padding: 28px;
      text-align: center;
    }
    .roi-stat-main {
      font-family: var(--font-display);
      font-size: clamp(2.4rem, 4vw, 3.4rem);
      font-weight: 800;
      letter-spacing: -0.04em;
      color: #fff;
      margin: 8px 0;
      font-variant-numeric: tabular-nums;
    }
    .roi-grid-mini {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
      margin-top: 20px;
      border-top: 1px solid rgba(255,255,255,0.06);
      padding-top: 16px;
    }
    .roi-mini-num {
      font-family: var(--font-mono);
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--emerald);
      font-variant-numeric: tabular-nums;
    }

    /* =========================================================================
       SCREEN 4: TRANSPARENT 3-TIER ENTERPRISE PRICING (#pricing)
       ========================================================================= */
    .pricing-section {
      min-height: 100svh;
      padding: 80px 0 60px;
      border-top: 1px solid var(--card-border-subtle);
      scroll-margin-top: 80px;
    }
    .billing-toggle-row {
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 12px;
      margin-bottom: 32px;
    }
    .cycle-btn {
      background: transparent;
      border: 1px solid var(--card-border-subtle);
      color: var(--text-sub);
      padding: 7px 18px;
      border-radius: 9999px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }
    .cycle-btn.active {
      background: rgba(124, 92, 252, 0.16);
      border-color: var(--violet);
      color: #fff;
    }
    .discount-chip {
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.35);
      color: var(--emerald-light);
      font-size: 0.72rem;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 9999px;
    }

    .pricing-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
    }
    .price-card {
      background: var(--card);
      border: 1px solid var(--card-border-subtle);
      border-radius: 20px;
      padding: 28px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.25s;
    }
    .price-card.featured {
      border-color: var(--violet);
      box-shadow: 0 20px 50px -15px rgba(124, 92, 252, 0.3);
      position: relative;
    }
    .price-card:hover { transform: translateY(-3px); }
    .featured-badge {
      position: absolute;
      top: -11px;
      left: 50%;
      transform: translateX(-50%);
      background: linear-gradient(135deg, var(--violet), var(--cobalt));
      color: #fff;
      font-size: 0.68rem;
      font-weight: 800;
      padding: 3px 12px;
      border-radius: 9999px;
      letter-spacing: 0.08em;
      text-transform: uppercase;
    }
    .tier-name {
      font-family: var(--font-display);
      font-size: 1.25rem;
      font-weight: 800;
      margin-bottom: 6px;
    }
    .tier-desc {
      font-size: 0.82rem;
      color: var(--text-sub);
      margin-bottom: 18px;
      min-height: 38px;
    }
    .price-row {
      display: flex;
      align-items: baseline;
      gap: 6px;
      margin-bottom: 22px;
    }
    .price-val {
      font-family: var(--font-display);
      font-size: 2.4rem;
      font-weight: 800;
      color: #fff;
      font-variant-numeric: tabular-nums;
    }
    .price-period {
      font-size: 0.82rem;
      color: var(--text-muted);
    }
    .feature-list {
      list-style: none;
      margin-bottom: 26px;
    }
    .feature-item {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 0.82rem;
      color: var(--text-sub);
      margin-bottom: 10px;
    }
    .feature-item svg {
      width: 14px;
      height: 14px;
      stroke: var(--emerald);
      stroke-width: 2.5;
      flex-shrink: 0;
    }
    .tier-btn {
      display: block;
      width: 100%;
      text-align: center;
      padding: 10px 0;
      border-radius: 9999px;
      font-weight: 700;
      font-size: 0.84rem;
      text-decoration: none;
      transition: all 0.2s;
    }
    .btn-tier-default {
      background: rgba(255,255,255,0.06);
      color: #fff;
      border: 1px solid var(--card-border-subtle);
    }
    .btn-tier-default:hover { background: rgba(255,255,255,0.12); }
    .btn-tier-featured {
      background: linear-gradient(135deg, var(--violet), #6946FA);
      color: #fff;
      box-shadow: 0 4px 16px var(--violet-glow);
    }
    .btn-tier-featured:hover { transform: translateY(-1px); box-shadow: 0 6px 22px rgba(124, 92, 252, 0.6); }

    /* =========================================================================
       SCREEN 5: EXECUTIVE FAQ (#faq)
       ========================================================================= */
    .faq-section {
      min-height: 100svh;
      padding: 80px 0 60px;
      border-top: 1px solid var(--card-border-subtle);
      scroll-margin-top: 80px;
    }
    .faq-layout {
      display: grid;
      grid-template-columns: 4fr 8fr;
      gap: 48px;
    }
    .faq-item {
      background: var(--card);
      border: 1px solid var(--card-border-subtle);
      border-radius: 12px;
      margin-bottom: 12px;
      overflow: hidden;
      transition: border-color 0.2s;
    }
    .faq-item:hover { border-color: rgba(124, 92, 252, 0.35); }
    .faq-q {
      padding: 18px 20px;
      font-weight: 700;
      font-size: 0.95rem;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .faq-a {
      padding: 0 20px 18px;
      color: var(--text-sub);
      font-size: 0.88rem;
      line-height: 1.55;
    }

    /* FOOTER */
    footer {
      border-top: 1px solid var(--card-border-subtle);
      padding: 32px 48px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.82rem;
      color: var(--text-muted);
      background: #020105;
    }
    footer a { color: var(--text-sub); text-decoration: none; }
    footer a:hover { color: #fff; }

    @media (max-width: 1024px) {
      .hero-split-grid { grid-template-columns: 1fr; gap: 36px; }
      .bento-grid { grid-template-columns: 1fr; }
      .col-7, .col-5, .col-4, .col-12 { grid-column: span 1; }
      .roi-card { grid-template-columns: 1fr; }
      .pricing-grid { grid-template-columns: 1fr; }
      .faq-layout { grid-template-columns: 1fr; }
      .clean-pipeline-strip { grid-template-columns: 1fr 1fr; }
    }
  </style>
</head>
<body>

  <!-- 1. GLOBAL ECOSYSTEM SWITCHER -->
  <div class="nexus-global-bar">
    <div><strong>NEXUS GROUP</strong> • AUTONOMOUS AI ECOSYSTEM</div>
    <div>
      <a href="../01_aios/index.html" class="active">AiOS</a>
      <a href="../02_crm/index.html">CRM</a>
      <a href="../03_commerce/index.html">Commerce</a>
      <a href="../04_finance/index.html">Finance</a>
      <a href="../05_affiliate/index.html">Affiliates</a>
      <a href="../06_talently/index.html">Talently</a>
      <a href="../07_agency/index.html">Agency</a>
      <a href="../08_ai_consulting/index.html">Enterprise AI</a>
      <a href="../09_vertex/index.html">Vertex</a>
    </div>
  </div>

  <!-- 2. NAVBAR -->
  <header class="navbar">
    <a href="index.html" class="brand-group">
      <div class="brand-icon">
        <svg viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
      </div>
      <div>Nexus <span style="color: var(--violet-light);">AiOS</span></div>
    </a>

    <nav class="nav-links">
      <a href="#bento">Capabilities</a>
      <a href="#roi">ROI Calculator</a>
      <a href="#pricing">Pricing</a>
      <a href="#faq">FAQ</a>
      <a href="https://t.me/DanLP18" target="_blank">Book AI Audit</a>
    </nav>

    <div class="nav-actions">
      <a href="#pricing" class="btn-login">Sign In</a>
      <a href="#pricing" class="btn-cta">
        <span>Deploy in 15 Mins</span>
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
      </a>
    </div>
  </header>

  <main class="container">
    <!-- =======================================================================
         SCREEN 1: FOUNDER COMMAND HERO (100SVH)
         ======================================================================= -->
    <section class="hero-screen">
      <div class="hero-split-grid">
        <!-- Hero Text -->
        <div>
          <div class="hero-pill">
            <span class="dot"></span>
            <span>TELEGRAM-NATIVE AI OPERATING SYSTEM</span>
          </div>

          <h1 class="hero-headline">
            Stop Chasing Team Reports.<br>
            <span>Start Every Day With Clarity.</span>
          </h1>

          <p class="hero-sub">
            Staff check in via Telegram in 60 seconds. AiOS synthesizes updates into a 2-minute audio briefing delivered to your phone at 8:00 AM.
          </p>

          <div class="hero-actions">
            <a href="#pricing" class="btn-cta" style="padding: 12px 28px; font-size: 0.95rem;">
              <span>Start Free 14-Day Pilot</span>
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </a>
            <a href="https://t.me/DanLP18" target="_blank" class="cycle-btn" style="padding: 12px 22px; font-size: 0.95rem; border-color: rgba(255,255,255,0.15);">
              Live Telegram Demo
            </a>
          </div>

          <div class="hero-trust-row">
            <div class="trust-pill">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--emerald)" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg>
              <span>100% Telegram Native</span>
            </div>
            <div class="trust-pill">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--emerald)" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg>
              <span>Zero Staff App Downloads</span>
            </div>
            <div class="trust-pill">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--emerald)" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg>
              <span>AES-256 Cloud Vault</span>
            </div>
          </div>
        </div>

        <!-- Founder Briefing Console -->
        <div class="console-wrapper">
          <div class="console-glow-underlay"></div>
          <div class="hero-product-stage">
            <div class="stage-chrome">
              <div class="traffic-lights">
                <span class="traffic-dot dot-red"></span>
                <span class="traffic-dot dot-yellow"></span>
                <span class="traffic-dot dot-green"></span>
              </div>
              <div class="stage-title">
                <span style="width: 7px; height: 7px; border-radius: 50%; background: var(--emerald); display: inline-block;"></span>
                <span>Founder Briefing Console</span>
              </div>
              <span class="status-chip">08:00 AM ICT</span>
            </div>

            <!-- AUDIO DIGEST PLAYER -->
            <div class="digest-player">
              <div class="player-header">
                <span style="font-weight: 600; color: #fff;">2-Minute Executive Voice Digest</span>
                <div class="speed-pills">
                  <button class="s-pill active" onclick="setSpeed(1, this)">1.0x</button>
                  <button class="s-pill" onclick="setSpeed(1.5, this)">1.5x</button>
                  <button class="s-pill" onclick="setSpeed(2, this)">2.0x</button>
                </div>
              </div>
              <div class="waveform-wrap">
                <button class="play-btn" id="playBtn" onclick="toggleAudio()">
                  <svg id="playIcon" width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg>
                </button>
                <div class="waveform-bars">
                  <div class="wf-bar" style="animation-delay: 0.1s"></div>
                  <div class="wf-bar" style="animation-delay: 0.3s"></div>
                  <div class="wf-bar" style="animation-delay: 0.2s"></div>
                  <div class="wf-bar" style="animation-delay: 0.5s"></div>
                  <div class="wf-bar" style="animation-delay: 0.4s"></div>
                  <div class="wf-bar" style="animation-delay: 0.7s"></div>
                  <div class="wf-bar" style="animation-delay: 0.2s"></div>
                  <div class="wf-bar" style="animation-delay: 0.6s"></div>
                  <div class="wf-bar" style="animation-delay: 0.3s"></div>
                  <div class="wf-bar" style="animation-delay: 0.8s"></div>
                  <div class="wf-bar" style="animation-delay: 0.4s"></div>
                  <div class="wf-bar" style="animation-delay: 0.2s"></div>
                  <div class="wf-bar" style="animation-delay: 0.5s"></div>
                  <div class="wf-bar" style="animation-delay: 0.3s"></div>
                  <div class="wf-bar" style="animation-delay: 0.6s"></div>
                  <div class="wf-bar" style="animation-delay: 0.1s"></div>
                </div>
                <span class="digest-time" id="digestTimer">00:00 / 02:14</span>
              </div>
            </div>

            <!-- TELEGRAM LIVE FEED -->
            <div class="tg-stream-box">
              <div class="feed-header">
                <span>Automated Synthesis Feed</span>
                <span style="color: var(--emerald); font-variant-numeric: tabular-nums;">● 3 Active Streams</span>
              </div>

              <!-- Stream 1 -->
              <div class="stream-item" onclick="toggleStreamDrawer(this)">
                <div class="stream-row">
                  <div class="stream-avatar" style="background: linear-gradient(135deg, #7C5CFC, #2B3BFF);">MK</div>
                  <div class="stream-meta">
                    <span style="font-weight: 700; font-size: 0.78rem; color: #fff;">Marketing Dept Check-In</span>
                    <span class="stream-time">07:42 AM</span>
                  </div>
                </div>
                <div class="stream-body">Meta ROAS 4.1x confirmed. 120 new qualified leads synced to CRM.</div>
                <div class="stream-detail-drawer">Raw Staff Telegram Check-In: "Campaign 12 launched at 6am, CPC $0.22, 120 leads passed to sales pipeline. No spend anomalies."</div>
              </div>

              <!-- Stream 2 -->
              <div class="stream-item" onclick="toggleStreamDrawer(this)">
                <div class="stream-row">
                  <div class="stream-avatar" style="background: linear-gradient(135deg, #10B981, #059669);">OPS</div>
                  <div class="stream-meta">
                    <span style="font-weight: 700; font-size: 0.78rem; color: #fff;">Fulfillment Alert Handled</span>
                    <span class="stream-time">07:55 AM</span>
                  </div>
                </div>
                <div class="stream-body">Inventory rebalanced across Siem Reap hub. 0 delayed customer deliveries.</div>
                <div class="stream-detail-drawer">Raw Staff Telegram Check-In: "Transferred 40 SKU units from Phnom Penh central warehouse to Siem Reap hub. Out-of-stock risk cleared."</div>
              </div>

              <!-- Stream 3 -->
              <div class="stream-item" onclick="toggleStreamDrawer(this)">
                <div class="stream-row">
                  <div class="stream-avatar" style="background: linear-gradient(135deg, #F59E0B, #D97706);">FIN</div>
                  <div class="stream-meta">
                    <span style="font-weight: 700; font-size: 0.78rem; color: #fff;">Automated Reconciliation</span>
                    <span class="stream-time">08:00 AM</span>
                  </div>
                </div>
                <div class="stream-body">$42,500 settled via Bakong KHQR. 0 pending reconciliations.</div>
                <div class="stream-detail-drawer">Raw Staff Check-In: "NBC Bakong reconciliation batch 884 completed. USD/KHR balances verified against treasury ledger."</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- =======================================================================
         SCREEN 2: ULTRA-CLEAN AUTONOMOUS ARCHITECTURE BENTO GRID (#bento)
         ======================================================================= -->
    <section class="bento-section" id="bento">
      <div class="section-tag">CAPABILITIES</div>
      <h2 class="section-title">Engineered for Autonomy</h2>
      <p class="section-lead">Everything your team does in Telegram, synthesized into executive decisions.</p>

      <div class="bento-grid">
        <!-- Card 1 (col-7): Telegram Native Check-In -->
        <div class="bento-card col-7">
          <div>
            <div class="bento-badge-row">
              <span class="micro-badge"><span class="badge-dot" style="background:#2AABEE;"></span>Telegram Native</span>
              <span class="badge-metric">98.4% on-time</span>
            </div>
            <h3 class="bento-card-title">Zero App Downloads</h3>
            <p class="bento-card-sub">Staff check in inside their existing Telegram chats in under 60 seconds.</p>
          </div>

          <!-- Sleek Telegram Chat UI Component -->
          <div class="tg-mini-chat" data-ui="telegram">
            <div class="tg-msg">
              <div class="tg-msg-avatar">AI</div>
              <div class="tg-msg-bubble">
                <div class="tg-sender">Nexus Check-In Bot</div>
                <div>Morning Sothea. Today's deliverables and blockers?</div>
                <div class="tg-time">07:30 AM</div>
              </div>
            </div>
            <div class="tg-msg user-msg">
              <div class="tg-msg-bubble user-bubble">
                <div>Dispatched 40 SKUs. Reconciled Bakong batch #884. No blockers.</div>
                <div class="tg-time">07:32 AM <span class="checks">✓✓</span></div>
              </div>
            </div>
          </div>
        </div>

        <!-- Card 2 (col-5): Blocker Interceptor -->
        <div class="bento-card col-5">
          <div>
            <div class="bento-badge-row">
              <span class="micro-badge"><span class="badge-dot" style="background:var(--amber);"></span>Live Radar</span>
              <span class="badge-metric" style="color:var(--amber);">Active</span>
            </div>
            <h3 class="bento-card-title">Blocker Interception</h3>
            <p class="bento-card-sub">Flags dependency bottlenecks before they cause customer cancellations.</p>
          </div>

          <!-- Sleek Radar Warning & Auto-Fix Widget -->
          <div class="radar-widget" data-ui="radar">
            <div class="radar-alert-pill">
              <div class="radar-pulse-ring">
                <span class="radar-pulse-dot"></span>
              </div>
              <div class="radar-alert-info">
                <div class="radar-alert-title">Customs Delay Flagged</div>
                <div class="radar-alert-sub">Batch 4 delayed 24h</div>
              </div>
            </div>
            <div class="radar-action-pill">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg>
              <span>Auto-rerouted to Siem Reap hub</span>
            </div>
          </div>
        </div>

        <!-- Card 3 (col-4): Cross-Department Sync -->
        <div class="bento-card col-4">
          <div>
            <div class="bento-badge-row">
              <span class="micro-badge"><span class="badge-dot" style="background:var(--violet-light);"></span>Synthesis</span>
            </div>
            <h3 class="bento-card-title">Cross-Department Sync</h3>
            <p class="bento-card-sub">Marketing, logistics, and sales aligned in one stream.</p>
          </div>

          <div class="sync-telemetry-box" data-ui="sync">
            <div class="sync-row">
              <span class="sync-label">Marketing</span>
              <span class="sync-val" style="color:var(--emerald);">4.1x ROAS</span>
            </div>
            <div class="sync-row">
              <span class="sync-label">Fulfillment</span>
              <span class="sync-val">0 delayed</span>
            </div>
            <div class="sync-row">
              <span class="sync-label">Sales</span>
              <span class="sync-val">120 leads synced</span>
            </div>
          </div>
        </div>

        <!-- Card 4 (col-4): Bakong Dual Currency -->
        <div class="bento-card col-4">
          <div>
            <div class="bento-badge-row">
              <span class="micro-badge"><span class="badge-dot" style="background:var(--emerald);"></span>Bakong KHQR</span>
            </div>
            <h3 class="bento-card-title">Dual-Currency Sync</h3>
            <p class="bento-card-sub">Real-time webhook settlement in USD and KHR.</p>
          </div>

          <div class="currency-card-widget" data-ui="currency">
            <div class="curr-line">
              <span class="curr-tag">USD</span>
              <span class="curr-amount">$42,500.00</span>
            </div>
            <div class="curr-line">
              <span class="curr-tag">KHR</span>
              <span class="curr-amount">174,250,000 ៛</span>
            </div>
            <div class="curr-status">
              <span class="status-indicator"></span> Webhook settled via NBC Bakong
            </div>
          </div>
        </div>

        <!-- Card 5 (col-4): Neural Audio Briefing -->
        <div class="bento-card col-4">
          <div>
            <div class="bento-badge-row">
              <span class="micro-badge"><span class="badge-dot" style="background:var(--cobalt);"></span>Audio Engine</span>
            </div>
            <h3 class="bento-card-title">Neural Audio Briefing</h3>
            <p class="bento-card-sub">2-minute voice digest delivered to your phone at 08:00 AM.</p>
          </div>

          <div class="audio-mini-card" data-ui="audio">
            <div class="mini-play-circle">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg>
            </div>
            <div class="mini-wave-bars">
              <span class="m-bar" style="height: 10px;"></span>
              <span class="m-bar" style="height: 18px;"></span>
              <span class="m-bar" style="height: 12px;"></span>
              <span class="m-bar" style="height: 22px;"></span>
              <span class="m-bar" style="height: 15px;"></span>
              <span class="m-bar" style="height: 7px;"></span>
            </div>
            <span class="mini-duration">02:14</span>
          </div>
        </div>

        <!-- Card 6 (col-12): Operating Topology -->
        <div class="bento-card col-12">
          <div>
            <div class="bento-badge-row">
              <span class="micro-badge"><span class="badge-dot" style="background:var(--violet-bright);"></span>Architecture</span>
              <span class="badge-metric">Automated Loop</span>
            </div>
            <h3 class="bento-card-title">From Telegram Message to Executive Digest</h3>
            <p class="bento-card-sub">Four automated steps connecting frontline operations to executive strategy.</p>
          </div>

          <div class="clean-pipeline-strip" data-ui="pipeline">
            <div class="pipeline-step">
              <div class="step-num">STEP 01</div>
              <div class="step-title">Telegram Input</div>
              <div class="step-desc">60s staff check-in</div>
            </div>
            <div class="pipeline-step">
              <div class="step-num">STEP 02</div>
              <div class="step-title">Vector Memory</div>
              <div class="step-desc">AES-256 cloud vault</div>
            </div>
            <div class="pipeline-step">
              <div class="step-num">STEP 03</div>
              <div class="step-title">Conflict Radar</div>
              <div class="step-desc">Dependency resolution</div>
            </div>
            <div class="pipeline-step">
              <div class="step-num">STEP 04</div>
              <div class="step-title">Audio Digest</div>
              <div class="step-desc">8:00 AM executive brief</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- =======================================================================
         SCREEN 3: FOUNDER ROI CALCULATOR (#roi)
         ======================================================================= -->
    <section class="roi-section" id="roi">
      <div class="section-tag">VALUE QUANTIFICATION</div>
      <h2 class="section-title">Calculate Executive Hours Recovered</h2>
      <p class="section-lead">Estimate the managerial time and payroll waste AiOS eliminates for your organization.</p>

      <div class="roi-card">
        <!-- Sliders -->
        <div>
          <div class="slider-group">
            <div class="slider-header">
              <span>Full-Time Team Size</span>
              <span class="slider-val" id="teamSizeVal">35 Staff</span>
            </div>
            <input type="range" id="teamSizeRange" min="10" max="250" value="35" oninput="calculateROI()">
          </div>

          <div class="slider-group">
            <div class="slider-header">
              <span>Daily Reporting Waste per Manager</span>
              <span class="slider-val" id="timeWasteVal">45 Mins / Day</span>
            </div>
            <input type="range" id="timeWasteRange" min="15" max="90" step="5" value="45" oninput="calculateROI()">
          </div>

          <div class="slider-group">
            <div class="slider-header">
              <span>Executive / Founder Hourly Value</span>
              <span class="slider-val" id="hourlyRateVal">$175 / Hour</span>
            </div>
            <input type="range" id="hourlyRateRange" min="50" max="500" step="25" value="175" oninput="calculateROI()">
          </div>
        </div>

        <!-- Dynamic Output Display -->
        <div class="roi-display-box">
          <div style="font-size: 0.75rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase; margin-bottom: 4px;">Estimated Annual Value Recovered</div>
          <div class="roi-stat-main" id="annualSavings">$138,600</div>
          <div style="font-size: 0.8rem; color: var(--violet-light); font-weight: 600;">Based on recovered management attention & blocker prevention</div>

          <div class="roi-grid-mini">
            <div>
              <div class="roi-mini-num" id="hoursPerWeek">16.5 hrs</div>
              <div style="font-size: 0.74rem; color: var(--text-muted);">Saved per week</div>
            </div>
            <div>
              <div class="roi-mini-num" id="paybackDays">&lt; 12 Days</div>
              <div style="font-size: 0.74rem; color: var(--text-muted);">Payback period</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- =======================================================================
         SCREEN 4: TRANSPARENT 3-TIER ENTERPRISE PRICING (#pricing)
         ======================================================================= -->
    <section class="pricing-section" id="pricing">
      <div style="text-align: center; max-width: 700px; margin: 0 auto 30px;">
        <div class="section-tag">PREDICTABLE INVESTMENT</div>
        <h2 class="section-title">Transparent Pricing Built for Scale</h2>
        <p class="section-lead" style="margin: 0 auto;">Deploy within 15 minutes. No implementation contracts or consulting retainers.</p>
      </div>

      <!-- Billing Cycle Toggle -->
      <div class="billing-toggle-row">
        <button class="cycle-btn active" id="btnMonthly" onclick="setBillingCycle('monthly')">Monthly Billing</button>
        <button class="cycle-btn" id="btnAnnual" onclick="setBillingCycle('annual')">Annual Billing</button>
        <span class="discount-chip">Save 20%</span>
      </div>

      <div class="pricing-grid">
        <!-- Tier 1 -->
        <div class="price-card">
          <div>
            <div class="tier-name">Starter Pilot</div>
            <div class="tier-desc">For growing firms replacing manual status meetings with autonomous Telegram reports.</div>
            <div class="price-row">
              <span class="price-val" id="priceStarter">$490</span>
              <span class="price-period">/ month</span>
            </div>
            <ul class="feature-list">
              <li class="feature-item">
                <svg viewBox="0 0 24 24" fill="none"><path d="M20 6L9 17l-5-5"/></svg>
                <span>Up to 25 team members</span>
              </li>
              <li class="feature-item">
                <svg viewBox="0 0 24 24" fill="none"><path d="M20 6L9 17l-5-5"/></svg>
                <span>Telegram native check-in bots</span>
              </li>
              <li class="feature-item">
                <svg viewBox="0 0 24 24" fill="none"><path d="M20 6L9 17l-5-5"/></svg>
                <span>Daily 8:00 AM text synthesis</span>
              </li>
              <li class="feature-item">
                <svg viewBox="0 0 24 24" fill="none"><path d="M20 6L9 17l-5-5"/></svg>
                <span>Standard email & chat support</span>
              </li>
            </ul>
          </div>
          <a href="https://t.me/DanLP18" target="_blank" class="tier-btn btn-tier-default">Start Starter Pilot</a>
        </div>

        <!-- Tier 2 (Featured) -->
        <div class="price-card featured">
          <div class="featured-badge">MOST POPULAR</div>
          <div>
            <div class="tier-name">Growth Operating</div>
            <div class="tier-desc">Complete autonomous loop with neural audio digests, Bakong KHQR sync, and blocker radar.</div>
            <div class="price-row">
              <span class="price-val" id="priceGrowth">$1,290</span>
              <span class="price-period">/ month</span>
            </div>
            <ul class="feature-list">
              <li class="feature-item">
                <svg viewBox="0 0 24 24" fill="none"><path d="M20 6L9 17l-5-5"/></svg>
                <span>Up to 100 team members</span>
              </li>
              <li class="feature-item">
                <svg viewBox="0 0 24 24" fill="none"><path d="M20 6L9 17l-5-5"/></svg>
                <span>Daily 8:00 AM neural voice brief</span>
              </li>
              <li class="feature-item">
                <svg viewBox="0 0 24 24" fill="none"><path d="M20 6L9 17l-5-5"/></svg>
                <span>Bakong KHQR webhook reconciliation</span>
              </li>
              <li class="feature-item">
                <svg viewBox="0 0 24 24" fill="none"><path d="M20 6L9 17l-5-5"/></svg>
                <span>Live revenue blocker interceptor</span>
              </li>
            </ul>
          </div>
          <a href="https://t.me/DanLP18" target="_blank" class="tier-btn btn-tier-featured">Start 14-Day Free Pilot</a>
        </div>

        <!-- Tier 3 -->
        <div class="price-card">
          <div>
            <div class="tier-name">Enterprise Custom</div>
            <div class="tier-desc">Dedicated cloud tenant, custom ERP webhooks, on-premise LLM routing, and 24/7 SLA.</div>
            <div class="price-row">
              <span class="price-val" id="priceEnterprise">$3,490</span>
              <span class="price-period">/ month</span>
            </div>
            <ul class="feature-list">
              <li class="feature-item">
                <svg viewBox="0 0 24 24" fill="none"><path d="M20 6L9 17l-5-5"/></svg>
                <span>Unlimited team members</span>
              </li>
              <li class="feature-item">
                <svg viewBox="0 0 24 24" fill="none"><path d="M20 6L9 17l-5-5"/></svg>
                <span>Isolated private cloud tenant</span>
              </li>
              <li class="feature-item">
                <svg viewBox="0 0 24 24" fill="none"><path d="M20 6L9 17l-5-5"/></svg>
                <span>Custom ERP & database integrations</span>
              </li>
              <li class="feature-item">
                <svg viewBox="0 0 24 24" fill="none"><path d="M20 6L9 17l-5-5"/></svg>
                <span>Dedicated solution architect</span>
              </li>
            </ul>
          </div>
          <a href="https://t.me/DanLP18" target="_blank" class="tier-btn btn-tier-default">Contact Executive Team</a>
        </div>
      </div>
    </section>

    <!-- =======================================================================
         SCREEN 5: EXECUTIVE FAQ (#faq)
         ======================================================================= -->
    <section class="faq-section" id="faq">
      <div class="faq-layout">
        <div>
          <div class="section-tag">EXECUTIVE FAQ</div>
          <h2 class="section-title">Common Questions</h2>
          <p class="section-lead">Everything executive leadership needs to know about security, rollout, and architecture.</p>
        </div>

        <div>
          <div class="faq-item">
            <div class="faq-q">
              <span>Do our employees have to download or learn any new apps?</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
            </div>
            <div class="faq-a">
              No. Staff report directly within their existing Telegram app in under 60 seconds. There are zero new software logins or training sessions required.
            </div>
          </div>

          <div class="faq-item">
            <div class="faq-q">
              <span>How does AiOS handle sensitive corporate and financial data?</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
            </div>
            <div class="faq-a">
              All communications are encrypted in transit and at rest using AES-256. Customer data is strictly isolated within dedicated cloud partitions and is never used to train public LLM models.
            </div>
          </div>

          <div class="faq-item">
            <div class="faq-q">
              <span>Can AiOS connect directly to National Bank of Cambodia Bakong KHQR?</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
            </div>
            <div class="faq-a">
              Yes. AiOS includes pre-built settlement webhooks supporting dual-currency (USD and KHR) reconciliation directly against your daily operational ledger.
            </div>
          </div>

          <div class="faq-item">
            <div class="faq-q">
              <span>What is the typical deployment timeframe?</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
            </div>
            <div class="faq-a">
              Standard deployment takes under 15 minutes. We connect your Telegram bot token, configure department routing, and your executive briefing begins the following morning at 8:00 AM.
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>

  <!-- FOOTER -->
  <footer>
    <div style="display: flex; align-items: center; gap: 12px;">
      <span style="font-weight: 800; color: #fff;">Nexus AiOS</span>
      <span>•</span>
      <span>Autonomous Operating Intelligence</span>
    </div>
    <p>© 2026 Nexus Group International. All rights reserved.</p>
  </footer>

  <!-- INTERACTIVE APPLICATION LOGIC -->
  <script>
    /* 1. AUDIO DIGEST PLAYER WITH WEB AUDIO SYNTH */
    let isPlaying = false;
    let timerInterval = null;
    let seconds = 0;
    let playbackSpeed = 1.0;
    let audioCtx = null;

    function playExecutiveChime() {
      try {
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        if (!audioCtx) audioCtx = new AudioContext();
        if (audioCtx.state === 'suspended') audioCtx.resume();

        // Twin-tone executive chime (587.33Hz D5 -> 880Hz A5 subtle sine)
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(587.33, audioCtx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(880, audioCtx.currentTime + 0.14);
        gain.gain.setValueAtTime(0.08, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.75);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + 0.8);
      } catch (e) {}
    }

    function toggleAudio() {
      isPlaying = !isPlaying;
      const playIcon = document.getElementById('playIcon');
      const timer = document.getElementById('digestTimer');
      const bars = document.querySelectorAll('.wf-bar');

      if (isPlaying) {
        playExecutiveChime();
        playIcon.innerHTML = '<rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/>';
        bars.forEach(b => b.style.animationPlayState = 'running');
        clearInterval(timerInterval);
        timerInterval = setInterval(() => {
          seconds += Math.round(playbackSpeed);
          const m = String(Math.floor(seconds / 60)).padStart(2, '0');
          const s = String(seconds % 60).padStart(2, '0');
          timer.innerText = m + ':' + s + ' / 02:14';
          if (seconds >= 134) toggleAudio();
        }, 1000 / playbackSpeed);
      } else {
        playIcon.innerHTML = '<polygon points="5 3 19 12 5 21 5 3"/>';
        bars.forEach(b => b.style.animationPlayState = 'paused');
        clearInterval(timerInterval);
      }
    }

    function setSpeed(speed, btn) {
      playbackSpeed = speed;
      document.querySelectorAll('.s-pill').forEach(p => p.classList.remove('active'));
      btn.classList.add('active');
      const bars = document.querySelectorAll('.wf-bar');
      bars.forEach(b => b.style.animationDuration = (1.2 / speed) + 's');
      if (isPlaying) {
        toggleAudio();
        toggleAudio();
      }
    }

    /* 2. TELEGRAM STREAM DRAWER EXPANDER */
    function toggleStreamDrawer(item) {
      item.classList.toggle('expanded');
    }

    /* 3. FOUNDER ROI CALCULATOR */
    function calculateROI() {
      const teamSize = parseInt(document.getElementById('teamSizeRange').value, 10);
      const timeWaste = parseInt(document.getElementById('timeWasteRange').value, 10);
      const hourlyRate = parseInt(document.getElementById('hourlyRateRange').value, 10);

      document.getElementById('teamSizeVal').innerText = teamSize + ' Staff';
      document.getElementById('timeWasteVal').innerText = timeWaste + ' Mins / Day';
      document.getElementById('hourlyRateVal').innerText = '$' + hourlyRate + ' / Hour';

      const managers = Math.max(1, Math.round(teamSize / 7));
      const hoursSavedPerDay = (managers * timeWaste) / 60;
      const hoursSavedPerWeek = hoursSavedPerDay * 5;
      const annualHours = hoursSavedPerWeek * 48;
      const annualValue = annualHours * hourlyRate;

      document.getElementById('hoursPerWeek').innerText = hoursSavedPerWeek.toFixed(1) + ' hrs';
      document.getElementById('annualSavings').innerText = '$' + Math.round(annualValue).toLocaleString();
    }

    /* 4. BILLING CYCLE TOGGLE */
    function setBillingCycle(cycle) {
      const btnMonthly = document.getElementById('btnMonthly');
      const btnAnnual = document.getElementById('btnAnnual');
      const pStarter = document.getElementById('priceStarter');
      const pGrowth = document.getElementById('priceGrowth');
      const pEnterprise = document.getElementById('priceEnterprise');

      if (cycle === 'annual') {
        btnMonthly.classList.remove('active');
        btnAnnual.classList.add('active');
        pStarter.innerText = '$392';
        pGrowth.innerText = '$1,032';
        pEnterprise.innerText = '$2,792';
      } else {
        btnAnnual.classList.remove('active');
        btnMonthly.classList.add('active');
        pStarter.innerText = '$490';
        pGrowth.innerText = '$1,290';
        pEnterprise.innerText = '$3,490';
      }
    }
  </script>
</body>
</html>
"""

with open("sites/01_aios/index.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("Successfully written sites/01_aios/index.html, length:", len(html_code))
