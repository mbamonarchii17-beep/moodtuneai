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
<title>MoodTune AI</title>
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
body{background:var(--bg);color:var(--text);font-family:var(--font-head);min-height:100vh;display:flex;flex-direction:column;overflow-x:hidden}

/* HEADER */
header{display:flex;align-items:center;justify-content:space-between;padding:18px 32px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(6,6,6,0.95);backdrop-filter:blur(16px);z-index:100;flex-wrap:wrap;gap:10px}
.logo-area{display:flex;align-items:center;gap:14px}
.fire-wings{display:flex;align-items:center;width:44px;height:24px}
.wing{width:20px;height:20px;background:linear-gradient(45deg,var(--fire),var(--fire-glow));filter:drop-shadow(0 0 8px var(--fire))}
.wing.left{border-radius:0 100% 30% 100%;animation:flapLeft 3s ease-in-out infinite alternate}
.wing.right{border-radius:100% 0 100% 30%;animation:flapRight 3s ease-in-out infinite alternate}
@keyframes flapLeft{0%{transform:rotate(-25deg) scaleY(0.9)}100%{transform:rotate(-5deg) scaleY(1.1)}}
@keyframes flapRight{0%{transform:rotate(25deg) scaleY(0.9)}100%{transform:rotate(5deg) scaleY(1.1)}}
.logo-text{font-weight:700;font-size:1.25rem;letter-spacing:-0.03em}
.logo-text span{color:transparent;background:linear-gradient(to right,var(--fire-glow),#fff);-webkit-background-clip:text;background-clip:text}
.header-right{display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.nav-tabs{display:flex;gap:4px;background:var(--surface);padding:4px;border-radius:10px;border:1px solid var(--border)}
.nav-tab{background:none;border:none;color:var(--muted);font-family:var(--font-head);font-size:0.82rem;font-weight:600;padding:7px 14px;cursor:pointer;border-radius:6px;transition:all 0.2s;white-space:nowrap}
.nav-tab.active{background:var(--surface2);color:var(--fire-glow);border:1px solid rgba(255,87,34,0.2)}

/* PAGES */
.page{display:none;flex:1;flex-direction:column}
.page.active{display:flex}
.main-wrap{max-width:720px;margin:0 auto;padding:28px 20px 120px;width:100%}

/* TRENDING */
.trending-title{font-size:0.75rem;font-weight:600;text-transform:uppercase;letter-spacing:0.1em;color:var(--muted);margin-bottom:14px;display:flex;align-items:center;gap:10px}
.trending-title::after{content:'';flex:1;height:1px;background:var(--border)}
.genre-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin-bottom:32px}
.genre-card{background:var(--surface);border:1px solid var(--border);border-radius:12px;overflow:hidden;cursor:pointer;transition:all 0.25s;text-decoration:none;display:block}
.genre-card:hover{border-color:var(--fire);transform:translateY(-2px);box-shadow:0 8px 24px rgba(255,87,34,0.12)}
.genre-thumb-placeholder{width:100%;aspect-ratio:16/9;display:flex;align-items:center;justify-content:center;font-size:2.2rem;background:linear-gradient(135deg,var(--surface2),#0d0d0d)}
.genre-info{padding:10px 12px}
.genre-label{font-size:0.68rem;font-weight:700;text-transform:uppercase;letter-spacing:0.08em;color:var(--fire-glow);margin-bottom:3px}
.genre-track{font-size:0.85rem;font-weight:600;color:var(--text);line-height:1.3;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.genre-artist{font-size:0.75rem;color:var(--muted);margin-top:1px}

/* MOOD TEST SECTION (PASTGA TUSHDI) */
.test-section{margin-top:20px}
.test-intro{background:var(--surface);border:1px solid rgba(255,87,34,0.25);border-radius:18px;padding:22px;margin-bottom:24px}
.test-intro-header{display:flex;align-items:center;gap:14px}
.test-intro-icon{font-size:2rem;width:52px;height:52px;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,rgba(255,87,34,0.15),rgba(255,145,0,0.08));border-radius:14px;border:1px solid rgba(255,87,34,0.2);flex-shrink:0}
.test-intro-title{font-size:1.1rem;font-weight:700}
.test-intro-sub{font-size:0.84rem;color:var(--muted);margin-top:4px;line-height:1.5}
.q-card{background:var(--surface);border:1px solid var(--border);border-radius:18px;padding:22px;animation:fadeSlide 0.35s cubic-bezier(0.16,1,0.3,1)}
@keyframes fadeSlide{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:translateY(0)}}
.progress-wrap{margin-bottom:18px}
.progress-top{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}
.progress-label{font-size:0.72rem;font-weight:700;text-transform:uppercase;letter-spacing:0.08em;color:var(--muted)}
.progress-count{font-family:var(--font-mono);font-size:0.72rem;color:var(--fire-glow)}
.progress-bar-track{height:3px;background:var(--border);border-radius:3px;overflow:hidden}
.progress-bar-fill{height:100%;background:linear-gradient(to right,var(--fire),var(--fire-glow));border-radius:3px;transition:width 0.4s ease}
.q-text{font-size:1rem;font-weight:600;line-height:1.45;margin-bottom:18px}
.options{display:flex;flex-direction:column;gap:9px}
.opt-btn{display:flex;align-items:flex-start;gap:12px;background:rgba(255,255,255,0.025);border:1px solid rgba(255,255,255,0.07);border-radius:12px;padding:13px 15px;cursor:pointer;transition:all 0.2s;text-align:left;width:100%;font-family:var(--font-head)}
.opt-btn:hover{background:rgba(255,87,34,0.07);border-color:rgba(255,87,34,0.3);transform:translateX(3px)}
.opt-key{display:flex;align-items:center;justify-content:center;width:26px;height:26px;border-radius:8px;background:rgba(255,87,34,0.12);border:1px solid rgba(255,87,34,0.2);color:var(--fire-glow);font-weight:700;font-size:0.72rem;font-family:var(--font-mono);flex-shrink:0}
.opt-label{font-size:0.9rem;font-weight:600;color:var(--text)}

/* RESULTS CARD */
.result-card{background:var(--surface);border:1px solid var(--border);border-radius:18px;overflow:hidden;margin-bottom:20px}
.result-banner{background:linear-gradient(135deg,rgba(255,87,34,0.15),rgba(255,145,0,0.05));padding:24px;border-bottom:1px solid var(--border)}
.result-vibe-icon{font-size:2.5rem;margin-bottom:8px;display:block}
.result-vibe-name{font-size:1.4rem;font-weight:700;color:var(--fire-glow)}
.result-desc{font-size:0.88rem;color:var(--muted);margin-top:6px;line-height:1.5}
.result-genres{padding:14px 20px 8px;display:flex;flex-wrap:wrap;gap:6px}
.genre-tag{background:var(--surface2);border:1px solid var(--border);font-size:0.72rem;font-weight:600;padding:4px 10px;border-radius:6px;color:var(--fire-glow)}
.music-track{display:flex;align-items:center;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.05);border-radius:12px;margin:0 20px 8px;text-decoration:none;color:#fff;overflow:hidden;transition:all 0.22s}
.music-track:hover{background:rgba(255,87,34,0.07);border-color:rgba(255,87,34,0.3);transform:translateX(3px)}
.track-thumb-wrap{position:relative;width:80px;height:52px;flex-shrink:0}
.track-thumb-ph{width:100%;height:100%;background:var(--surface2);display:flex;align-items:center;justify-content:center;font-size:1.2rem}
.track-num-badge{position:absolute;bottom:3px;right:3px;background:rgba(0,0,0,0.75);font-size:0.6rem;font-weight:700;padding:1px 5px;border-radius:3px}
.track-info{flex:1;padding:0 12px;min-width:0}
.track-title{font-weight:600;font-size:0.86rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.track-artist{font-size:0.72rem;color:var(--muted);margin-top:2px}
.track-yt{font-family:var(--font-mono);font-size:0.65rem;font-weight:700;color:#ff5555;padding:0 14px;background:rgba(255,0,0,0.05);height:52px;display:flex;align-items:center}
.tracks-header{padding:12px 20px 6px;font-size:0.7rem;font-weight:700;text-transform:uppercase;letter-spacing:0.08em;color:var(--muted)}
.retry-row{text-align:center;margin-bottom:24px}
.retry-btn{background:var(--surface);border:1px solid var(--border);color:var(--text);font-family:var(--font-head);font-weight:600;font-size:0.86rem;padding:10px 20px;border-radius:10px;cursor:pointer;transition:all 0.2s}
.retry-btn:hover{border-color:var(--fire);color:var(--fire-glow)}

/* ─── PAGE 2: MUSIC INFO CHAT & RICH PANEL ─── */
.info-welcome-card{background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:26px 22px;margin-bottom:20px}
.info-welcome-icon{font-size:2.2rem;margin-bottom:10px}
.info-welcome-title{font-size:1.25rem;font-weight:700;margin-bottom:6px}
.info-welcome-sub{color:var(--muted);font-size:0.88rem;line-height:1.55}
.chat-stream{display:flex;flex-direction:column;gap:14px;margin-bottom:20px}
.bubble{display:flex;flex-direction:column;max-width:85%;animation:bubbleIn 0.25s ease-out forwards}
@keyframes bubbleIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
.bubble.user{align-self:flex-end}
.bubble.bot{align-self:flex-start}
.bubble-msg{padding:12px 16px;border-radius:14px;font-size:0.92rem;line-height:1.45}
.bubble.user .bubble-msg{background:linear-gradient(135deg,var(--fire),var(--fire-glow));color:#fff;border-bottom-right-radius:4px}
.bubble.bot .bubble-msg{background:var(--surface);border:1px solid var(--border);color:var(--text);border-bottom-left-radius:4px}

/* DYNAMIC RICH CARD FOR MUSIC INFO */
.info-rich{margin-top:10px}
.info-section{margin-bottom:16px}
.info-section:last-child{margin-bottom:0}
.info-section-title{font-size:0.72rem;font-weight:700;text-transform:uppercase;letter-spacing:0.1em;color:var(--fire-glow);margin-bottom:8px;display:flex;align-items:center;gap:6px}
.info-section-title::after{content:'';flex:1;height:1px;background:rgba(255,87,34,0.15)}
.info-fact-row{display:flex;gap:8px;margin-bottom:5px;align-items:flex-start}
.info-fact-key{font-size:0.78rem;color:var(--muted);min-width:85px;flex-shrink:0}
.info-fact-val{font-size:0.85rem;color:var(--text);font-weight:500;line-height:1.4}
.info-bio{font-size:0.84rem;color:var(--muted);line-height:1.5;margin-top:4px}
.typing-indicator{display:flex;gap:4px;padding:8px 12px;background:var(--surface);border:1px solid var(--border);border-radius:10px;width:fit-content;align-self:flex-start;margin-bottom:10px}
.typing-dot{width:6px;height:6px;background:var(--muted);border-radius:50%;animation:typeBounce 1.2s infinite ease-in-out}
.typing-dot:nth-child(2){animation-delay:0.2s}
.typing-dot:nth-child(3){animation-delay:0.4s}
@keyframes typeBounce{0%,100%{transform:translateY(0)}50%{transform:translateY(-4px);background:var(--fire-glow)}}

/* FIXED BOTTOM CHAT BAR */
.bottom-panel{position:fixed;bottom:0;left:0;right:0;background:rgba(6,6,6,0.92);backdrop-filter:blur(20px);border-top:1px solid var(--border);padding:14px 20px 20px;z-index:90}
.input-container{max-width:700px;margin:0 auto;display:flex;gap:10px;align-items:flex-end}
.input-field{flex:1;background:var(--surface);border:1px solid var(--border);border-radius:12px;color:var(--text);font-family:var(--font-head);font-size:0.95rem;padding:12px 14px;resize:none;outline:none;min-height:46px;max-height:120px;line-height:1.4;transition:all 0.2s}
.input-field:focus{border-color:var(--fire)}
.send-btn{width:46px;height:46px;border-radius:12px;background:linear-gradient(135deg,var(--fire),var(--fire-glow));border:none;cursor:pointer;display:flex;align-items:center;justify-content:center;color:#fff;transition:transform 0.15s;flex-shrink:0}
.send-btn:hover{transform:scale(1.03)}
.send-btn:disabled{background:var(--surface2);color:var(--muted);cursor:not-allowed}
</style>
</head>
<body>

<header>
  <div class="logo-area">
    <div class="fire-wings"><div class="wing left"></div><div class="wing right"></div></div>
    <div class="logo-text">MoodTune<span>AI</span></div>
  </div>
  <div class="header-right">
    <div class="nav-tabs">
      <button class="nav-tab active" data-page="page-mood">🎵 Mood Chat</button>
      <button class="nav-tab" data-page="page-info">🎤 Music Info</button>
    </div>
  </div>
</header>

<div class="page active" id="page-mood">
  <div class="main-wrap">
    
    <div class="trending-title">Trenddagi Janrlar</div>
    <div class="genre-grid" id="genre-grid"></div>

    <div class="test-section">
      <div class="test-intro" id="test-intro-box">
        <div class="test-intro-header">
          <div class="test-intro-icon">🎭</div>
          <div>
            <div class="test-intro-title">Hozirgi kayfiyatingiz qanday?</div>
            <div class="test-intro-sub">Tezkor psixologik testni topshiring va AI sizga mos keladigan musiqiy to'plamni (Vibe) shakllantirib beradi.</div>
          </div>
        </div>
      </div>
      <div id="test-core-box"></div>
    </div>

  </div>
</div>

<div class="page" id="page-info">
  <div class="main-wrap">
    <div class="info-welcome-card">
      <div class="info-welcome-icon">🎤</div>
      <div class="info-welcome-title">Music Info Panel</div>
      <div class="info-welcome-sub">Sevimli san'atkorlaringiz, guruhlar yoki treklar haqida chuqur tahliliy ma'lumotlar bazasi. Istalgan ijodkor nomini yozib qidiring.</div>
    </div>

    <div class="chat-stream" id="info-chat-stream"></div>
    <div class="typing-indicator" id="info-typing" style="display:none"><div class="typing-dot"></div><div class="typing-dot"></div><div class="typing-dot"></div></div>
  </div>
</div>

<div class="bottom-panel">
  <div class="input-container">
    <textarea class="input-field" id="chat-input" rows="1" placeholder="Savolingizni yozing..."></textarea>
    <button class="send-btn" id="send-btn" disabled>
      <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
    </button>
  </div>
</div>

<script>
// ─── MA'LUMOTLAR BAZASI (final.html dagi kabi) ───
const ARTISTS_DB = [
  {
    name: "The Weeknd",
    match: ["weeknd", "the weeknd", "abel"],
    genre: "R&B, Pop, Synth-pop",
    country: "Kanada",
    period: "2010 - hozirgacha",
    vibe: "Tungi shahar, melanxoliya, neon xotiralar",
    bio: "Abel Tesfaye o'zining sirlilik va chuqur retro-sintizator tovushlari bilan zamonaviy R&B va Pop musiqasini butunlay o'zgartirdi. Uning 'Blinding Lights' treki o'n yillikning eng katta xitlaridan biridir."
  },
  {
    name: "Eminem",
    match: ["eminem", "slim shady", "marshall"],
    genre: "Hip-Hop, Rap",
    country: "AQSh",
    period: "1996 - hozirgacha",
    vibe: "Agressiv energiya, motivatsiya, o'tkir lirika",
    bio: "Marshall Mathers - tarixdagi eng ko'p sotilgan rep ijrochisi. Tezkor va murakkab qofiyalari, texnik mahorati hamda hayotiy qiyinchiliklar tasvirlangan treklari bilan dunyoga mashhur."
  },
  {
    name: "Hans Zimmer",
    match: ["hans zimmer", "zimmer", "hans"],
    genre: "Cinematic, Orchestral",
    country: "Germaniya / AQSh",
    period: "1977 - hozirgacha",
    vibe: "Epik atmosferalar, chuqur o'ylash, grandiozlik",
    bio: "Interstellar, Inception, Gladiator va The Dark Knight filmlari bastakori. Elektron musiqani simfonik orkestr bilan mukammal uyg'unlashtirgan master."
  }
];

const sampleGenres = [
  { label: "Chill & Lo-Fi", track: "Sunset Drive", artist: "Lofi Dreamer", icon: "☕" },
  { label: "Energetic Pop", track: "Neon Lights", artist: "Star Glow", icon: "⚡" },
  { label: "Cinematic Epic", track: "Time Travel", artist: "Orchestra", icon: "🌌" },
  { label: "Deep Rap", track: "Night Stories", artist: "Shadow", icon: "🎤" }
];

const TEST_QUESTIONS = [
  {
    q: "Hozirgi atrofingizdagi muhit qanday ko'rinishda?",
    opts: [
      { text: "Tinch va qorong'u xona", vibe: "melancholic" },
      { text: "Yorug' va harakat ko'p joy", vibe: "energetic" },
      { text: "Tabiat qo'ynida yoki ochiq havo", vibe: "chill" }
    ]
  },
  {
    q: "Agar hozir rasm chizsangiz, qaysi rang asosiy bo'lardi?",
    opts: [
      { text: "To'q ko'k yoki binafsha", vibe: "melancholic" },
      { text: "Yorqin qizil yoki sariq", vibe: "energetic" },
      { text: "Yumshoq pastel yoki yashil", vibe: "chill" }
    ]
  }
];

// REKORDLAR VA HOLATLAR
let currentTab = "page-mood";
let testAnswers = [];
let currentQIdx = 0;

const chatInput = document.getElementById("chat-input");
const sendBtn = document.getElementById("send-btn");
const infoStream = document.getElementById("info-chat-stream");

// SAHIFALAR ALMASHINUVI
document.querySelectorAll(".nav-tab").forEach(tab => {
  tab.addEventListener("click", () => {
    document.querySelectorAll(".nav-tab").forEach(t => t.classList.remove("active"));
    document.querySelectorAll(".page").forEach(p => p.classList.remove("active"));
    
    tab.classList.add("active");
    currentTab = tab.getAttribute("data-page");
    document.getElementById(currentTab).classList.add("active");

    // Inputning placeholderini sahifaga moslab o'zgartirish
    if (currentTab === "page-mood") {
      chatInput.placeholder = "Kayfiyatingizni yozing yoki tasvirlang...";
    } else {
      chatInput.placeholder = "Ijodkor nomini yozing (Masalan: Eminem, The Weeknd)...";
    }
  });
});

// INITIALIZE LOBBY GIGS
function initLobby() {
  const grid = document.getElementById("genre-grid");
  grid.innerHTML = sampleGenres.map(g => `
    <div class="genre-card">
      <div class="genre-thumb-placeholder">${g.icon}</div>
      <div class="genre-info">
        <div class="genre-label">${g.label}</div>
        <div class="genre-track">${g.track}</div>
        <div class="genre-artist">${g.artist}</div>
      </div>
    </div>
  `).join("");
  
  renderQuestion();
}

// KAYFIYAT TESTI TIZIMI
function renderQuestion() {
  const box = document.getElementById("test-core-box");
  if (currentQIdx >= TEST_QUESTIONS.length) {
    renderResult();
    return;
  }
  
  const qObj = TEST_QUESTIONS[currentQIdx];
  let optionsHtml = qObj.opts.map((opt, i) => `
    <button class="opt-btn" onclick="selectOption('${opt.vibe}')">
      <span class="opt-key">${String.fromCharCode(65 + i)}</span>
      <span class="opt-label">${opt.text}</span>
    </button>
  `).join("");

  box.innerHTML = `
    <div class="q-card">
      <div class="progress-wrap">
        <div class="progress-top">
          <span class="progress-label">Savol</span>
          <span class="progress-count">${currentQIdx + 1}/${TEST_QUESTIONS.length}</span>
        </div>
        <div class="progress-bar-track">
          <div class="progress-bar-fill" style="width: ${((currentQIdx + 1) / TEST_QUESTIONS.length) * 100}%"></div>
        </div>
      </div>
      <div class="q-text">${qObj.q}</div>
      <div class="options">${optionsHtml}</div>
    </div>
  `;
}

window.selectOption = function(vibe) {
  testAnswers.push(vibe);
  currentQIdx++;
  renderQuestion();
};

function renderResult() {
  const box = document.getElementById("test-core-box");
  // Eng ko'p tanlangan vibe'ni hisoblash
  const counts = {};
  let finalVibe = "chill";
  let max = 0;
  testAnswers.forEach(v => {
    counts[v] = (counts[v] || 0) + 1;
    if (counts[v] > max) { max = counts[v]; finalVibe = v; }
  });

  let vibeTitle = "Chill & Relax";
  let vibeIcon = "☕";
  let vibeDesc = "Siz xotirjamlik va sokinlik holatidasiz. Sizga eng mos keladigan treklar tanlandi.";

  if (finalVibe === "energetic") {
    vibeTitle = "High Energy Boost"; vibeIcon = "⚡"; vibeDesc = "Ichki kuch va yuqori motivatsiya oqimidasiz! Dinamik ritmlar siz uchun.";
  } else if (finalVibe === "melancholic") {
    vibeTitle = "Night Melancholy"; vibeIcon = "🌌"; vibeDesc = "Chuqur o'ylar va retro hislar og'ushidasiz. Chuqur lirik treklar ro'yxati.";
  }

  box.innerHTML = `
    <div class="result-card">
      <div class="result-banner">
        <span class="result-vibe-icon">${vibeIcon}</span>
        <div class="result-vibe-name">${vibeTitle}</div>
        <div class="result-desc">${vibeDesc}</div>
      </div>
      <div class="tracks-header">Tavsiya etilgan musiqalar</div>
      <a class="music-track" href="https://youtube.com" target="_blank">
        <div class="track-thumb-wrap"><div class="track-thumb-ph">🎵</div><span class="track-num-badge">1</span></div>
        <div class="track-info"><div class="track-title">AI Selected Track #1</div><div class="track-artist">Vibe Producer</div></div>
        <div class="track-yt">▶ YouTube</div>
      </a>
    </div>
    <div class="retry-row">
      <button class="retry-btn" onclick="resetTest()">🔄 Qayta urinish</button>
    </div>
  `;
}

window.resetTest = function() {
  testAnswers = [];
  currentQIdx = 0;
  renderQuestion();
};

// ─── MUSIC INFO PANEL INTEGRATSIYASI ───
function addBubble(stream, role, html) {
  const b = document.createElement("div");
  b.className = `bubble ${role}`;
  b.innerHTML = `<div class="bubble-msg">${html}</div>`;
  stream.appendChild(b);
  stream.scrollTop = stream.scrollHeight;
}

function renderArtistCard(art) {
  return `
    <div class="info-rich">
      <div class="info-section">
        <div class="info-section-title">Ijodkor Tahlili</div>
        <div class="info-fact-row"><div class="info-fact-key">Nomi:</div><div class="info-fact-val">${art.name}</div></div>
        <div class="info-fact-row"><div class="info-fact-key">Janr:</div><div class="info-fact-val">${art.genre}</div></div>
        <div class="info-fact-row"><div class="info-fact-key">Diyor / Yillar:</div><div class="info-fact-val">${art.country} (${art.period})</div></div>
        <div class="info-fact-row"><div class="info-fact-key">Musiqiy Vibe:</div><div class="info-fact-val">${art.vibe}</div></div>
      </div>
      <div class="info-section">
        <div class="info-section-title">Biografiya va Uslub</div>
        <div class="info-bio">${art.bio}</div>
      </div>
    </div>
  `;
}

function processInfoSearch(text) {
  const lower = text.toLowerCase();
  const found = ARTISTS_DB.find(a => a.match.some(m => lower.includes(m)));

  document.getElementById("info-typing").style.display = "flex";
  
  setTimeout(() => {
    document.getElementById("info-typing").style.display = "none";
    if (found) {
      addBubble(infoStream, "bot", renderArtistCard(found));
    } else {
      addBubble(infoStream, "bot", `🔍 "<b>${text}</b>" bazamizdan topilmadi. Hozircha quyidagi ijodkorlarni qidirib ko'rishingiz mumkin:<br><br>• <i>Eminem</i><br>• <i>The Weeknd</i><br>• <i>Hans Zimmer</i>`);
    }
    sendBtn.disabled = false;
  }, 600);
}

// INPUT VA SEND TUYMALARI MANTIG'I
chatInput.addEventListener("input", () => {
  chatInput.style.height = "auto";
  chatInput.style.height = chatInput.scrollHeight + "px";
  sendBtn.disabled = !chatInput.value.trim();
});

function handleSend() {
  const val = chatInput.value.trim();
  if (!val) return;

  chatInput.value = "";
  chatInput.style.height = "auto";
  sendBtn.disabled = true;

  if (currentTab === "page-info") {
    // 2-sahifada bo'lsa chat oqimiga yozadi
    addBubble(infoStream, "user", val);
    processInfoSearch(val);
  } else {
    // 1-sahifada bo'lsa shunchaki notification yoki javob simulyatsiyasi
    alert("Kayfiyatingiz qabul qilindi: " + val + "\\nTest topshirish orqali ham natija olishingiz mumkin.");
    sendBtn.disabled = false;
  }
}

sendBtn.addEventListener("click", handleSend);
chatInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    handleSend();
  }
});

// Start application
initLobby();
</script>
</body>
</html>
"""

components.html(HTML, height=850, scrolling=True)
