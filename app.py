import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="MoodTune AI",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
#MainMenu,footer,header{visibility:hidden}
.block-container{padding:0!important;max-width:100%!important}
section[data-testid="stSidebar"]{display:none}
div[data-testid="stToolbar"]{display:none}
.stApp{background:#060606!important}
</style>
""", unsafe_allow_html=True)

HTML = r"""<!DOCTYPE html>
<html lang="uz">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet"/>
<style>
:root{
  --bg:#060606;--surface:#111111;--surface2:#1a1a1a;
  --border:#222222;--fire:#ff5722;--fire-glow:#ff9100;
  --text:#f5f5f5;--muted:#777777;--radius:16px;
  --font-head:'Space Grotesk',sans-serif;--font-mono:'Space Mono',monospace;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html,body{background:var(--bg);color:var(--text);font-family:var(--font-head);min-height:100vh;overflow-x:hidden}

/* HEADER */
header{display:flex;align-items:center;justify-content:space-between;padding:16px 28px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(6,6,6,0.97);backdrop-filter:blur(16px);z-index:100;flex-wrap:wrap;gap:10px}
.logo-area{display:flex;align-items:center;gap:12px}
.fire-wings{display:flex;align-items:center;width:44px;height:24px}
.wing{width:20px;height:20px;background:linear-gradient(45deg,var(--fire),var(--fire-glow));filter:drop-shadow(0 0 8px var(--fire))}
.wing.left{border-radius:0 100% 30% 100%;animation:flapLeft 3s ease-in-out infinite alternate}
.wing.right{border-radius:100% 0 100% 30%;animation:flapRight 3s ease-in-out infinite alternate}
@keyframes flapLeft{0%{transform:rotate(-25deg) scaleY(0.9)}100%{transform:rotate(-5deg) scaleY(1.1)}}
@keyframes flapRight{0%{transform:rotate(25deg) scaleY(0.9)}100%{transform:rotate(5deg) scaleY(1.1)}}
.logo-text{font-weight:700;font-size:1.25rem;letter-spacing:-0.03em}
.logo-text span{color:transparent;background:linear-gradient(to right,var(--fire-glow),#fff);-webkit-background-clip:text;background-clip:text}
.nav-tabs{display:flex;gap:4px;background:var(--surface);padding:4px;border-radius:10px;border:1px solid var(--border)}
.nav-tab{background:none;border:none;color:var(--muted);font-family:var(--font-head);font-size:0.82rem;font-weight:600;padding:7px 14px;cursor:pointer;border-radius:6px;transition:all 0.2s;white-space:nowrap}
.nav-tab.active{background:var(--surface2);color:var(--fire-glow);border:1px solid rgba(255,87,34,0.2)}
.lang-panel{display:flex;gap:4px;background:var(--surface);padding:4px;border-radius:10px;border:1px solid var(--border)}
.lang-btn{background:none;border:none;color:var(--muted);font-family:var(--font-mono);font-size:0.75rem;padding:6px 10px;cursor:pointer;border-radius:6px;transition:all 0.2s}
.lang-btn.active{background:var(--surface2);color:var(--fire-glow);border:1px solid rgba(255,87,34,0.2)}

/* PAGES */
.page{display:none;flex:1;flex-direction:column}
.page.active{display:flex}

/* MAIN CONTENT */
.main-wrap{max-width:740px;margin:0 auto;padding:28px 20px 60px;width:100%}

/* TRENDING */
.trending-title{font-size:0.74rem;font-weight:600;text-transform:uppercase;letter-spacing:0.1em;color:var(--muted);margin-bottom:14px;display:flex;align-items:center;gap:10px}
.trending-title::after{content:'';flex:1;height:1px;background:var(--border)}
.genre-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin-bottom:32px}
.genre-card{background:var(--surface);border:1px solid var(--border);border-radius:12px;overflow:hidden;cursor:pointer;transition:all 0.25s}
.genre-card:hover{border-color:var(--fire);transform:translateY(-2px);box-shadow:0 8px 24px rgba(255,87,34,0.12)}
.genre-thumb{width:100%;aspect-ratio:16/9;object-fit:cover;display:block;background:var(--surface2)}
.genre-thumb-placeholder{width:100%;aspect-ratio:16/9;display:flex;align-items:center;justify-content:center;font-size:2.2rem;background:linear-gradient(135deg,var(--surface2),#0d0d0d)}
.genre-info{padding:10px 12px}
.genre-label{font-size:0.68rem;font-weight:700;text-transform:uppercase;letter-spacing:0.08em;color:var(--fire-glow);margin-bottom:3px}
.genre-track{font-size:0.85rem;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.genre-artist{font-size:0.75rem;color:var(--muted);margin-top:1px}

/* DIVIDER */
.section-divider{display:flex;align-items:center;gap:12px;margin:8px 0 20px}
.section-divider::before,.section-divider::after{content:'';flex:1;height:1px;background:var(--border)}
.section-divider span{font-size:0.72rem;font-weight:600;text-transform:uppercase;letter-spacing:0.1em;color:var(--muted);white-space:nowrap}

/* ─── MOOD TEST ─────────────────────────────────────────── */
.test-section{margin-bottom:40px}
.q-card{background:var(--surface);border:1px solid var(--border);border-radius:18px;padding:22px;animation:fadeSlide 0.35s cubic-bezier(0.16,1,0.3,1)}
@keyframes fadeSlide{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:translateY(0)}}
.progress-wrap{margin-bottom:18px}
.progress-top{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}
.progress-label{font-size:0.72rem;font-weight:700;text-transform:uppercase;letter-spacing:0.08em;color:var(--muted)}
.progress-count{font-family:var(--font-mono);font-size:0.72rem;color:var(--fire-glow)}
.progress-bar-track{height:3px;background:var(--border);border-radius:3px;overflow:hidden}
.progress-bar-fill{height:100%;background:linear-gradient(to right,var(--fire),var(--fire-glow));border-radius:3px;transition:width 0.4s ease}
.progress-dots{display:flex;gap:6px;margin-top:10px}
.p-dot{width:8px;height:8px;border-radius:50%;background:var(--border);transition:all 0.3s}
.p-dot.done{background:var(--fire)}
.p-dot.active{background:var(--fire-glow);box-shadow:0 0 8px var(--fire-glow);transform:scale(1.2)}
.q-number{font-size:0.68rem;font-weight:700;text-transform:uppercase;letter-spacing:0.1em;color:var(--fire-glow);margin-bottom:8px}
.q-text{font-size:1rem;font-weight:600;line-height:1.45;margin-bottom:18px;color:var(--text)}
.options{display:flex;flex-direction:column;gap:9px}
.opt-btn{display:flex;align-items:flex-start;gap:12px;background:rgba(255,255,255,0.025);border:1px solid rgba(255,255,255,0.07);border-radius:12px;padding:13px 15px;cursor:pointer;transition:all 0.2s;text-align:left;width:100%;font-family:var(--font-head)}
.opt-btn:hover{background:rgba(255,87,34,0.07);border-color:rgba(255,87,34,0.3);transform:translateX(3px)}
.opt-btn.selected{background:rgba(255,87,34,0.12);border-color:rgba(255,87,34,0.5)}
.opt-key{display:flex;align-items:center;justify-content:center;width:26px;height:26px;border-radius:8px;background:rgba(255,87,34,0.12);border:1px solid rgba(255,87,34,0.2);color:var(--fire-glow);font-weight:700;font-size:0.72rem;font-family:var(--font-mono);flex-shrink:0;margin-top:1px;transition:all 0.2s}
.opt-btn:hover .opt-key,.opt-btn.selected .opt-key{background:var(--fire);color:#fff;border-color:var(--fire)}
.opt-content{flex:1}
.opt-label{font-size:0.9rem;font-weight:600;color:var(--text);line-height:1.3}
.opt-sub{font-size:0.75rem;color:var(--muted);margin-top:3px;line-height:1.3}

/* ─── RESULT ─────────────────────────────────────────────── */
.result-card{background:var(--surface);border:1px solid rgba(255,87,34,0.25);border-radius:20px;overflow:hidden;animation:fadeSlide 0.4s cubic-bezier(0.16,1,0.3,1);margin-bottom:24px}
.result-banner{padding:28px 24px 22px;text-align:center;position:relative;overflow:hidden}
.result-banner::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 50% 0%,rgba(255,87,34,0.18) 0%,transparent 70%)}
.result-vibe-icon{font-size:3rem;margin-bottom:10px;display:block;animation:pop 0.5s cubic-bezier(0.16,1,0.3,1)}
@keyframes pop{from{transform:scale(0.5);opacity:0}to{transform:scale(1);opacity:1}}
.result-vibe-name{font-size:1.4rem;font-weight:700;color:var(--fire-glow);margin-bottom:8px;position:relative}
.result-desc{font-size:0.88rem;color:#bbb;line-height:1.6;max-width:440px;margin:0 auto;position:relative}
.result-genres{display:flex;flex-wrap:wrap;gap:7px;padding:16px 20px;border-top:1px solid var(--border);border-bottom:1px solid var(--border)}
.result-genre-tag{background:rgba(255,87,34,0.08);border:1px solid rgba(255,87,34,0.2);color:var(--fire-glow);padding:5px 13px;border-radius:20px;font-size:0.78rem;font-weight:600}
.tracks-header{padding:14px 20px 10px;font-size:0.68rem;font-weight:700;text-transform:uppercase;letter-spacing:0.1em;color:var(--muted);display:flex;align-items:center;gap:8px}
.tracks-header::after{content:'';flex:1;height:1px;background:var(--border)}
.track-list{padding:0 12px 16px;display:flex;flex-direction:column;gap:6px}
.music-track{display:flex;align-items:center;background:rgba(255,255,255,0.025);border:1px solid rgba(255,255,255,0.05);border-radius:10px;text-decoration:none;color:#fff;transition:all 0.22s;overflow:hidden}
.music-track:hover{background:rgba(255,87,34,0.07);border-color:rgba(255,87,34,0.35);transform:translateX(3px);box-shadow:0 4px 16px rgba(255,87,34,0.1)}
.track-thumb-wrap{position:relative;flex-shrink:0;width:88px;height:56px}
.track-thumb{width:88px;height:56px;object-fit:cover;display:block}
.track-thumb-ph{width:88px;height:56px;background:linear-gradient(135deg,#1a1a1a,#0d0d0d);display:flex;align-items:center;justify-content:center;font-size:1.4rem}
.track-num-badge{position:absolute;bottom:3px;right:3px;min-width:18px;height:18px;background:rgba(0,0,0,0.78);border-radius:4px;font-size:0.6rem;font-weight:700;display:flex;align-items:center;justify-content:center;color:#fff;padding:0 4px;backdrop-filter:blur(4px)}
.track-info{flex:1;min-width:0;padding:0 12px}
.track-title{font-weight:600;font-size:0.87rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;color:#f0f0f0;letter-spacing:-0.01em}
.track-artist{font-size:0.72rem;color:var(--muted);margin-top:3px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.track-yt{flex-shrink:0;display:flex;align-items:center;gap:5px;font-family:var(--font-mono);font-size:0.65rem;font-weight:700;background:rgba(255,0,0,0.1);border-left:1px solid rgba(255,255,255,0.05);color:#ff5555;padding:0 14px;height:56px;white-space:nowrap;transition:background 0.2s}
.music-track:hover .track-yt{background:rgba(255,0,0,0.2)}
.retry-row{display:flex;gap:10px;flex-wrap:wrap}
.retry-btn{flex:1;min-width:140px;background:none;border:1px solid var(--border);color:var(--muted);padding:12px 18px;border-radius:12px;font-family:var(--font-head);font-size:0.88rem;font-weight:600;cursor:pointer;transition:all 0.2s}
.retry-btn:hover{border-color:var(--fire);color:var(--text)}
.retry-btn.primary{background:linear-gradient(135deg,var(--fire),var(--fire-glow));border-color:transparent;color:#fff}
.retry-btn.primary:hover{opacity:0.9;transform:translateY(-1px);box-shadow:0 6px 20px rgba(255,87,34,0.3)}

/* ─── MUSIC INFO PAGE ────────────────────────────────────── */
.info-page-wrap{max-width:740px;margin:0 auto;padding:28px 20px 60px;width:100%;display:flex;flex-direction:column;gap:0}
.info-welcome-card{background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:26px 22px;margin-bottom:20px}
.info-welcome-icon{font-size:2.2rem;margin-bottom:10px}
.info-welcome-title{font-size:1.25rem;font-weight:700;margin-bottom:6px}
.info-welcome-sub{color:var(--muted);font-size:0.88rem;line-height:1.55}
.info-chips{display:flex;gap:8px;flex-wrap:wrap;margin-top:14px}
.info-chip{background:rgba(255,87,34,0.08);border:1px solid rgba(255,87,34,0.2);color:var(--fire-glow);padding:7px 13px;border-radius:20px;font-size:0.8rem;cursor:pointer;transition:all 0.2s}
.info-chip:hover{background:rgba(255,87,34,0.16);border-color:var(--fire)}
.info-search-box{display:flex;gap:10px;align-items:center;background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:4px 4px 4px 16px;margin-bottom:20px;transition:border-color 0.2s}
.info-search-box:focus-within{border-color:var(--fire)}
.info-search-input{flex:1;background:none;border:none;outline:none;color:var(--text);font-family:var(--font-head);font-size:0.95rem;padding:8px 0}
.info-search-input::placeholder{color:var(--muted)}
.info-search-btn{width:44px;height:44px;border-radius:10px;background:linear-gradient(135deg,var(--fire),var(--fire-glow));border:none;cursor:pointer;display:flex;align-items:center;justify-content:center;color:#fff;flex-shrink:0;transition:transform 0.2s}
.info-search-btn:hover{transform:scale(1.04)}
.info-search-btn:disabled{background:var(--surface2);color:var(--muted);cursor:not-allowed}
.info-search-btn svg{width:18px;height:18px}
.info-results{display:flex;flex-direction:column;gap:16px}

/* Info cards */
.info-card{background:var(--surface);border:1px solid var(--border);border-radius:16px;overflow:hidden;animation:fadeSlide 0.35s cubic-bezier(0.16,1,0.3,1)}
.info-card-header{padding:20px;display:flex;align-items:center;gap:16px;border-bottom:1px solid var(--border);background:linear-gradient(135deg,rgba(255,87,34,0.06),transparent)}
.info-card-photo{width:68px;height:68px;border-radius:14px;object-fit:cover;border:2px solid rgba(255,87,34,0.4);flex-shrink:0}
.info-card-emoji{width:68px;height:68px;border-radius:14px;background:var(--surface2);border:2px solid var(--border);display:flex;align-items:center;justify-content:center;font-size:2.5rem;flex-shrink:0}
.info-card-name{font-size:1.15rem;font-weight:700;margin-bottom:4px}
.info-card-tagline{font-size:0.83rem;color:var(--muted);line-height:1.4}
.info-card-body{padding:16px 20px}
.info-section{margin-bottom:16px}
.info-section:last-child{margin-bottom:0}
.info-section-title{font-size:0.7rem;font-weight:700;text-transform:uppercase;letter-spacing:0.1em;color:var(--fire-glow);margin-bottom:10px;display:flex;align-items:center;gap:8px}
.info-section-title::after{content:'';flex:1;height:1px;background:rgba(255,87,34,0.15)}
.info-fact-row{display:flex;gap:8px;margin-bottom:6px;align-items:flex-start}
.info-fact-key{font-size:0.78rem;color:var(--muted);min-width:90px;flex-shrink:0}
.info-fact-val{font-size:0.85rem;color:var(--text);font-weight:500}
.info-prose{font-size:0.9rem;color:#d0d0d0;line-height:1.65}
.info-stat-row{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:4px}
.info-stat{background:var(--surface2);border:1px solid var(--border);border-radius:10px;padding:10px 16px;text-align:center;flex:1;min-width:80px}
.info-stat-num{font-size:1.1rem;font-weight:700;color:var(--fire-glow)}
.info-stat-lbl{font-size:0.7rem;color:var(--muted);margin-top:2px}
.info-album-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(130px,1fr));gap:8px}
.info-album-card{background:var(--surface2);border:1px solid var(--border);border-radius:10px;padding:12px;text-align:center}
.info-album-name{font-size:0.82rem;font-weight:600;margin-bottom:4px}
.info-album-year{font-size:0.72rem;color:var(--fire-glow);font-family:var(--font-mono)}
.info-tag-list{display:flex;flex-wrap:wrap;gap:6px}
.info-tag{background:rgba(255,87,34,0.08);border:1px solid rgba(255,87,34,0.2);color:var(--fire-glow);padding:5px 11px;border-radius:20px;font-size:0.76rem}
.info-summary{margin-top:4px;padding:12px 16px;background:rgba(255,87,34,0.05);border-left:3px solid var(--fire);border-radius:0 8px 8px 0;font-size:0.88rem;color:#bbb;line-height:1.6}
.info-not-found{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:32px;text-align:center;color:var(--muted)}
.info-not-found .big-icon{font-size:2.5rem;margin-bottom:12px}

/* Info track list */
.info-track-item{display:flex;align-items:center;background:rgba(255,255,255,0.025);border:1px solid rgba(255,255,255,0.05);border-radius:10px;text-decoration:none;color:#fff;transition:all 0.22s;overflow:hidden;margin-bottom:6px}
.info-track-item:hover{background:rgba(255,87,34,0.07);border-color:rgba(255,87,34,0.35);transform:translateX(3px)}

/* GENRE MODAL */
.genre-modal-overlay{position:fixed;inset:0;background:rgba(0,0,0,0.85);backdrop-filter:blur(8px);z-index:200;display:none;align-items:center;justify-content:center;padding:20px}
.genre-modal-overlay.open{display:flex}
.genre-modal{background:var(--surface);border:1px solid var(--border);border-radius:20px;max-width:520px;width:100%;max-height:82vh;overflow-y:auto;position:relative;animation:fadeSlide 0.35s cubic-bezier(0.16,1,0.3,1)}
.genre-modal-header{padding:18px 20px 14px;border-bottom:1px solid var(--border);position:sticky;top:0;background:var(--surface);z-index:2;display:flex;align-items:center;justify-content:space-between}
.genre-modal-title{font-size:1rem;font-weight:700;display:flex;align-items:center;gap:8px}
.genre-modal-label{font-size:0.72rem;font-weight:700;text-transform:uppercase;letter-spacing:0.08em;color:var(--fire-glow)}
.genre-modal-close{background:var(--surface2);border:1px solid var(--border);color:var(--muted);width:34px;height:34px;border-radius:50%;cursor:pointer;font-size:1.1rem;display:flex;align-items:center;justify-content:center;transition:all 0.2s}
.genre-modal-close:hover{border-color:var(--fire);color:#fff}
.genre-modal-list{padding:14px;display:flex;flex-direction:column;gap:8px}
.modal-track{display:flex;align-items:center;gap:12px;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.06);padding:10px 13px;border-radius:10px;text-decoration:none;color:#fff;transition:all 0.2s}
.modal-track:hover{background:rgba(255,87,34,0.1);border-color:var(--fire);transform:translateX(3px)}
.modal-track-num{width:24px;height:24px;background:var(--surface2);border:1px solid var(--border);border-radius:50%;font-size:0.7rem;font-weight:700;color:var(--fire-glow);display:flex;align-items:center;justify-content:center;flex-shrink:0}
.modal-track-thumb{width:64px;height:42px;border-radius:7px;object-fit:cover;flex-shrink:0;background:var(--surface2)}
.modal-track-thumb-ph{width:64px;height:42px;border-radius:7px;background:linear-gradient(135deg,#1e1e1e,#0d0d0d);display:flex;align-items:center;justify-content:center;font-size:1.2rem;flex-shrink:0;border:1px solid var(--border)}
.modal-track-info{flex:1;min-width:0}
.modal-track-title{font-size:0.88rem;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.modal-track-artist{font-size:0.75rem;color:var(--muted);margin-top:2px}
.modal-yt-btn{background:rgba(255,0,0,0.12);border:1px solid rgba(255,0,0,0.3);color:#ff4444;padding:5px 10px;border-radius:20px;font-size:0.7rem;font-weight:700;white-space:nowrap;flex-shrink:0}

/* Typing loader */
.typing-dots{display:flex;gap:5px;align-items:center;padding:4px 0}
.typing-dots span{width:7px;height:7px;border-radius:50%;background:var(--muted);animation:bounce 1.2s infinite ease-in-out}
.typing-dots span:nth-child(2){animation-delay:0.15s}
.typing-dots span:nth-child(3){animation-delay:0.3s}
@keyframes bounce{0%,100%{transform:translateY(0)}50%{transform:translateY(-7px)}}

::-webkit-scrollbar{width:5px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:#333;border-radius:5px}
</style>
</head>
<body>

<header>
  <div class="logo-area">
    <div class="fire-wings"><div class="wing left"></div><div class="wing right"></div></div>
    <div class="logo-text">MoodTune<span>AI</span></div>
  </div>
  <div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap">
    <div class="nav-tabs">
      <button class="nav-tab active" data-page="page-home">🎵 Musiqa</button>
      <button class="nav-tab" data-page="page-info">🎤 Music Info</button>
    </div>
    <div class="lang-panel" id="lang-panel">
      <button class="lang-btn active" data-lang="uz">UZ</button>
      <button class="lang-btn" data-lang="ru">RU</button>
      <button class="lang-btn" data-lang="en">EN</button>
    </div>
  </div>
</header>

<!-- PAGE 1: HOME (Trending + Kayfiyat Testi) -->
<div class="page active" id="page-home">
  <div class="main-wrap">
    <div class="trending-title" id="trending-title">🔥 Trending hozir — bosing va tinglang</div>
    <div class="genre-grid" id="genre-grid"></div>

    <div class="section-divider"><span>🎭 Kayfiyat Testi</span></div>
    <div class="test-section" id="test-section"></div>
  </div>
</div>

<!-- PAGE 2: MUSIC INFO -->
<div class="page" id="page-info">
  <div class="info-page-wrap">
    <div class="info-welcome-card" id="info-welcome">
      <div class="info-welcome-icon">🎤</div>
      <div class="info-welcome-title" id="info-welcome-title">Music Info Assistant</div>
      <div class="info-welcome-sub" id="info-welcome-sub">Artist, albom yoki qo'shiq haqida biror narsa so'rang.</div>
      <div class="info-chips" id="info-chips">
        <span class="info-chip" onclick="infoSearch('The Weeknd')">The Weeknd</span>
        <span class="info-chip" onclick="infoSearch('Eminem')">Eminem</span>
        <span class="info-chip" onclick="infoSearch('Billie Eilish')">Billie Eilish</span>
        <span class="info-chip" onclick="infoSearch('Drake')">Drake</span>
        <span class="info-chip" onclick="infoSearch('Скриптонит')">Скриптонит</span>
        <span class="info-chip" onclick="infoSearch('BAKR')">BAKR</span>
      </div>
    </div>

    <div class="info-search-box">
      <input class="info-search-input" id="info-input" type="text"
        placeholder="Artist, albom yoki qo'shiq nomi..." autocomplete="off"/>
      <button class="info-search-btn" id="info-send-btn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
        </svg>
      </button>
    </div>

    <div class="info-results" id="info-results"></div>
  </div>
</div>

<!-- GENRE MODAL -->
<div class="genre-modal-overlay" id="genre-modal-overlay">
  <div class="genre-modal">
    <div class="genre-modal-header">
      <div>
        <div class="genre-modal-label" id="modal-genre-label"></div>
        <div class="genre-modal-title" id="modal-genre-title"></div>
      </div>
      <button class="genre-modal-close" id="genre-modal-close">✕</button>
    </div>
    <div class="genre-modal-list" id="genre-modal-list"></div>
  </div>
</div>

<script>
// ── DATA ──────────────────────────────────────────────────────────────────────
const GENRES = [
  {label:"Pop / R&B", icon:"🎶", track:"Blinding Lights", artist:"The Weeknd", ytId:"4NRXx6U8ABQ"},
  {label:"Rap / Hip-Hop", icon:"🎤", track:"God's Plan", artist:"Drake", ytId:"xpVfcZ0ZcFM"},
  {label:"Classic Rock", icon:"🎸", track:"Bohemian Rhapsody", artist:"Queen", ytId:"fJ9rUzIMcZQ"},
  {label:"Nostalgic", icon:"🌅", track:"Hotel California", artist:"Eagles", ytId:"BciS5krYL80"}
];

const GENRE_SONGS = {
  "Pop / R&B":[
    {title:"Blinding Lights",artist:"The Weeknd",ytId:"4NRXx6U8ABQ"},
    {title:"As It Was",artist:"Harry Styles",ytId:"H5v3kku4y6Q"},
    {title:"Watermelon Sugar",artist:"Harry Styles",ytId:"E07s5ZYygMg"},
    {title:"Anti-Hero",artist:"Taylor Swift",ytId:"b1kbLwvqugk"},
    {title:"Levitating",artist:"Dua Lipa",ytId:"TUVcZfQe-Kw"},
    {title:"Save Your Tears",artist:"The Weeknd",ytId:"XXYlFuWEuKI"},
    {title:"Stay",artist:"The Kid LAROI & Justin Bieber",ytId:"kTJczUoc26U"},
    {title:"Positions",artist:"Ariana Grande",ytId:"tcYodQoapMg"},
    {title:"Good 4 U",artist:"Olivia Rodrigo",ytId:"gNi_6U5Pm_o"},
    {title:"Starboy",artist:"The Weeknd",ytId:"34Na4j8AVgA"},
    {title:"Shape of You",artist:"Ed Sheeran",ytId:"JGwWNGJdvx8"},
    {title:"Circles",artist:"Post Malone",ytId:"wXhTHyIgQ_U"},
    {title:"Love Story (Taylor's Version)",artist:"Taylor Swift",ytId:"8xg3vE8Ie_E"},
    {title:"Peaches",artist:"Justin Bieber",ytId:"tQ0yjYUFKAE"},
    {title:"drivers license",artist:"Olivia Rodrigo",ytId:"ZmDBbnmKpqQ"}
  ],
  "Rap / Hip-Hop":[
    {title:"God's Plan",artist:"Drake",ytId:"xpVfcZ0ZcFM"},
    {title:"HUMBLE.",artist:"Kendrick Lamar",ytId:"tvTRZJ-4EyI"},
    {title:"Rockstar",artist:"Post Malone ft. 21 Savage",ytId:"UceaB4D0jpo"},
    {title:"Sicko Mode",artist:"Travis Scott",ytId:"6ONRf7h3Mdk"},
    {title:"Lucid Dreams",artist:"Juice WRLD",ytId:"mzB1VGEGcSU"},
    {title:"Hotline Bling",artist:"Drake",ytId:"uxpDa-c-4Mc"},
    {title:"Rap God",artist:"Eminem",ytId:"XbGs_qK2PQA"},
    {title:"MIDDLE CHILD",artist:"J. Cole",ytId:"MaT4Jk77af8"},
    {title:"Old Town Road",artist:"Lil Nas X",ytId:"w2Ov5jzm3j8"},
    {title:"Congratulations",artist:"Post Malone",ytId:"SC4xMk98Pdc"},
    {title:"XO Tour Llif3",artist:"Lil Uzi Vert",ytId:"WrsFXgrun6g"},
    {title:"Big Rings",artist:"Drake & Future",ytId:"7GaRr2GGzao"},
    {title:"Money In The Grave",artist:"Drake ft. Rick Ross",ytId:"RjWGetUKqzM"}
  ],
  "Classic Rock":[
    {title:"Bohemian Rhapsody",artist:"Queen",ytId:"fJ9rUzIMcZQ"},
    {title:"Don't Stop Me Now",artist:"Queen",ytId:"HgzGwKwLmgM"},
    {title:"Hotel California",artist:"Eagles",ytId:"BciS5krYL80"},
    {title:"Stairway to Heaven",artist:"Led Zeppelin",ytId:"QkF3oxziUI4"},
    {title:"Sweet Child O' Mine",artist:"Guns N' Roses",ytId:"1w7OgIMMRc4"},
    {title:"November Rain",artist:"Guns N' Roses",ytId:"8SbUC-UaAxE"},
    {title:"Eye of the Tiger",artist:"Survivor",ytId:"btPJPFnesV4"},
    {title:"Livin' on a Prayer",artist:"Bon Jovi",ytId:"lDK9QqIzhwk"},
    {title:"Purple Rain",artist:"Prince",ytId:"TvnYmWpD_T8"},
    {title:"We Will Rock You",artist:"Queen",ytId:"-tJYN-eG1zk"},
    {title:"Dream On",artist:"Aerosmith",ytId:"89dGtCN_cPg"},
    {title:"Should I Stay or Should I Go",artist:"The Clash",ytId:"BN1WwnEDWAM"},
    {title:"Sultans of Swing",artist:"Dire Straits",ytId:"0fAQhSRLQnM"},
    {title:"With or Without You",artist:"U2",ytId:"ujNeHIo9dAU"},
    {title:"Jump",artist:"Van Halen",ytId:"SwYN7mTi6HM"}
  ],
  "Nostalgic":[
    {title:"Take On Me",artist:"a-ha",ytId:"djV11Xbc914"},
    {title:"Africa",artist:"Toto",ytId:"FTQbiNvZqaY"},
    {title:"Don't You (Forget About Me)",artist:"Simple Minds",ytId:"CdqoNKCCt7A"},
    {title:"Every Breath You Take",artist:"The Police",ytId:"OMOGaugKpzs"},
    {title:"Girls Just Want to Have Fun",artist:"Cyndi Lauper",ytId:"PIb6AZdTr-A"},
    {title:"99 Luftballons",artist:"Nena",ytId:"La4Dcd1aUcI"},
    {title:"Walking on Sunshine",artist:"Katrina & The Waves",ytId:"iPUmE-tne5U"},
    {title:"Wake Me Up Before You Go-Go",artist:"Wham!",ytId:"pITmCFYkWN8"},
    {title:"Summer of '69",artist:"Bryan Adams",ytId:"9f06QZCVUHg"},
    {title:"Sweet Home Alabama",artist:"Lynyrd Skynyrd",ytId:"ye5BuYf8q4o"},
    {title:"Piano Man",artist:"Billy Joel",ytId:"gxEPV4kolz0"},
    {title:"Hotel California",artist:"Eagles",ytId:"BciS5krYL80"},
    {title:"Come On Eileen",artist:"Dexys Midnight Runners",ytId:"qpbIaE5Bhdk"},
    {title:"Kokomo",artist:"The Beach Boys",ytId:"pAwR6C82TCI"}
  ]
};

// ── MOOD TEST DATA ─────────────────────────────────────────────────────────────
const QUESTIONS = {
  uz:[
    {text:"Hozir ichingizdagi qaysi emotsiya birinchi o'rinda turibdi?",opts:[
      {key:"A",label:"😤 Jahl, asabiylik yoki stress",sub:"Hamma narsa asabga tegyapti"},
      {key:"B",label:"⚡ Energiya to'lib-toshayapti",sub:"Harakat qilgim kelyapti"},
      {key:"C",label:"😴 Charchoq va bo'shashish",sub:"Miyaga sokinlik kerak"},
      {key:"D",label:"🌙 Zerikish yoki mayuslik",sub:"Xayol surish kayfiyati"}
    ]},
    {text:"Sizga hozir qanday ritm (sur'at) kerak?",opts:[
      {key:"A",label:"💥 Juda tez va shovqinli",sub:""},
      {key:"B",label:"🕺 Ritmli, sho'x",sub:"Lekin asabga tegmaydigan"},
      {key:"C",label:"〰️ Bir tekisda ketadigan",sub:"Sokin fon"},
      {key:"D",label:"🌊 Sekin va mayin",sub:""}
    ]},
    {text:"Qo'shiqda so'zlar bo'lishi shartmi?",opts:[
      {key:"A",label:"🔥 Farqi yo'q",sub:"Asosiysi drayv bo'lsa bo'ldi"},
      {key:"B",label:"🎉 Ha, sho'x so'zlar",sub:"Qo'shilib aytishga oson"},
      {key:"C",label:"🎹 Umuman bo'lmasin",sub:"Yoki chet tilida, tushunarsiz"},
      {key:"D",label:"📖 Ha, ma'noli chuqur so'zlar",sub:""}
    ]},
    {text:"Musiqa sizni hozir qayerga yetaklashi kerak?",opts:[
      {key:"A",label:"💢 Negativni tashqariga chiqarishga",sub:"Baqirib-chaqirib"},
      {key:"B",label:"💃 To'g'ri raqs maydonchasiga",sub:"Divandan turib ketishga"},
      {key:"C",label:"🛋️ Divanga yotib dam olishga",sub:"Ko'zni yumib"},
      {key:"D",label:"💭 Shirin xayollarga",sub:"O'tmish yoki kelajak haqida"}
    ]}
  ],
  ru:[
    {text:"Какая эмоция сейчас у вас на первом месте?",opts:[
      {key:"A",label:"😤 Злость, раздражение или стресс",sub:"Всё достало"},
      {key:"B",label:"⚡ Переполняет энергия",sub:"Хочется действовать"},
      {key:"C",label:"😴 Усталость и расслабленность",sub:"Нужен покой"},
      {key:"D",label:"🌙 Скука или лёгкая грусть",sub:"Настрой на мечты"}
    ]},
    {text:"Какой темп нужен прямо сейчас?",opts:[
      {key:"A",label:"💥 Очень быстрый и громкий",sub:""},
      {key:"B",label:"🕺 Ритмичный, весёлый",sub:"Но не раздражающий"},
      {key:"C",label:"〰️ Равномерный, спокойный фон",sub:""},
      {key:"D",label:"🌊 Медленный и мягкий",sub:""}
    ]},
    {text:"Нужны ли слова в песне?",opts:[
      {key:"A",label:"🔥 Неважно",sub:"Главное — драйв"},
      {key:"B",label:"🎉 Да, весёлые слова",sub:"Чтобы подпевать"},
      {key:"C",label:"🎹 Нет, без слов",sub:"Или на непонятном языке"},
      {key:"D",label:"📖 Да, глубокие и смысловые",sub:""}
    ]},
    {text:"Куда должна привести тебя музыка?",opts:[
      {key:"A",label:"💢 Выплеснуть весь негатив",sub:"Кричать и бесноваться"},
      {key:"B",label:"💃 Прямо на танцпол",sub:"Встать с дивана"},
      {key:"C",label:"🛋️ Лечь и отдохнуть",sub:"Закрыть глаза"},
      {key:"D",label:"💭 В сладкие мечты",sub:"О прошлом или будущем"}
    ]}
  ],
  en:[
    {text:"Which emotion is on top right now?",opts:[
      {key:"A",label:"😤 Anger, irritation or stress",sub:"Everything is getting on my nerves"},
      {key:"B",label:"⚡ Bursting with energy",sub:"I want to move"},
      {key:"C",label:"😴 Tired and relaxed",sub:"Need some quiet"},
      {key:"D",label:"🌙 Boredom or mild sadness",sub:"Daydreaming mood"}
    ]},
    {text:"What kind of tempo do you need right now?",opts:[
      {key:"A",label:"💥 Very fast and loud",sub:""},
      {key:"B",label:"🕺 Rhythmic and upbeat",sub:"But not overwhelming"},
      {key:"C",label:"〰️ Steady, calm background",sub:""},
      {key:"D",label:"🌊 Slow and gentle",sub:""}
    ]},
    {text:"Do you need lyrics in the song?",opts:[
      {key:"A",label:"🔥 Doesn't matter",sub:"As long as it has drive"},
      {key:"B",label:"🎉 Yes, fun lyrics to sing along",sub:""},
      {key:"C",label:"🎹 No lyrics at all",sub:"Or in a foreign language"},
      {key:"D",label:"📖 Yes, deep and meaningful",sub:""}
    ]},
    {text:"Where should the music take you right now?",opts:[
      {key:"A",label:"💢 Release all the negativity",sub:"Scream it out"},
      {key:"B",label:"💃 Straight to the dance floor",sub:"Get off the couch"},
      {key:"C",label:"🛋️ Lie down and rest",sub:"Close your eyes"},
      {key:"D",label:"💭 Into sweet daydreams",sub:"About past or future"}
    ]}
  ]
};

const RESULTS = {
  uz:{
    A:{vibe:"Asabga qarshi dori",icon:"🔥",desc:"Siz hozir portlash arafasidasiz. Ikkita yo'l bor: energiyani chiqarib yuborish yoki tinchlanish.",genres:["Phonk","Heavy Metal","Lo-Fi Ambient","Dark Techno"],
      tracks:[{title:"DEAF KEV - Invincible",artist:"DEAF KEV",ytId:"J2X5mJ3HDYE"},{title:"Night Lovell - Dark Light",artist:"Night Lovell",ytId:"j-_7hqnHMbE"},{title:"Freddie Dredd - Gottage Inn",artist:"Freddie Dredd",ytId:"JhFbRBfqkbg"},{title:"Three Days Grace - I Hate Everything About You",artist:"Three Days Grace",ytId:"nRmAEgIpGiU"},{title:"Linkin Park - In The End",artist:"Linkin Park",ytId:"eVTXPUF4Oz4"},{title:"Linkin Park - Numb",artist:"Linkin Park",ytId:"kXYiU_JCYtU"},{title:"Disturbed - Down With The Sickness",artist:"Disturbed",ytId:"08dn6eNpTX4"},{title:"Rage Against The Machine - Killing In The Name",artist:"RATM",ytId:"bWXazVeVnYA"},{title:"System Of A Down - Chop Suey",artist:"System Of A Down",ytId:"CSvFpBOe8eY"},{title:"Slipknot - Wait And Bleed",artist:"Slipknot",ytId:"sSFTMbGlRY8"}]},
    B:{vibe:"Raqs va Kayfiyat",icon:"💃",desc:"Energiya bor, lekin qo'shiq yo'q. Ssenariy emas — faqat raqs va quvnoqlik.",genres:["Dance Pop","Club Music","Uzbek Pop","Remix"],
      tracks:[{title:"Dua Lipa - Levitating",artist:"Dua Lipa",ytId:"TUVcZfQe-Kw"},{title:"Bruno Mars - Uptown Funk",artist:"Bruno Mars ft. Mark Ronson",ytId:"OPf0YbXqDm0"},{title:"The Weeknd - Blinding Lights",artist:"The Weeknd",ytId:"4NRXx6U8ABQ"},{title:"Dua Lipa - Don't Start Now",artist:"Dua Lipa",ytId:"oygrmKOqttA"},{title:"Harry Styles - As It Was",artist:"Harry Styles",ytId:"H5v3kku4y6Q"},{title:"Calvin Harris - Summer",artist:"Calvin Harris",ytId:"ebXbLfLACGM"},{title:"Kygo - Firestone",artist:"Kygo ft. Conrad",ytId:"9Sc-ir2UwGU"},{title:"Avicii - Wake Me Up",artist:"Avicii",ytId:"IcrbM1l_BoI"},{title:"Martin Garrix - Animals",artist:"Martin Garrix",ytId:"gCYcHz2k5x0"},{title:"Ariana Grande - 7 rings",artist:"Ariana Grande",ytId:"QYh6mYIJG2Y"}]},
    C:{vibe:"Miyaga Perekur",icon:"🧠",desc:"Ishdan, o'qishdan yoki odamlardan charchagansiz. Miyani yuklamaydigan, shunchaki yoqimli fon kerak.",genres:["Lo-Fi Hip-Hop","Deep House","Mayin Jazz","Ambient"],
      tracks:[{title:"Lofi Girl - Chill Beats to Study",artist:"Lofi Girl",ytId:"jfKfPfyJRdk"},{title:"ChilledCow - Sleepy Fish",artist:"Sleepy Fish",ytId:"UiTBNVHUGbc"},{title:"Norah Jones - Don't Know Why",artist:"Norah Jones",ytId:"tO4dxvguQDk"},{title:"Nujabes - Feather",artist:"Nujabes",ytId:"RKoriT3NNOE"},{title:"J Dilla - So Far to Go",artist:"J Dilla",ytId:"jfJnMDdKgY0"},{title:"Bonobo - Kong",artist:"Bonobo",ytId:"7GF3Gg7IUi0"},{title:"Tycho - Awake",artist:"Tycho",ytId:"lAb-xDIXv6c"},{title:"Washed Out - Feel It All Around",artist:"Washed Out",ytId:"Tc0oJPJGSmo"},{title:"Still Woozy - Goodie Bag",artist:"Still Woozy",ytId:"oVvDKpS7Tj4"},{title:"Rex Orange County - Corduroy Dreams",artist:"Rex Orange County",ytId:"g9foCk25Y5Y"}]},
    D:{vibe:"Lirika / Sokinlik",icon:"🌙",desc:"Bir oz yolg'izlik yoki sokin hayotiy kayfiyat. Naushnikda yolg'iz eshitiladigan treklar.",genres:["Indie Folk","Acoustic","Soul","Sad Pop"],
      tracks:[{title:"Billie Eilish - When The Party's Over",artist:"Billie Eilish",ytId:"pbMwTqkKSps"},{title:"The Weeknd - Call Out My Name",artist:"The Weeknd",ytId:"P9t9jHus3EU"},{title:"Lewis Capaldi - Someone You Loved",artist:"Lewis Capaldi",ytId:"zABZyAoxXqk"},{title:"Olivia Rodrigo - drivers license",artist:"Olivia Rodrigo",ytId:"ZmDBbnmKpqQ"},{title:"Sufjan Stevens - Death With Dignity",artist:"Sufjan Stevens",ytId:"lN0uOKPxGcE"},{title:"Phoebe Bridgers - Motion Sickness",artist:"Phoebe Bridgers",ytId:"GwLMDpbHvSY"},{title:"Bon Iver - Skinny Love",artist:"Bon Iver",ytId:"ssdgMomZqMI"},{title:"Hozier - Take Me To Church",artist:"Hozier",ytId:"PVjiKRfKpPI"},{title:"Ed Sheeran - The A Team",artist:"Ed Sheeran",ytId:"UAWcs5H-qgQ"},{title:"Damien Rice - The Blower's Daughter",artist:"Damien Rice",ytId:"RWJ8TqLMeAo"}]}
  }
};
RESULTS.ru={
  A:{...RESULTS.uz.A,vibe:"Антидот от стресса",desc:"Вы сейчас на грани взрыва. Два пути: выплеснуть или успокоиться."},
  B:{...RESULTS.uz.B,vibe:"Танцы и кайф",desc:"Энергия есть, а музыки — нет. Никаких сценариев, только танец."},
  C:{...RESULTS.uz.C,vibe:"Перекур для мозга",desc:"Устали от работы, учёбы или людей. Нужен приятный, ненавязчивый фон."},
  D:{...RESULTS.uz.D,vibe:"Лирика / Тишина",desc:"Немного одиноко или тихое жизненное настроение. Треки для наушников в одиночестве."}
};
RESULTS.en={
  A:{...RESULTS.uz.A,vibe:"Stress Antidote",desc:"You're on the verge of exploding. Two paths: release it or calm down."},
  B:{...RESULTS.uz.B,vibe:"Dance & Vibes",desc:"Energy is here, music is not. No script — just pure dance."},
  C:{...RESULTS.uz.C,vibe:"Brain Break",desc:"Tired of work, study or people. Just need a pleasant, non-demanding background."},
  D:{...RESULTS.uz.D,vibe:"Lyrics & Silence",desc:"A little lonely or quiet life mood. Tracks for headphones, alone."}
};

const LANG_TEXT = {
  uz:{trending:"🔥 Trending hozir — bosing va tinglang",q:"Savol",of:"dan",restart:"🔄 Qaytadan boshlash",songs:"🎧 Siz uchun qo'shiqlar",moodDivider:"🎭 Kayfiyat Testi",infoTitle:"Music Info Assistant",infoSub:"Artist, albom yoki qo'shiq haqida biror narsa so'rang.",infoPlaceholder:"Artist, albom yoki qo'shiq nomi..."},
  ru:{trending:"🔥 Сейчас в тренде — нажмите и слушайте",q:"Вопрос",of:"из",restart:"🔄 Начать заново",songs:"🎧 Треки для вас",moodDivider:"🎭 Тест настроения",infoTitle:"Music Info Assistant",infoSub:"Ask about any artist, album or song.",infoPlaceholder:"Имя артиста, альбома или песни..."},
  en:{trending:"🔥 Trending Now — click and listen",q:"Question",of:"of",restart:"🔄 Start Over",songs:"🎧 Songs for you",moodDivider:"🎭 Mood Test",infoTitle:"Music Info Assistant",infoSub:"Artist, albom yoki qo'shiq haqida so'rang.",infoPlaceholder:"Artist, album or song name..."}
};

// ── MUSIC DB ──────────────────────────────────────────────────────────────────
const MUSIC_DB = [
{name:"The Weeknd",aliases:["the weeknd","weeknd","уикенд"],emoji:"🌃",photo:"https://img.youtube.com/vi/4NRXx6U8ABQ/mqdefault.jpg",tagline:"Kanadalik R&B/Pop yulduzi, 'Blinding Lights' ijrochisi",facts:[{key:"Janr",val:"R&B, Pop, Synth-pop"},{key:"Mamlakat",val:"Kanada"},{key:"Faoliyati",val:"2010 - hozirgacha"}],sections:[{title:"Biografiya",icon:"📖",type:"prose",content:"Abel Tesfaye (The Weeknd) - zamonaviy R&B sohasidagi eng katta yulduzlardan biri. Uning 80-yillar sintipopiga yaqin uslubi butun dunyo bo'ylab milliardlab tinglashlarga ega bo'ldi."},{title:"Albomlar",icon:"💿",type:"albums",content:[{name:"Beauty Behind the Madness",year:"2015"},{name:"Starboy",year:"2016"},{name:"After Hours",year:"2020"},{name:"Dawn FM",year:"2022"}]},{title:"Top qo'shiqlar",icon:"🎵",type:"tracks",content:[{title:"Blinding Lights",ytId:"4NRXx6U8ABQ"},{title:"Starboy",ytId:"34Na4j8AVgA"},{title:"The Hills",ytId:"yzTuBuRdAyA"},{title:"Can't Feel My Face",ytId:"KEI4qSrkPAs"},{title:"Save Your Tears",ytId:"XXYlFuWEuKI"}]}],summary:"The Weeknd zamonaviy pop/R&B sahnasidagi eng nufuzli ijrochilardan biri hisoblanadi."},
{name:"Drake",aliases:["drake","дрейк"],emoji:"🦉",photo:"https://img.youtube.com/vi/xpVfcZ0ZcFM/mqdefault.jpg",tagline:"Kanadalik rap yulduzi, hip-hop sohasining eng ko'p sotuvchi artistlaridan biri",facts:[{key:"Janr",val:"Hip-Hop, R&B, Rap"},{key:"Mamlakat",val:"Kanada"},{key:"Faoliyati",val:"2006 - hozirgacha"}],sections:[{title:"Biografiya",icon:"📖",type:"prose",content:"Drake zamonaviy hip-hop sanoatining eng muvaffaqiyatli va eng ko'p Billboard rekordlarini o'rnatgan artistlaridan biri."},{title:"Albomlar",icon:"💿",type:"albums",content:[{name:"Take Care",year:"2011"},{name:"Views",year:"2016"},{name:"Scorpion",year:"2018"},{name:"Certified Lover Boy",year:"2021"}]},{title:"Top qo'shiqlar",icon:"🎵",type:"tracks",content:[{title:"God's Plan",ytId:"xpVfcZ0ZcFM"},{title:"One Dance",ytId:"iHCn3a3YIOU"},{title:"Hotline Bling",ytId:"uxpDa-c-4Mc"},{title:"In My Feelings",ytId:"DRS_PpOrUZ4"},{title:"Started From the Bottom",ytId:"RubczQuh47k"}]}],summary:"Drake hip-hop sanoatining eng nufuzli va ta'sirli figuralaridan biri."},
{name:"Taylor Swift",aliases:["taylor swift","тейлор свифт"],emoji:"🎀",photo:"https://img.youtube.com/vi/nfWlot6h_JM/mqdefault.jpg",tagline:"Amerikalik pop/country yulduzi va eng ko'p mukofotga ega qo'shiqchi",facts:[{key:"Janr",val:"Pop, Country, Folk-pop"},{key:"Mamlakat",val:"AQSH"},{key:"Faoliyati",val:"2006 - hozirgacha"}],sections:[{title:"Biografiya",icon:"📖",type:"prose",content:"Taylor Swift country sahnasidan boshlab, keyinchalik pop musiqaning eng yirik yulduziga aylangan."},{title:"Albomlar",icon:"💿",type:"albums",content:[{name:"1989",year:"2014"},{name:"Reputation",year:"2017"},{name:"Folklore",year:"2020"},{name:"Midnights",year:"2022"}]},{title:"Top qo'shiqlar",icon:"🎵",type:"tracks",content:[{title:"Shake It Off",ytId:"nfWlot6h_JM"},{title:"Blank Space",ytId:"e-ORhEE9VVg"},{title:"Anti-Hero",ytId:"b1kbLwvqugk"},{title:"Love Story",ytId:"8xg3vE8Ie_E"},{title:"Cruel Summer",ytId:"ic8j13piAhQ"}]}],summary:"Taylor Swift zamonaviy pop musiqaning eng nufuzli va ta'sirchan ijrochisi hisoblanadi."},
{name:"Ed Sheeran",aliases:["ed sheeran","эд ширан"],emoji:"🎸",photo:"https://img.youtube.com/vi/JGwWNGJdvx8/mqdefault.jpg",tagline:"Britaniyalik pop/akustik gitara qo'shiqchisi va bastakor",facts:[{key:"Janr",val:"Pop, Folk-pop, Acoustic"},{key:"Mamlakat",val:"Buyuk Britaniya"},{key:"Faoliyati",val:"2011 - hozirgacha"}],sections:[{title:"Biografiya",icon:"📖",type:"prose",content:"Ed Sheeran gitara bilan kontsert berishdan boshlab, dunyo bo'ylab eng ko'p sotuvchi pop artistlardan biriga aylandi."},{title:"Albomlar",icon:"💿",type:"albums",content:[{name:"+ (Plus)",year:"2011"},{name:"x (Multiply)",year:"2014"},{name:"÷ (Divide)",year:"2017"},{name:"= (Equals)",year:"2021"}]},{title:"Top qo'shiqlar",icon:"🎵",type:"tracks",content:[{title:"Shape of You",ytId:"JGwWNGJdvx8"},{title:"Perfect",ytId:"2Vv-BfVoq4g"},{title:"Thinking Out Loud",ytId:"lp-EO5I60KA"},{title:"Photograph",ytId:"nSDgHBxUbVQ"},{title:"Bad Habits",ytId:"orJSJGHjBLI"}]}],summary:"Ed Sheeran zamonaviy pop musiqaning eng yumshoq va ommabop ovozlaridan biri."},
{name:"Adele",aliases:["adele","адель"],emoji:"🎤",photo:"https://img.youtube.com/vi/rYEDA3JcQqw/mqdefault.jpg",tagline:"Britaniyalik soul/pop qo'shiqchisi, kuchli vokal ovozi bilan tanilgan",facts:[{key:"Janr",val:"Soul, Pop, Ballad"},{key:"Mamlakat",val:"Buyuk Britaniya"},{key:"Faoliyati",val:"2006 - hozirgacha"}],sections:[{title:"Biografiya",icon:"📖",type:"prose",content:"Adele o'zining kuchli va his-tuyg'uga boy ovozi bilan butun dunyoda tanilgan."},{title:"Albomlar",icon:"💿",type:"albums",content:[{name:"19",year:"2008"},{name:"21",year:"2011"},{name:"25",year:"2015"},{name:"30",year:"2021"}]},{title:"Top qo'shiqlar",icon:"🎵",type:"tracks",content:[{title:"Rolling in the Deep",ytId:"rYEDA3JcQqw"},{title:"Someone Like You",ytId:"hLQl3WQQoQ0"},{title:"Hello",ytId:"YQHsXMglC9A"},{title:"Set Fire to the Rain",ytId:"Ri7-vnrJD3k"},{title:"Easy on Me",ytId:"U3ASj1L6_sY"}]}],summary:"Adele zamonaviy soul-pop musiqaning eng kuchli ovozlaridan biri sifatida tanilgan."},
{name:"Billie Eilish",aliases:["billie eilish","билли айлиш"],emoji:"🖤",photo:"https://img.youtube.com/vi/DyDfgMOUjCI/mqdefault.jpg",tagline:"Amerikalik pop yulduzi, alternativ va minimalistik uslubi bilan tanilgan",facts:[{key:"Janr",val:"Pop, Alternative, Electropop"},{key:"Mamlakat",val:"AQSH"},{key:"Faoliyati",val:"2015 - hozirgacha"}],sections:[{title:"Biografiya",icon:"📖",type:"prose",content:"Billie Eilish o'zining shivirlovchi vokal uslubi va qoraygan, alternativ pop sound'i bilan yosh avlod orasida juda mashhur bo'ldi."},{title:"Albomlar",icon:"💿",type:"albums",content:[{name:"When We All Fall Asleep, Where Do We Go?",year:"2019"},{name:"Happier Than Ever",year:"2021"},{name:"Hit Me Hard and Soft",year:"2024"}]},{title:"Top qo'shiqlar",icon:"🎵",type:"tracks",content:[{title:"Bad Guy",ytId:"DyDfgMOUjCI"},{title:"Ocean Eyes",ytId:"viimfQi_pUw"},{title:"Happier Than Ever",ytId:"5GJWxDKyk3A"},{title:"Birds of a Feather",ytId:"_XYLD-gOe0I"},{title:"Lovely",ytId:"AKlqpxFtS2k"}]}],summary:"Billie Eilish zamonaviy alternativ pop sohasining eng noyob ovozlaridan biri."},
{name:"Ariana Grande",aliases:["ariana grande","ариана гранде"],emoji:"🎀",photo:"https://img.youtube.com/vi/gl1aHhXnN1k/mqdefault.jpg",tagline:"Amerikalik pop/R&B qo'shiqchisi, keng diapazonli ovozi bilan tanilgan",facts:[{key:"Janr",val:"Pop, R&B"},{key:"Mamlakat",val:"AQSH"},{key:"Faoliyati",val:"2008 - hozirgacha"}],sections:[{title:"Biografiya",icon:"📖",type:"prose",content:"Ariana Grande aktrisalikdan musiqaga o'tib, zamonaviy pop musiqaning yetakchi ovozlaridan biriga aylandi."},{title:"Albomlar",icon:"💿",type:"albums",content:[{name:"Dangerous Woman",year:"2016"},{name:"Sweetener",year:"2018"},{name:"Thank U, Next",year:"2019"},{name:"Eternal Sunshine",year:"2024"}]},{title:"Top qo'shiqlar",icon:"🎵",type:"tracks",content:[{title:"Thank U, Next",ytId:"gl1aHhXnN1k"},{title:"7 Rings",ytId:"QYh6mYIJG2Y"},{title:"No Tears Left to Cry",ytId:"ffxKSjUwKdU"},{title:"Problem",ytId:"iS1g8G_njx8"},{title:"Positions",ytId:"tcYodQoapMg"}]}],summary:"Ariana Grande zamonaviy pop-R&B sohasining eng kuchli vokalchilaridan biri."},
{name:"Eminem",aliases:["eminem","эминем","marshall mathers"],emoji:"🎤",photo:"https://img.youtube.com/vi/_Yhyp-_hX2s/mqdefault.jpg",tagline:"Amerikalik rap legendasi, tarixdagi eng ko'p sotilgan reperlardan biri",facts:[{key:"Janr",val:"Hip-Hop, Rap"},{key:"Mamlakat",val:"AQSH"},{key:"Faoliyati",val:"1996 - hozirgacha"}],sections:[{title:"Biografiya",icon:"📖",type:"prose",content:"Eminem tezkor va texnik jihatdan murakkab rep uslubi bilan hip-hop tarixidagi eng nufuzli artistlardan biriga aylandi."},{title:"Albomlar",icon:"💿",type:"albums",content:[{name:"The Marshall Mathers LP",year:"2000"},{name:"The Eminem Show",year:"2002"},{name:"Recovery",year:"2010"},{name:"Curtain Call",year:"2005"}]},{title:"Top qo'shiqlar",icon:"🎵",type:"tracks",content:[{title:"Lose Yourself",ytId:"_Yhyp-_hX2s"},{title:"Not Afraid",ytId:"j5-yKhDd64s"},{title:"Stan",ytId:"gOMhN-hfMtY"},{title:"Without Me",ytId:"YVkUvmDQ3HY"},{title:"Love the Way You Lie",ytId:"uelHwf8o7_U"}]}],summary:"Eminem hip-hop tarixidagi eng texnik va ta'sirli reperlardan biri hisoblanadi."},
{name:"Beyoncé",aliases:["beyonce","beyoncé","бейонсе"],emoji:"👑",photo:"https://img.youtube.com/vi/bnVUHWCynig/mqdefault.jpg",tagline:"Amerikalik R&B/Pop qirolichasi, Grammy mukofotlarining rekordchisi",facts:[{key:"Janr",val:"R&B, Pop, Soul"},{key:"Mamlakat",val:"AQSH"},{key:"Faoliyati",val:"1997 - hozirgacha"}],sections:[{title:"Biografiya",icon:"📖",type:"prose",content:"Beyoncé Destiny's Child guruhidan boshlab, mustaqil ravishda zamonaviy R&B va pop musiqaning eng nufuzli ovozlaridan biriga aylandi."},{title:"Albomlar",icon:"💿",type:"albums",content:[{name:"Dangerously in Love",year:"2003"},{name:"Lemonade",year:"2016"},{name:"Renaissance",year:"2022"},{name:"Cowboy Carter",year:"2024"}]},{title:"Top qo'shiqlar",icon:"🎵",type:"tracks",content:[{title:"Halo",ytId:"bnVUHWCynig"},{title:"Single Ladies",ytId:"4m1EFMoRFvY"},{title:"Crazy in Love",ytId:"ViwtNLUqkMY"},{title:"Formation",ytId:"WDZJPJV__bQ"},{title:"Texas Hold 'Em",ytId:"SdMODhMlyMY"}]}],summary:"Beyoncé zamonaviy musiqa sanoatining eng nufuzli va ko'p mukofotlangan yulduzlaridan biri."},
{name:"Michael Jackson",aliases:["michael jackson","майкл джексон"],emoji:"🕺",photo:"https://img.youtube.com/vi/Zi_XLOBDo_Y/mqdefault.jpg",tagline:"'Pop qiroli' nomi bilan tanilgan, musiqa tarixidagi eng ta'sirli san'atkor",facts:[{key:"Janr",val:"Pop, R&B, Funk"},{key:"Mamlakat",val:"AQSH"},{key:"Faoliyati",val:"1964-2009"}],sections:[{title:"Biografiya",icon:"📖",type:"prose",content:"Michael Jackson Jackson 5 guruhidan boshlab, dunyo tarixidagi eng katta sotuvchi va eng ta'sirli pop ijrochisiga aylandi. Uning raqs uslubi va video-kliplari musiqa sanoatini o'zgartirdi."},{title:"Albomlar",icon:"💿",type:"albums",content:[{name:"Off the Wall",year:"1979"},{name:"Thriller",year:"1982"},{name:"Bad",year:"1987"},{name:"Dangerous",year:"1991"}]},{title:"Top qo'shiqlar",icon:"🎵",type:"tracks",content:[{title:"Billie Jean",ytId:"Zi_XLOBDo_Y"},{title:"Thriller",ytId:"sOnqjkJTMaA"},{title:"Beat It",ytId:"oRdxUFDoQe0"},{title:"Smooth Criminal",ytId:"h_D3VFfhvs4"},{title:"Man in the Mirror",ytId:"PivWY9wn5ps"}]}],summary:"Michael Jackson 'Pop qiroli' sifatida musiqa tarixiga abadiy muhrlangan."},
{name:"Bruno Mars",aliases:["bruno mars","бруно марс"],emoji:"🎩",photo:"https://img.youtube.com/vi/OPf0YbXqDm0/mqdefault.jpg",tagline:"Amerikalik pop/funk qo'shiqchisi, sahna mahorati va retro uslubi bilan tanilgan",facts:[{key:"Janr",val:"Pop, Funk, R&B"},{key:"Mamlakat",val:"AQSH"},{key:"Faoliyati",val:"2004 - hozirgacha"}],sections:[{title:"Biografiya",icon:"📖",type:"prose",content:"Bruno Mars zamonaviy pop musiqaga 70-80-yillar funk va soul uslublarini qaytargan ijrochi."},{title:"Albomlar",icon:"💿",type:"albums",content:[{name:"Doo-Wops & Hooligans",year:"2010"},{name:"Unorthodox Jukebox",year:"2012"},{name:"24K Magic",year:"2016"}]},{title:"Top qo'shiqlar",icon:"🎵",type:"tracks",content:[{title:"Uptown Funk",ytId:"OPf0YbXqDm0"},{title:"24K Magic",ytId:"UqyT8IEBkvY"},{title:"Just the Way You Are",ytId:"LjhCEhWiKXk"},{title:"That's What I Like",ytId:"PMivT7MJ41M"},{title:"Grenade",ytId:"XjVNlgyjcpM"}]}],summary:"Bruno Mars zamonaviy pop-funk uslubining eng ko'zga ko'ringan vakili."},
{name:"Coldplay",aliases:["coldplay","колдплей"],emoji:"🌈",photo:"https://img.youtube.com/vi/dvgZkm1xWPE/mqdefault.jpg",tagline:"Britaniyalik rok guruhi, dunyoda eng ko'p tinglanadigan jamoalardan biri",facts:[{key:"Janr",val:"Alternative Rock, Pop Rock"},{key:"Mamlakat",val:"Buyuk Britaniya"},{key:"Faoliyati",val:"1996 - hozirgacha"}],sections:[{title:"Biografiya",icon:"📖",type:"prose",content:"Coldplay - Chris Martin boshchiligidagi guruh, ularning musiqasi keng auditoriyaga ega va katta stadion kontsertlari bilan mashhur."},{title:"Albomlar",icon:"💿",type:"albums",content:[{name:"Parachutes",year:"2000"},{name:"A Rush of Blood to the Head",year:"2002"},{name:"Viva la Vida",year:"2008"},{name:"Music of the Spheres",year:"2021"}]},{title:"Top qo'shiqlar",icon:"🎵",type:"tracks",content:[{title:"Yellow",ytId:"yKNxeF4KMsY"},{title:"Viva la Vida",ytId:"dvgZkm1xWPE"},{title:"The Scientist",ytId:"RB-RcX5DS5A"},{title:"Paradise",ytId:"1G4isv_Fylg"},{title:"Hymn for the Weekend",ytId:"YykjpeuMNEk"}]}],summary:"Coldplay dunyodagi eng katta stadion-rok guruhlaridan biri hisoblanadi."},
{name:"Imagine Dragons",aliases:["imagine dragons","имеджин драгонс"],emoji:"🐉",photo:"https://img.youtube.com/vi/W2TE0DjdNqI/mqdefault.jpg",tagline:"Amerikalik rok guruhi, anthem-uslubdagi xitlari bilan tanilgan",facts:[{key:"Janr",val:"Alternative Rock, Pop Rock, Electronic"},{key:"Mamlakat",val:"AQSH"},{key:"Faoliyati",val:"2008 - hozirgacha"}],sections:[{title:"Biografiya",icon:"📖",type:"prose",content:"Imagine Dragons rok va elektron musiqani birlashtirib, kuchli, energetik va keng auditoriyaga mos qo'shiqlar yaratadi."},{title:"Albomlar",icon:"💿",type:"albums",content:[{name:"Night Visions",year:"2012"},{name:"Evolve",year:"2017"},{name:"Mercury - Act 1",year:"2021"},{name:"Mercury - Act 2",year:"2022"}]},{title:"Top qo'shiqlar",icon:"🎵",type:"tracks",content:[{title:"Believer",ytId:"W2TE0DjdNqI"},{title:"Radioactive",ytId:"ktvTqknDobU"},{title:"Thunder",ytId:"fKopy74weus"},{title:"Demons",ytId:"mWRsgZuwf_8"},{title:"Enemy",ytId:"D9G1VOjN_84"}]}],summary:"Imagine Dragons zamonaviy alternativ-pop-rok sohasining eng ommabop guruhlaridan biri."},
{name:"Dua Lipa",aliases:["dua lipa","дуа липа"],emoji:"✨",photo:"https://img.youtube.com/vi/DyHkM3YFQVY/mqdefault.jpg",tagline:"Britaniyalik pop/disko-pop yulduzi, retro-disko uyg'onishining yetakchisi",facts:[{key:"Janr",val:"Pop, Disco-pop, Dance"},{key:"Mamlakat",val:"Buyuk Britaniya"},{key:"Faoliyati",val:"2015 - hozirgacha"}],sections:[{title:"Biografiya",icon:"📖",type:"prose",content:"Dua Lipa zamonaviy pop musiqaga 70-80-yillar disko ta'sirini qaytargan eng yorqin ovozlardan biri."},{title:"Albomlar",icon:"💿",type:"albums",content:[{name:"Dua Lipa",year:"2017"},{name:"Future Nostalgia",year:"2020"},{name:"Radical Optimism",year:"2024"}]},{title:"Top qo'shiqlar",icon:"🎵",type:"tracks",content:[{title:"Levitating",ytId:"TUVcZfQe-Kw"},{title:"Don't Start Now",ytId:"oygrmKOqttA"},{title:"New Rules",ytId:"k2qgadSvNyU"},{title:"IDGAF",ytId:"DyHkM3YFQVY"},{title:"Houdini",ytId:"5OBDFaLCDzQ"}]}],summary:"Dua Lipa 2020-yillar pop-disko uyg'onishining yetakchi ovozi hisoblanadi."},
{name:"Rihanna",aliases:["rihanna","рианна"],emoji:"💎",photo:"https://img.youtube.com/vi/CvBqzbB9-rk/mqdefault.jpg",tagline:"Barbadoslik pop/R&B yulduzi, musiqa va biznes sohasida muvaffaqiyatli",facts:[{key:"Janr",val:"Pop, R&B, Dancehall"},{key:"Mamlakat",val:"Barbados"},{key:"Faoliyati",val:"2005 - hozirgacha"}],sections:[{title:"Biografiya",icon:"📖",type:"prose",content:"Rihanna 2000-yillar oxiri va 2010-yillarning eng muvaffaqiyatli pop yulduzlaridan biri bo'lib, keyinchalik Fenty brendi orqali biznes sohasida ham katta yutuqlarga erishdi."},{title:"Albomlar",icon:"💿",type:"albums",content:[{name:"Good Girl Gone Bad",year:"2007"},{name:"Loud",year:"2010"},{name:"Talk That Talk",year:"2011"},{name:"Anti",year:"2016"}]},{title:"Top qo'shiqlar",icon:"🎵",type:"tracks",content:[{title:"Umbrella",ytId:"CvBqzbB9-rk"},{title:"Diamonds",ytId:"lWA2pjMjpBs"},{title:"We Found Love",ytId:"tg00YEETFzg"},{title:"Work",ytId:"HL1UzIK-flA"},{title:"Stay",ytId:"JF8BRvqGCNs"}]}],summary:"Rihanna 2000-2010 yillar pop musiqasining eng muhim ovozlaridan biri hisoblanadi."},
{name:"Скриптонит",aliases:["скриптонит","scriptonite","адиль жалелов"],emoji:"🎙️",photo:"https://img.youtube.com/vi/lFYCMo3UGCY/mqdefault.jpg",tagline:"Qozoqstonlik reper/prodyuser, rus tilidagi hip-hop sahnasiga katta ta'sir ko'rsatgan",facts:[{key:"Janr",val:"Hip-Hop, Trip-hop"},{key:"Mamlakat",val:"Qozoqiston"},{key:"Faoliyati",val:"2010 - hozirgacha"}],sections:[{title:"Biografiya",icon:"📖",type:"prose",content:"Скриптонит (Adil Jalelov) Pavlodar shahridan bo'lib, o'ziga xos atmosferik prodyuserlik va melanxolik rep uslubi bilan butun MDH hududidagi hip-hop sahnasiga katta ta'sir ko'rsatgan."},{title:"Albomlar",icon:"💿",type:"albums",content:[{name:"Кто убил Марка?",year:"2014"},{name:"Праздник",year:"2017"}]},{title:"Top qo'shiqlar",icon:"🎵",type:"tracks",content:[{title:"Чёрный лексус"},{title:"Юность"},{title:"Иногда"},{title:"Слова"},{title:"Розовое вино"}]}],summary:"Скриптонит Qozoqistondan chiqqan, MDH hip-hop sahnasiga eng katta ta'sir ko'rsatgan reperlardan biri."},
{name:"BAKR",aliases:["bakr","бакр","bakar"],emoji:"🎙️",photo:"https://img.youtube.com/vi/Rn5GNpGSrMQ/mqdefault.jpg",tagline:"Qirg'izistonlik reper, qirg'iz trap va hip-hop sahnasining yorqin vakili",facts:[{key:"Janr",val:"Hip-Hop, Trap, Rap"},{key:"Mamlakat",val:"Qirg'iziston"},{key:"Faoliyati",val:"2015 - hozirgacha"},{key:"Til",val:"Qirg'iz, Rus"}],sections:[{title:"Biografiya",icon:"📖",type:"prose",content:"BAKR — Qirg'izistondan chiqqan zamonaviy trap va hip-hop ijrochisi. U qirg'iz va rus tillarida ijro etib, MDH yoshlari orasida katta muxlislar bazasini to'plagan."},{title:"Mashhur qo'shiqlar",icon:"🎵",type:"tracks",content:[{title:"BAKR - Пустота",ytId:"Rn5GNpGSrMQ"},{title:"BAKR - Больно"},{title:"BAKR - Холодно"},{title:"BAKR - Дорога"},{title:"BAKR - Небо"}]},{title:"Uslub",icon:"🎨",type:"tags",content:["Trap","Hip-Hop","Qirg'iz rap","MDH rap","Yoshlar"]}],summary:"BAKR Qirg'iziston rap sahnasining eng tanilgan vakili, MDH bo'ylab keng auditoriyaga ega ijrochi."},
{name:"Ulukmanapo",aliases:["ulukmanapo","улукманапо","улук"],emoji:"🎙️",photo:"https://img.youtube.com/vi/2K7PPMdFOq0/mqdefault.jpg",tagline:"Qirg'izistonlik rep/trap ijrochisi, MDH yoshlar orasida mashhur",facts:[{key:"Janr",val:"Rap, Trap, Hip-Hop"},{key:"Mamlakat",val:"Qirg'iziston"},{key:"Faoliyati",val:"2015 - hozirgacha"}],sections:[{title:"Biografiya",icon:"📖",type:"prose",content:"Ulukmanapo — qirg'iz trap va rep musiqasining eng yorqin vakili. Qirg'iz va rus tillarida ijro etib, ijtimoiy tarmoqlarda katta auditoriya to'plagan."},{title:"Mashhur qo'shiqlar",icon:"🎵",type:"tracks",content:[{title:"Бишкек",ytId:"2K7PPMdFOq0"},{title:"Улук",ytId:"dP1sSZZkDr4"},{title:"Асфальт",ytId:"XMh4GqWJVFk"},{title:"Мечта",ytId:"HVLyO2jAMiw"},{title:"Горы"}]},{title:"Uslub",icon:"🎨",type:"tags",content:["Trap","Qirg'iz rap","Street","Yoshlar","MDH rap"]}],summary:"Ulukmanapo qirg'iz rep sahnasida o'z yo'lini topgan va MDH bo'ylab tanilgan ijrochi."},
{name:"Земфира",aliases:["земфира","zemfira"],emoji:"🎸",photo:"https://img.youtube.com/vi/vTQXMRYol5E/mqdefault.jpg",tagline:"Rossiyalik rok qo'shiqchisi va bastakor, 90-2000-yillar rok sahnasining yetakchisi",facts:[{key:"Janr",val:"Alternative Rock"},{key:"Mamlakat",val:"Rossiya"},{key:"Faoliyati",val:"1999 - hozirgacha"}],sections:[{title:"Biografiya",icon:"📖",type:"prose",content:"Земфира rus tilidagi alternativ-rok sahnasining eng nufuzli ijrochilaridan biri."},{title:"Albomlar",icon:"💿",type:"albums",content:[{name:"Zemfira",year:"1999"},{name:"Прости меня моя любовь",year:"2000"},{name:"Спасибо",year:"2007"}]},{title:"Top qo'shiqlar",icon:"🎵",type:"tracks",content:[{title:"Хочешь?"},{title:"Аривидерчи"},{title:"Искала"},{title:"Сигареты"},{title:"Малыш"}]}],summary:"Земфира rus rok musiqasining eng nufuzli va ta'sirchan ovozlaridan biri."},
{name:"Моргенштерн",aliases:["моргенштерн","morgenshtern"],emoji:"🔥",photo:"https://img.youtube.com/vi/kKFiGSCMHkI/mqdefault.jpg",tagline:"Rossiyalik reper va shou-biznes yulduzi",facts:[{key:"Janr",val:"Hip-Hop, Trap"},{key:"Mamlakat",val:"Rossiya"},{key:"Faoliyati",val:"2017 - hozirgacha"}],sections:[{title:"Biografiya",icon:"📖",type:"prose",content:"Моргенштерн (Алишер Валеев) ijtimoiy tarmoqlardagi mashhurligi va provokatsion uslubi bilan rus trap-rep sahnasining eng yirik yulduzlaridan biriga aylandi."},{title:"Albomlar",icon:"💿",type:"albums",content:[{name:"Million Dollar: Original",year:"2021"}]},{title:"Top qo'shiqlar",icon:"🎵",type:"tracks",content:[{title:"Cadillac"},{title:"Show"},{title:"Bling-Bling"},{title:"Кто бы мог подумать"},{title:"Family"}]}],summary:"Моргенштерн 2020-yillar rus trap-rep madaniyatining eng ko'zga ko'ringan vakili."},
{name:"Баста",aliases:["баста","basta","ноггано"],emoji:"🎤",photo:"https://img.youtube.com/vi/jqQQnrF-Hyg/mqdefault.jpg",tagline:"Rossiyalik reper, rus hip-hop sahnasining faxriy vakillaridan biri",facts:[{key:"Janr",val:"Hip-Hop, Rap"},{key:"Mamlakat",val:"Rossiya"},{key:"Faoliyati",val:"2000 - hozirgacha"}],sections:[{title:"Biografiya",icon:"📖",type:"prose",content:"Баста (Василий Вакуленко) rus hip-hop sahnasining eng uzoq vaqt faoliyat ko'rsatib kelayotgan va hurmatga sazovor vakillaridan biri."},{title:"Top qo'shiqlar",icon:"🎵",type:"tracks",content:[{title:"Сансара"},{title:"Моя игра"},{title:"Любимый город"},{title:"Робот"},{title:"Шоу"}]}],summary:"Баста rus hip-hop tarixidagi eng obro'li va izchil ijrochilardan biri."},
{name:"Макс Корж",aliases:["макс корж","max korzh"],emoji:"🎸",tagline:"Belarusiyalik reper/qo'shiqchi, rus tilida ijro etadi",facts:[{key:"Janr",val:"Hip-Hop, Pop-rap"},{key:"Mamlakat",val:"Belarus"},{key:"Faoliyati",val:"2010 - hozirgacha"}],sections:[{title:"Biografiya",icon:"📖",type:"prose",content:"Макс Корж Belarusiyalik bo'lib, rus tilidagi pop-rep sahnasida juda katta muxlislar bazasiga ega, katta stadion kontsertlari bilan mashhur."},{title:"Top qo'shiqlar",icon:"🎵",type:"tracks",content:[{title:"Сэнсэй"},{title:"Гнев"},{title:"Розовое вино"},{title:"Огонь"},{title:"Иногда"}]}],summary:"Макс Корж rus tilidagi pop-rep sahnasining eng katta stadion yulduzlaridan biri."}
];

// ── STATE ─────────────────────────────────────────────────────────────────────
let currentLang = "uz";
let answers = [];
let testDone = false;

// ── LANG ──────────────────────────────────────────────────────────────────────
document.getElementById("lang-panel").addEventListener("click", e=>{
  const btn = e.target.closest(".lang-btn");
  if(!btn || btn.classList.contains("active")) return;
  document.querySelectorAll(".lang-btn").forEach(b=>b.classList.remove("active"));
  btn.classList.add("active");
  currentLang = btn.dataset.lang;
  const t = LANG_TEXT[currentLang];
  document.getElementById("trending-title").textContent = t.trending;
  document.getElementById("info-welcome-title").textContent = t.infoTitle;
  document.getElementById("info-welcome-sub").textContent = t.infoSub;
  document.getElementById("info-input").placeholder = t.infoPlaceholder;
  renderTest();
});

// ── PAGE NAV ──────────────────────────────────────────────────────────────────
document.querySelectorAll(".nav-tab").forEach(tab=>{
  tab.addEventListener("click",()=>{
    document.querySelectorAll(".nav-tab").forEach(t=>t.classList.remove("active"));
    document.querySelectorAll(".page").forEach(p=>p.classList.remove("active"));
    tab.classList.add("active");
    document.getElementById(tab.dataset.page).classList.add("active");
  });
});

// ── GENRE GRID ────────────────────────────────────────────────────────────────
function buildGrid(){
  const grid = document.getElementById("genre-grid");
  GENRES.forEach(g=>{
    const card = document.createElement("div");
    card.className = "genre-card";
    card.innerHTML = `
      <img class="genre-thumb" src="https://img.youtube.com/vi/${g.ytId}/mqdefault.jpg" alt="${g.track}"
        onerror="this.outerHTML='<div class=genre-thumb-placeholder>${g.icon}</div>'">
      <div class="genre-info">
        <div class="genre-label">${g.label}</div>
        <div class="genre-track">${g.track}</div>
        <div class="genre-artist">${g.artist}</div>
      </div>`;
    card.addEventListener("click",()=>openGenreModal(g));
    grid.appendChild(card);
  });
}

function openGenreModal(g){
  const songs = GENRE_SONGS[g.label]||[];
  document.getElementById("modal-genre-label").textContent = g.label;
  document.getElementById("modal-genre-title").innerHTML = `${g.icon} Top ${songs.length} Qo'shiqlar`;
  const list = document.getElementById("genre-modal-list");
  list.innerHTML = "";
  songs.forEach((s,i)=>{
    const el = document.createElement("a");
    el.className = "modal-track";
    el.href = `https://www.youtube.com/watch?v=${s.ytId}`;
    el.target = "_blank"; el.rel = "noopener noreferrer";
    el.innerHTML = `
      <div class="modal-track-num">${i+1}</div>
      <img class="modal-track-thumb" src="https://img.youtube.com/vi/${s.ytId}/mqdefault.jpg"
        onerror="this.outerHTML='<div class=modal-track-thumb-ph>🎵</div>'">
      <div class="modal-track-info">
        <div class="modal-track-title">${s.title}</div>
        <div class="modal-track-artist">${s.artist}</div>
      </div>
      <span class="modal-yt-btn">▶ YouTube</span>`;
    list.appendChild(el);
  });
  document.getElementById("genre-modal-overlay").classList.add("open");
  document.body.style.overflow = "hidden";
}
document.getElementById("genre-modal-close").addEventListener("click",()=>{
  document.getElementById("genre-modal-overlay").classList.remove("open");
  document.body.style.overflow = "";
});
document.getElementById("genre-modal-overlay").addEventListener("click",e=>{
  if(e.target===e.currentTarget){e.currentTarget.classList.remove("open");document.body.style.overflow="";}
});

// ── MOOD TEST ─────────────────────────────────────────────────────────────────
function renderTest(){
  const sec = document.getElementById("test-section");
  sec.innerHTML = "";
  const t = LANG_TEXT[currentLang];
  const qs = QUESTIONS[currentLang];
  if(testDone){ renderResult(sec); return; }
  const current = answers.length;
  const pct = Math.round((current/4)*100);
  const dots = [0,1,2,3].map(i=>{
    let cls = i<current?"done":i===current?"active":"";
    return `<div class="p-dot ${cls}"></div>`;
  }).join("");
  const card = document.createElement("div");
  card.className = "q-card";
  card.innerHTML = `
    <div class="progress-wrap">
      <div class="progress-top">
        <span class="progress-label">${t.q} ${current+1} ${t.of} 4</span>
        <span class="progress-count">${pct}%</span>
      </div>
      <div class="progress-bar-track"><div class="progress-bar-fill" style="width:${pct}%"></div></div>
      <div class="progress-dots">${dots}</div>
    </div>
    <div class="q-number">${t.q} ${current+1}</div>
    <div class="q-text">${qs[current].text}</div>
    <div class="options" id="opts"></div>`;
  sec.appendChild(card);
  const opts = card.querySelector("#opts");
  qs[current].opts.forEach(o=>{
    const btn = document.createElement("button");
    btn.className = "opt-btn";
    btn.innerHTML = `
      <div class="opt-key">${o.key}</div>
      <div class="opt-content">
        <div class="opt-label">${o.label}</div>
        ${o.sub?`<div class="opt-sub">${o.sub}</div>`:""}
      </div>`;
    btn.addEventListener("click",()=>{
      opts.querySelectorAll(".opt-btn").forEach(b=>b.classList.remove("selected"));
      btn.classList.add("selected");
      setTimeout(()=>{ answers.push(o.key); if(answers.length===4){testDone=true;} renderTest(); },280);
    });
    opts.appendChild(btn);
  });
}

function getWinner(){
  const count={A:0,B:0,C:0,D:0};
  answers.forEach(a=>count[a]++);
  return Object.entries(count).sort((x,y)=>y[1]-x[1])[0][0];
}

function renderResult(sec){
  const winner = getWinner();
  const res = RESULTS[currentLang][winner];
  const t = LANG_TEXT[currentLang];
  const genreTags = res.genres.map(g=>`<span class="result-genre-tag">${g}</span>`).join("");
  const tracksHtml = res.tracks.map((tr,i)=>{
    const ytId = tr.ytId||"";
    const ytUrl = ytId ? `https://www.youtube.com/watch?v=${ytId}` : `https://www.youtube.com/results?search_query=${encodeURIComponent(tr.artist+" "+tr.title)}`;
    const thumb = ytId ? `<img class="track-thumb" src="https://img.youtube.com/vi/${ytId}/mqdefault.jpg" loading="lazy" onerror="this.style.display='none';this.nextElementSibling.style.display='flex'">` : "";
    return `<a class="music-track" href="${ytUrl}" target="_blank" rel="noopener noreferrer">
      <div class="track-thumb-wrap">
        ${thumb}
        <div class="track-thumb-ph" style="${ytId?"display:none":""}">🎵</div>
        <span class="track-num-badge">${i+1}</span>
      </div>
      <div class="track-info">
        <div class="track-title">${tr.title}</div>
        <div class="track-artist">${tr.artist}</div>
      </div>
      <div class="track-yt">▶ YouTube</div>
    </a>`;
  }).join("");
  sec.innerHTML = `
    <div class="result-card">
      <div class="result-banner">
        <span class="result-vibe-icon">${res.icon}</span>
        <div class="result-vibe-name">${res.vibe}</div>
        <div class="result-desc">${res.desc}</div>
      </div>
      <div class="result-genres">${genreTags}</div>
      <div class="tracks-header">${t.songs}</div>
      <div class="track-list">${tracksHtml}</div>
    </div>
    <div class="retry-row">
      <button class="retry-btn primary" id="retry-btn">🔄 ${t.restart}</button>
    </div>`;
  document.getElementById("retry-btn").addEventListener("click",()=>{ answers=[]; testDone=false; renderTest(); });
}

// ── MUSIC INFO ────────────────────────────────────────────────────────────────
function levenshtein(a,b){
  const m=a.length,n=b.length;
  const dp=Array.from({length:m+1},(_,i)=>Array.from({length:n+1},(_,j)=>i===0?j:j===0?i:0));
  for(let i=1;i<=m;i++)
    for(let j=1;j<=n;j++)
      dp[i][j]=a[i-1]===b[j-1]?dp[i-1][j-1]:1+Math.min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]);
  return dp[m][n];
}

function findArtistInDB(text){
  const norm=text.toLowerCase().trim();
  let best=null, bestLen=0;
  for(const artist of MUSIC_DB){
    for(const alias of artist.aliases){
      const a=alias.toLowerCase();
      if(norm.includes(a)&&a.length>bestLen){ best=artist; bestLen=a.length; }
    }
  }
  if(best) return {artist:best,fuzzy:false};
  const words=norm.split(/\s+/);
  let closestArtist=null, closestDist=Infinity;
  const MAX_DIST=3;
  for(const artist of MUSIC_DB){
    for(const alias of artist.aliases){
      const aliasWords=alias.toLowerCase().split(/\s+/);
      for(let i=0;i<=words.length-aliasWords.length;i++){
        const slice=words.slice(i,i+aliasWords.length).join(" ");
        const dist=levenshtein(slice,alias.toLowerCase());
        if(dist<closestDist){closestDist=dist;closestArtist=artist;}
      }
      const dist=levenshtein(norm,alias.toLowerCase());
      if(dist<closestDist){closestDist=dist;closestArtist=artist;}
    }
  }
  if(closestArtist&&closestDist<=MAX_DIST) return {artist:closestArtist,fuzzy:true,dist:closestDist,originalText:text};
  return null;
}

function renderInfoCard(data, fuzzyText){
  let html = `<div class="info-card">`;
  const photoHtml = data.photo
    ? `<img class="info-card-photo" src="${data.photo}" alt="${data.name}" onerror="this.outerHTML='<div class=info-card-emoji>${data.emoji||\"🎵\"}</div>'">`
    : `<div class="info-card-emoji">${data.emoji||"🎵"}</div>`;
  html += `<div class="info-card-header">
    ${photoHtml}
    <div>
      <div class="info-card-name">${data.name}</div>
      <div class="info-card-tagline">${data.tagline||""}</div>
    </div>
  </div>`;
  if(fuzzyText){
    html += `<div style="padding:10px 20px 0;font-size:0.8rem;color:var(--muted);background:rgba(255,145,0,0.06);border-bottom:1px solid var(--border)">🔍 "<b>${fuzzyText}</b>" topilmadi — <b>${data.name}</b> ni ko'rsatyapmiz</div>`;
  }
  html += `<div class="info-card-body">`;
  if(data.facts&&data.facts.length){
    html += `<div class="info-section"><div class="info-section-title"><span>📋</span> Asosiy ma'lumotlar</div>`;
    data.facts.forEach(f=>{html+=`<div class="info-fact-row"><span class="info-fact-key">${f.key}</span><span class="info-fact-val">${f.val}</span></div>`;});
    html += `</div>`;
  }
  if(data.sections&&data.sections.length){
    data.sections.forEach(sec=>{
      html += `<div class="info-section"><div class="info-section-title"><span>${sec.icon||"📌"}</span> ${sec.title}</div>`;
      if(sec.type==="prose"){
        html += `<div class="info-prose">${(sec.content||"").replace(/\n/g,"<br>")}</div>`;
      } else if(sec.type==="tags"&&Array.isArray(sec.content)){
        html += `<div class="info-tag-list">`;
        sec.content.forEach(tag=>{html+=`<span class="info-tag">${tag}</span>`;});
        html += `</div>`;
      } else if(sec.type==="albums"&&Array.isArray(sec.content)){
        html += `<div class="info-album-grid">`;
        sec.content.forEach(al=>{html+=`<div class="info-album-card"><div class="info-album-name">${al.name||al.title||""}</div><div class="info-album-year">${al.year||""}</div></div>`;});
        html += `</div>`;
      } else if(sec.type==="tracks"&&Array.isArray(sec.content)){
        sec.content.forEach((tr,idx)=>{
          const hasId=tr.ytId&&tr.ytId.length===11;
          const ytUrl=hasId?`https://www.youtube.com/watch?v=${tr.ytId}`:`https://www.youtube.com/results?search_query=${encodeURIComponent(tr.title||tr)}`;
          const thumbHtml=hasId?`<img src="https://img.youtube.com/vi/${tr.ytId}/mqdefault.jpg" style="width:80px;height:52px;border-radius:8px;object-fit:cover;flex-shrink:0;border:1px solid var(--border)" loading="lazy" onerror="this.outerHTML='<div style=width:80px;height:52px;border-radius:8px;background:var(--surface2);display:flex;align-items:center;justify-content:center;font-size:1.3rem;flex-shrink:0>🎵</div>'">`:`<div style="width:80px;height:52px;border-radius:8px;background:var(--surface2);display:flex;align-items:center;justify-content:center;font-size:1.3rem;flex-shrink:0;border:1px solid var(--border)">🎵</div>`;
          html+=`<a href="${ytUrl}" target="_blank" rel="noopener" class="info-track-item">
            <div style="position:relative;flex-shrink:0">
              <span style="position:absolute;bottom:3px;right:3px;min-width:18px;height:18px;background:rgba(0,0,0,0.78);border-radius:4px;font-size:0.6rem;font-weight:700;display:flex;align-items:center;justify-content:center;color:#fff;padding:0 4px">${idx+1}</span>
              ${thumbHtml}
            </div>
            <div style="flex:1;min-width:0;padding:0 12px">
              <div style="font-weight:600;font-size:0.87rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;color:#f0f0f0">${tr.title||tr}</div>
            </div>
            <div style="flex-shrink:0;font-family:var(--font-mono);font-size:0.65rem;font-weight:700;background:rgba(255,0,0,0.1);border-left:1px solid rgba(255,255,255,0.05);color:#ff5555;padding:0 14px;height:52px;display:flex;align-items:center;white-space:nowrap">▶ YouTube</div>
          </a>`;
        });
      }
      html += `</div>`;
    });
  }
  if(data.summary){
    html += `<div class="info-summary">${data.summary}</div>`;
  }
  html += `</div></div>`;
  return html;
}

function showTypingIndicator(){
  const el = document.createElement("div");
  el.id = "info-typing";
  el.style.cssText = "background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:16px 20px;margin-bottom:8px";
  el.innerHTML = `<div class="typing-dots"><span></span><span></span><span></span></div>`;
  document.getElementById("info-results").prepend(el);
}

function hideTypingIndicator(){
  const el = document.getElementById("info-typing");
  if(el) el.remove();
}

function infoSearch(query){
  if(!query) query = document.getElementById("info-input").value.trim();
  if(!query) return;
  document.getElementById("info-input").value = "";
  document.getElementById("info-welcome").style.display = "none";
  const btn = document.getElementById("info-send-btn");
  btn.disabled = true;
  const results = document.getElementById("info-results");
  showTypingIndicator();
  setTimeout(()=>{
    hideTypingIndicator();
    const found = findArtistInDB(query);
    if(found){
      const fuzzyLabel = found.fuzzy ? found.originalText||query : null;
      const card = document.createElement("div");
      card.innerHTML = renderInfoCard(found.artist, fuzzyLabel);
      results.prepend(card.firstElementChild);
    } else {
      const notFound = document.createElement("div");
      notFound.className = "info-not-found";
      notFound.innerHTML = `<div class="big-icon">🔍</div><div style="font-weight:600;margin-bottom:6px">"${query}" topilmadi</div><div style="font-size:0.84rem">Boshqa nom bilan urinib ko'ring</div>`;
      results.prepend(notFound);
    }
    btn.disabled = false;
  }, 500);
}

document.getElementById("info-send-btn").addEventListener("click",()=>infoSearch(""));
document.getElementById("info-input").addEventListener("keydown",e=>{
  if(e.key==="Enter"){e.preventDefault();infoSearch("");}
});

// ── INIT ──────────────────────────────────────────────────────────────────────
buildGrid();
renderTest();
</script>
</body>
</html>"""

components.html(HTML, height=1400, scrolling=True)
