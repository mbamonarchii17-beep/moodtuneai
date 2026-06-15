import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="MoodTune AI",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide streamlit chrome
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

/* ─── MOOD TEST ─────────────────────────────────────────── */
.test-section{margin-bottom:40px}
.test-intro{background:var(--surface);border:1px solid rgba(255,87,34,0.25);border-radius:18px;padding:22px;margin-bottom:24px}
.test-intro-header{display:flex;align-items:center;gap:14px;margin-bottom:12px}
.test-intro-icon{font-size:2rem;width:52px;height:52px;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,rgba(255,87,34,0.15),rgba(255,145,0,0.08));border-radius:14px;border:1px solid rgba(255,87,34,0.2);flex-shrink:0}
.test-intro-title{font-size:1.1rem;font-weight:700;margin-bottom:4px}
.test-intro-sub{font-size:0.84rem;color:var(--muted);line-height:1.5}

/* Question card */
.q-card{background:var(--surface);border:1px solid var(--border);border-radius:18px;padding:22px;animation:fadeSlide 0.35s cubic-bezier(0.16,1,0.3,1)}
@keyframes fadeSlide{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:translateY(0)}}

/* Progress bar */
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

/* Question text */
.q-number{font-size:0.68rem;font-weight:700;text-transform:uppercase;letter-spacing:0.1em;color:var(--fire-glow);margin-bottom:8px}
.q-text{font-size:1rem;font-weight:600;line-height:1.45;margin-bottom:18px;color:var(--text)}

/* Options */
.options{display:flex;flex-direction:column;gap:9px}
.opt-btn{display:flex;align-items:flex-start;gap:12px;background:rgba(255,255,255,0.025);border:1px solid rgba(255,255,255,0.07);border-radius:12px;padding:13px 15px;cursor:pointer;transition:all 0.2s;text-align:left;width:100%;font-family:var(--font-head)}
.opt-btn:hover{background:rgba(255,87,34,0.07);border-color:rgba(255,87,34,0.3);transform:translateX(3px)}
.opt-btn.selected{background:rgba(255,87,34,0.12);border-color:rgba(255,87,34,0.5);transform:translateX(0)}
.opt-key{display:flex;align-items:center;justify-content:center;width:26px;height:26px;border-radius:8px;background:rgba(255,87,34,0.12);border:1px solid rgba(255,87,34,0.2);color:var(--fire-glow);font-weight:700;font-size:0.72rem;font-family:var(--font-mono);flex-shrink:0;margin-top:1px;transition:all 0.2s}
.opt-btn:hover .opt-key,.opt-btn.selected .opt-key{background:var(--fire);color:#fff;border-color:var(--fire)}
.opt-content{flex:1}
.opt-label{font-size:0.9rem;font-weight:600;color:var(--text);line-height:1.3}
.opt-sub{font-size:0.75rem;color:var(--muted);margin-top:3px;line-height:1.3}

/* ─── RESULT ────────────────────────────────────────────── */
.result-card{background:var(--surface);border:1px solid rgba(255,87,34,0.25);border-radius:20px;overflow:hidden;animation:fadeSlide 0.4s cubic-bezier(0.16,1,0.3,1);margin-bottom:24px}
.result-banner{padding:28px 24px 22px;text-align:center;position:relative;overflow:hidden}
.result-banner::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 50% 0%,rgba(255,87,34,0.18) 0%,transparent 70%)}
.result-vibe-icon{font-size:3rem;margin-bottom:10px;display:block;animation:pop 0.5s cubic-bezier(0.16,1,0.3,1)}
@keyframes pop{from{transform:scale(0.5);opacity:0}to{transform:scale(1);opacity:1}}
.result-vibe-name{font-size:1.4rem;font-weight:700;color:var(--fire-glow);margin-bottom:8px;position:relative}
.result-desc{font-size:0.88rem;color:#bbb;line-height:1.6;max-width:440px;margin:0 auto;position:relative}
.result-genres{display:flex;flex-wrap:wrap;gap:7px;padding:16px 20px;border-top:1px solid var(--border);border-bottom:1px solid var(--border)}
.result-genre-tag{background:rgba(255,87,34,0.08);border:1px solid rgba(255,87,34,0.2);color:var(--fire-glow);padding:5px 13px;border-radius:20px;font-size:0.78rem;font-weight:600}

/* Tracks */
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

/* Reset / Retry */
.retry-row{display:flex;gap:10px;flex-wrap:wrap}
.retry-btn{flex:1;min-width:140px;background:none;border:1px solid var(--border);color:var(--muted);padding:12px 18px;border-radius:12px;font-family:var(--font-head);font-size:0.88rem;font-weight:600;cursor:pointer;transition:all 0.2s}
.retry-btn:hover{border-color:var(--fire);color:var(--text)}
.retry-btn.primary{background:linear-gradient(135deg,var(--fire),var(--fire-glow));border-color:transparent;color:#fff}
.retry-btn.primary:hover{opacity:0.9;transform:translateY(-1px);box-shadow:0 6px 20px rgba(255,87,34,0.3)}

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

/* scrollbar */
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
      <button class="nav-tab" data-page="page-test">🎭 Kayfiyat Testi</button>
    </div>
    <div class="lang-panel" id="lang-panel">
      <button class="lang-btn active" data-lang="uz">UZ</button>
      <button class="lang-btn" data-lang="ru">RU</button>
      <button class="lang-btn" data-lang="en">EN</button>
    </div>
  </div>
</header>

<!-- PAGE 1: HOME (Trending) -->
<div class="page active" id="page-home">
  <div class="main-wrap">
    <div class="trending-title" id="trending-title">🔥 Trending hozir — bosing va tinglang</div>
    <div class="genre-grid" id="genre-grid"></div>
  </div>
</div>

<!-- PAGE 2: MOOD TEST -->
<div class="page" id="page-test">
  <div class="main-wrap">
    <div class="test-section" id="test-section"></div>
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
    {title:"Wow.",artist:"Post Malone",ytId:"SsodjxbHdcE"},
    {title:"Big Rings",artist:"Drake & Future",ytId:"7GaRr2GGzao"},
    {title:"Fefe",artist:"6ix9ine ft. Nicki Minaj",ytId:"qNkR6y_kBjg"},
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
    {title:"Kokomo",artist:"The Beach Boys",ytId:"pAwR6C82TCI"},
    {title:"867-5309/Jenny",artist:"Tommy Tutone",ytId:"6dx_8mHxMI0"}
  ]
};

// ── MOOD TEST DATA ────────────────────────────────────────────────────────────
const QUESTIONS = {
  uz:[
    {
      text:"Hozir ichingizdagi qaysi emotsiya birinchi o'rinda turibdi?",
      opts:[
        {key:"A",label:"😤 Jahl, asabiylik yoki stress",sub:"Hamma narsa asabga tegyapti"},
        {key:"B",label:"⚡ Energiya to'lib-toshayapti",sub:"Harakat qilgim kelyapti"},
        {key:"C",label:"😴 Charchoq va bo'shashish",sub:"Miyaga sokinlik kerak"},
        {key:"D",label:"🌙 Zerikish yoki mayuslik",sub:"Xayol surish kayfiyati"}
      ]
    },
    {
      text:"Sizga hozir qanday ritm (sur'at) kerak?",
      opts:[
        {key:"A",label:"💥 Juda tez va shovqinli",sub:""},
        {key:"B",label:"🕺 Ritmli, sho'x",sub:"Lekin asabga tegmaydigan"},
        {key:"C",label:"〰️ Bir tekisda ketadigan",sub:"Sokin fon"},
        {key:"D",label:"🌊 Sekin va mayin",sub:""}
      ]
    },
    {
      text:"Qo'shiqda so'zlar bo'lishi shartmi?",
      opts:[
        {key:"A",label:"🔥 Farqi yo'q",sub:"Asosiysi drayv bo'lsa bo'ldi"},
        {key:"B",label:"🎉 Ha, sho'x so'zlar",sub:"Qo'shilib aytishga oson"},
        {key:"C",label:"🎹 Umuman bo'lmasin",sub:"Yoki chet tilida, tushunarsiz"},
        {key:"D",label:"📖 Ha, ma'noli chuqur so'zlar",sub:""}
      ]
    },
    {
      text:"Musiqa sizni hozir qayerga yetaklashi kerak?",
      opts:[
        {key:"A",label:"💢 Negativni tashqariga chiqarishga",sub:"Baqirib-chaqirib"},
        {key:"B",label:"💃 To'g'ri raqs maydonchasiga",sub:"Divandan turib ketishga"},
        {key:"C",label:"🛋️ Divanga yotib dam olishga",sub:"Ko'zni yumib"},
        {key:"D",label:"💭 Shirin xayollarga",sub:"O'tmish yoki kelajak haqida"}
      ]
    }
  ],
  ru:[
    {
      text:"Какая эмоция сейчас у вас на первом месте?",
      opts:[
        {key:"A",label:"😤 Злость, раздражение или стресс",sub:"Всё достало"},
        {key:"B",label:"⚡ Переполняет энергия",sub:"Хочется действовать"},
        {key:"C",label:"😴 Усталость и расслабленность",sub:"Нужен покой"},
        {key:"D",label:"🌙 Скука или лёгкая грусть",sub:"Настрой на мечты"}
      ]
    },
    {
      text:"Какой темп нужен прямо сейчас?",
      opts:[
        {key:"A",label:"💥 Очень быстрый и громкий",sub:""},
        {key:"B",label:"🕺 Ритмичный, весёлый",sub:"Но не раздражающий"},
        {key:"C",label:"〰️ Равномерный, спокойный фон",sub:""},
        {key:"D",label:"🌊 Медленный и мягкий",sub:""}
      ]
    },
    {
      text:"Нужны ли слова в песне?",
      opts:[
        {key:"A",label:"🔥 Неважно",sub:"Главное — драйв"},
        {key:"B",label:"🎉 Да, весёлые слова",sub:"Чтобы подпевать"},
        {key:"C",label:"🎹 Нет, без слов",sub:"Или на непонятном языке"},
        {key:"D",label:"📖 Да, глубокие и смысловые",sub:""}
      ]
    },
    {
      text:"Куда должна привести тебя музыка?",
      opts:[
        {key:"A",label:"💢 Выплеснуть весь негатив",sub:"Кричать и бесноваться"},
        {key:"B",label:"💃 Прямо на танцпол",sub:"Встать с дивана"},
        {key:"C",label:"🛋️ Лечь и отдохнуть",sub:"Закрыть глаза"},
        {key:"D",label:"💭 В сладкие мечты",sub:"О прошлом или будущем"}
      ]
    }
  ],
  en:[
    {
      text:"Which emotion is on top right now?",
      opts:[
        {key:"A",label:"😤 Anger, irritation or stress",sub:"Everything is getting on my nerves"},
        {key:"B",label:"⚡ Bursting with energy",sub:"I want to move"},
        {key:"C",label:"😴 Tired and relaxed",sub:"Need some quiet"},
        {key:"D",label:"🌙 Boredom or mild sadness",sub:"Daydreaming mood"}
      ]
    },
    {
      text:"What kind of tempo do you need right now?",
      opts:[
        {key:"A",label:"💥 Very fast and loud",sub:""},
        {key:"B",label:"🕺 Rhythmic and upbeat",sub:"But not overwhelming"},
        {key:"C",label:"〰️ Steady, calm background",sub:""},
        {key:"D",label:"🌊 Slow and gentle",sub:""}
      ]
    },
    {
      text:"Do you need lyrics in the song?",
      opts:[
        {key:"A",label:"🔥 Doesn't matter",sub:"As long as it has drive"},
        {key:"B",label:"🎉 Yes, fun lyrics to sing along",sub:""},
        {key:"C",label:"🎹 No lyrics at all",sub:"Or in a foreign language"},
        {key:"D",label:"📖 Yes, deep and meaningful",sub:""}
      ]
    },
    {
      text:"Where should the music take you right now?",
      opts:[
        {key:"A",label:"💢 Release all the negativity",sub:"Scream it out"},
        {key:"B",label:"💃 Straight to the dance floor",sub:"Get off the couch"},
        {key:"C",label:"🛋️ Lie down and rest",sub:"Close your eyes"},
        {key:"D",label:"💭 Into sweet daydreams",sub:"About past or future"}
      ]
    }
  ]
};

// Result algorithm: count A,B,C,D → pick winner
const RESULTS = {
  uz:{
    A:{
      vibe:"Asabga qarshi dori", icon:"🔥",
      desc:"Siz hozir portlash arafasidasiz. Ikkita yo'l bor: energiyani chiqarib yuborish yoki tinchlanish.",
      genres:["Phonk","Heavy Metal","Lo-Fi Ambient","Dark Techno"],
      tracks:[
        {title:"DEAF KEV - Invincible",artist:"DEAF KEV",ytId:"J2X5mJ3HDYE"},
        {title:"Night Lovell - Dark Light",artist:"Night Lovell",ytId:"j-_7hqnHMbE"},
        {title:"Freddie Dredd - Gottage Inn",artist:"Freddie Dredd",ytId:"JhFbRBfqkbg"},
        {title:"Three Days Grace - I Hate Everything About You",artist:"Three Days Grace",ytId:"nRmAEgIpGiU"},
        {title:"Linkin Park - In The End",artist:"Linkin Park",ytId:"eVTXPUF4Oz4"},
        {title:"Linkin Park - Numb",artist:"Linkin Park",ytId:"kXYiU_JCYtU"},
        {title:"Disturbed - Down With The Sickness",artist:"Disturbed",ytId:"08dn6eNpTX4"},
        {title:"Rage Against The Machine - Killing In The Name",artist:"RATM",ytId:"bWXazVeVnYA"},
        {title:"System Of A Down - Chop Suey",artist:"System Of A Down",ytId:"CSvFpBOe8eY"},
        {title:"Slipknot - Wait And Bleed",artist:"Slipknot",ytId:"sSFTMbGlRY8"}
      ]
    },
    B:{
      vibe:"Raqs va Kayfiyat", icon:"💃",
      desc:"Energiya bor, lekin qo'shiq yo'q. Ssenariy emas — faqat raqs va quvnoqlik.",
      genres:["Dance Pop","Club Music","Uzbek Pop","Remix"],
      tracks:[
        {title:"Dua Lipa - Levitating",artist:"Dua Lipa",ytId:"TUVcZfQe-Kw"},
        {title:"Bruno Mars - Uptown Funk",artist:"Bruno Mars ft. Mark Ronson",ytId:"OPf0YbXqDm0"},
        {title:"The Weeknd - Blinding Lights",artist:"The Weeknd",ytId:"4NRXx6U8ABQ"},
        {title:"Dua Lipa - Don't Start Now",artist:"Dua Lipa",ytId:"oygrmKOqttA"},
        {title:"Harry Styles - As It Was",artist:"Harry Styles",ytId:"H5v3kku4y6Q"},
        {title:"Calvin Harris - Summer",artist:"Calvin Harris",ytId:"ebXbLfLACGM"},
        {title:"Kygo - Firestone",artist:"Kygo ft. Conrad",ytId:"9Sc-ir2UwGU"},
        {title:"Avicii - Wake Me Up",artist:"Avicii",ytId:"IcrbM1l_BoI"},
        {title:"Martin Garrix - Animals",artist:"Martin Garrix",ytId:"gCYcHz2k5x0"},
        {title:"Ariana Grande - 7 rings",artist:"Ariana Grande",ytId:"QYh6mYIJG2Y"}
      ]
    },
    C:{
      vibe:"Miyaga Perekur", icon:"🧠",
      desc:"Ishdan, o'qishdan yoki odamlardan charchagansiz. Miyani yuklamaydigan, shunchaki yoqimli fon kerak.",
      genres:["Lo-Fi Hip-Hop","Deep House","Mayin Jazz","Ambient"],
      tracks:[
        {title:"Lofi Girl - Chill Beats to Study",artist:"Lofi Girl",ytId:"jfKfPfyJRdk"},
        {title:"ChilledCow - Sleepy Fish",artist:"Sleepy Fish",ytId:"UiTBNVHUGbc"},
        {title:"Norah Jones - Don't Know Why",artist:"Norah Jones",ytId:"tO4dxvguQDk"},
        {title:"Nujabes - Feather",artist:"Nujabes",ytId:"RKoriT3NNOE"},
        {title:"J Dilla - So Far to Go",artist:"J Dilla",ytId:"jfJnMDdKgY0"},
        {title:"Bonobo - Kong",artist:"Bonobo",ytId:"7GF3Gg7IUi0"},
        {title:"Tycho - Awake",artist:"Tycho",ytId:"lAb-xDIXv6c"},
        {title:"Washed Out - Feel It All Around",artist:"Washed Out",ytId:"Tc0oJPJGSmo"},
        {title:"Still Woozy - Goodie Bag",artist:"Still Woozy",ytId:"oVvDKpS7Tj4"},
        {title:"Rex Orange County - Corduroy Dreams",artist:"Rex Orange County",ytId:"g9foCk25Y5Y"}
      ]
    },
    D:{
      vibe:"Lirika / Sokinlik", icon:"🌙",
      desc:"Bir oz yolg'izlik yoki sokin hayotiy kayfiyat. Naushnikda yolg'iz eshitiladigan treklar.",
      genres:["Indie Folk","Acoustic","Soul","Sad Pop"],
      tracks:[
        {title:"Billie Eilish - When The Party's Over",artist:"Billie Eilish",ytId:"pbMwTqkKSps"},
        {title:"The Weeknd - Call Out My Name",artist:"The Weeknd",ytId:"P9t9jHus3EU"},
        {title:"Lewis Capaldi - Someone You Loved",artist:"Lewis Capaldi",ytId:"zABZyAoxXqk"},
        {title:"Olivia Rodrigo - drivers license",artist:"Olivia Rodrigo",ytId:"ZmDBbnmKpqQ"},
        {title:"Sufjan Stevens - Death With Dignity",artist:"Sufjan Stevens",ytId:"lN0uOKPxGcE"},
        {title:"Phoebe Bridgers - Motion Sickness",artist:"Phoebe Bridgers",ytId:"GwLMDpbHvSY"},
        {title:"Bon Iver - Skinny Love",artist:"Bon Iver",ytId:"ssdgMomZqMI"},
        {title:"Hozier - Take Me To Church",artist:"Hozier",ytId:"PVjiKRfKpPI"},
        {title:"Ed Sheeran - The A Team",artist:"Ed Sheeran",ytId:"UAWcs5H-qgQ"},
        {title:"Damien Rice - The Blower's Daughter",artist:"Damien Rice",ytId:"RWJ8TqLMeAo"}
      ]
    }
  }
};
// Copy uz results to ru/en (same tracks, different vibe names)
RESULTS.ru = {
  A:{...RESULTS.uz.A, vibe:"Антидот от стресса", desc:"Вы сейчас на грани взрыва. Два пути: выплеснуть или успокоиться."},
  B:{...RESULTS.uz.B, vibe:"Танцы и кайф", desc:"Энергия есть, а музыки — нет. Никаких сценариев, только танец."},
  C:{...RESULTS.uz.C, vibe:"Перекур для мозга", desc:"Устали от работы, учёбы или людей. Нужен приятный, ненавязчивый фон."},
  D:{...RESULTS.uz.D, vibe:"Лирика / Тишина", desc:"Немного одиноко или тихое жизненное настроение. Треки для наушников в одиночестве."}
};
RESULTS.en = {
  A:{...RESULTS.uz.A, vibe:"Stress Antidote", desc:"You're on the verge of exploding. Two paths: release it or calm down."},
  B:{...RESULTS.uz.B, vibe:"Dance & Vibes", desc:"Energy is here, music is not. No script — just pure dance."},
  C:{...RESULTS.uz.C, vibe:"Brain Break", desc:"Tired of work, study or people. Just need a pleasant, non-demanding background."},
  D:{...RESULTS.uz.D, vibe:"Lyrics & Silence", desc:"A little lonely or quiet life mood. Tracks for headphones, alone."}
};

const LANG_TEXT = {
  uz:{trending:"🔥 Trending hozir — bosing va tinglang", q:"Savol",of:"dan",restart:"🔄 Qaytadan boshlash",seeAll:"Barchasi",result:"Sizning kayfiyatingiz:",genres:"Tavsiya etiladigan janrlar",songs:"🎧 Siz uchun qo'shiqlar"},
  ru:{trending:"🔥 Сейчас в тренде — нажмите и слушайте", q:"Вопрос",of:"из",restart:"🔄 Начать заново",seeAll:"Все треки",result:"Ваше настроение:",genres:"Рекомендуемые жанры",songs:"🎧 Треки для вас"},
  en:{trending:"🔥 Trending Now — click and listen", q:"Question",of:"of",restart:"🔄 Start Over",seeAll:"See all tracks",result:"Your vibe:",genres:"Recommended genres",songs:"🎧 Songs for you"}
};

// ── STATE ─────────────────────────────────────────────────────────────────────
let currentLang = "uz";
let answers = [];  // array of "A"|"B"|"C"|"D"
let testDone = false;

// ── LANG ──────────────────────────────────────────────────────────────────────
document.getElementById("lang-panel").addEventListener("click", e=>{
  const btn = e.target.closest(".lang-btn");
  if(!btn || btn.classList.contains("active")) return;
  document.querySelectorAll(".lang-btn").forEach(b=>b.classList.remove("active"));
  btn.classList.add("active");
  currentLang = btn.dataset.lang;
  document.getElementById("trending-title").textContent = LANG_TEXT[currentLang].trending;
  if(document.getElementById("page-test").classList.contains("active")) renderTest();
});

// ── PAGE NAV ──────────────────────────────────────────────────────────────────
document.querySelectorAll(".nav-tab").forEach(tab=>{
  tab.addEventListener("click",()=>{
    document.querySelectorAll(".nav-tab").forEach(t=>t.classList.remove("active"));
    document.querySelectorAll(".page").forEach(p=>p.classList.remove("active"));
    tab.classList.add("active");
    document.getElementById(tab.dataset.page).classList.add("active");
    if(tab.dataset.page === "page-test") renderTest();
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

// ── MOOD TEST RENDERER ────────────────────────────────────────────────────────
function renderTest(){
  const sec = document.getElementById("test-section");
  sec.innerHTML = "";
  const t = LANG_TEXT[currentLang];
  const qs = QUESTIONS[currentLang];

  if(testDone){
    renderResult(sec);
    return;
  }

  const current = answers.length; // 0..3

  // Progress HTML
  const pct = Math.round((current/4)*100);
  const dots = [0,1,2,3].map(i=>{
    let cls = "";
    if(i<current) cls="done";
    else if(i===current) cls="active";
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
      // Visual feedback
      opts.querySelectorAll(".opt-btn").forEach(b=>b.classList.remove("selected"));
      btn.classList.add("selected");
      btn.querySelector(".opt-key").style.background="var(--fire)";
      btn.querySelector(".opt-key").style.color="#fff";
      setTimeout(()=>{
        answers.push(o.key);
        if(answers.length===4){ testDone=true; }
        renderTest();
      }, 280);
    });
    opts.appendChild(btn);
  });
}

function getWinner(){
  const count = {A:0,B:0,C:0,D:0};
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
    const ytUrl = ytId && ytId!=="SEARCH"
      ? `https://www.youtube.com/watch?v=${ytId}`
      : `https://www.youtube.com/results?search_query=${encodeURIComponent(tr.artist+" "+tr.title)}`;
    const thumb = ytId && ytId!=="SEARCH"
      ? `<img class="track-thumb" src="https://img.youtube.com/vi/${ytId}/mqdefault.jpg" loading="lazy"
           onerror="this.style.display='none';this.nextElementSibling.style.display='flex'">`
      : "";
    return `<a class="music-track" href="${ytUrl}" target="_blank" rel="noopener noreferrer">
      <div class="track-thumb-wrap">
        ${thumb}
        <div class="track-thumb-ph" style="${ytId && ytId!=="SEARCH"?"display:none":""}">🎵</div>
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

  document.getElementById("retry-btn").addEventListener("click",()=>{
    answers=[]; testDone=false; renderTest();
  });
}

// ── INIT ──────────────────────────────────────────────────────────────────────
buildGrid();
</script>
</body>
</html>"""

components.html(HTML, height=1200, scrolling=True)
