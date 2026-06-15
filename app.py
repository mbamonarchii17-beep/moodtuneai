cat > /home/claude/final_app.py << 'PYEOF'
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
iframe{border:none!important}
</style>
""", unsafe_allow_html=True)

HTML = r"""<!DOCTYPE html>
<html lang="uz">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet"/>
<style>
:root{
  --bg:#060606;--surface:#111;--surface2:#1a1a1a;--border:#222;
  --fire:#ff5722;--glow:#ff9100;--text:#f5f5f5;--muted:#666;
  --r:14px;--head:'Space Grotesk',sans-serif;--mono:'Space Mono',monospace;
}
*{box-sizing:border-box;margin:0;padding:0}
html{height:100%}
body{background:var(--bg);color:var(--text);font-family:var(--head);min-height:100vh}

/* ── HEADER ── */
.hdr{display:flex;align-items:center;justify-content:space-between;padding:14px 24px;
  border-bottom:1px solid var(--border);background:rgba(6,6,6,.97);
  backdrop-filter:blur(16px);position:sticky;top:0;z-index:999;flex-wrap:wrap;gap:8px}
.logo{display:flex;align-items:center;gap:10px;font-weight:700;font-size:1.15rem;letter-spacing:-.03em}
.logo em{color:transparent;background:linear-gradient(90deg,var(--glow),#fff);-webkit-background-clip:text;background-clip:text;font-style:normal}
.wings{display:flex;gap:2px}
.w{width:18px;height:18px;background:linear-gradient(45deg,var(--fire),var(--glow));filter:drop-shadow(0 0 6px var(--fire))}
.w.l{border-radius:0 100% 30% 100%;animation:fl 3s ease-in-out infinite alternate}
.w.r{border-radius:100% 0 100% 30%;animation:fr 3s ease-in-out infinite alternate}
@keyframes fl{0%{transform:rotate(-25deg)}100%{transform:rotate(-5deg)}}
@keyframes fr{0%{transform:rotate(25deg)}100%{transform:rotate(5deg)}}
.nav{display:flex;gap:4px;background:var(--surface);padding:4px;border-radius:10px;border:1px solid var(--border)}
.ntab{background:none;border:none;color:var(--muted);font-family:var(--head);font-size:.8rem;font-weight:600;
  padding:7px 13px;cursor:pointer;border-radius:7px;transition:all .2s;white-space:nowrap}
.ntab.on{background:var(--surface2);color:var(--glow);border:1px solid rgba(255,87,34,.2)}
.langs{display:flex;gap:3px;background:var(--surface);padding:4px;border-radius:10px;border:1px solid var(--border)}
.lb{background:none;border:none;color:var(--muted);font-family:var(--mono);font-size:.72rem;
  padding:5px 9px;cursor:pointer;border-radius:6px;transition:all .2s}
.lb.on{background:var(--surface2);color:var(--glow);border:1px solid rgba(255,87,34,.2)}

/* ── PAGES ── */
.page{display:none}.page.on{display:block}
.wrap{max-width:720px;margin:0 auto;padding:24px 18px 60px}

/* ── TRENDING ── */
.sec-label{font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;
  color:var(--muted);margin-bottom:12px;display:flex;align-items:center;gap:10px}
.sec-label::after{content:'';flex:1;height:1px;background:var(--border)}
.grid4{display:grid;grid-template-columns:1fr 1fr;gap:9px;margin-bottom:28px}
.gcard{background:var(--surface);border:1px solid var(--border);border-radius:12px;overflow:hidden;cursor:pointer;transition:all .25s}
.gcard:hover{border-color:var(--fire);transform:translateY(-2px);box-shadow:0 8px 24px rgba(255,87,34,.12)}
.gcard img{width:100%;aspect-ratio:16/9;object-fit:cover;display:block;background:var(--surface2)}
.gcard-ph{width:100%;aspect-ratio:16/9;display:flex;align-items:center;justify-content:center;font-size:2rem;background:var(--surface2)}
.gcard-info{padding:9px 11px}
.glabel{font-size:.65rem;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--glow);margin-bottom:2px}
.gtrack{font-size:.83rem;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.gartist{font-size:.72rem;color:var(--muted);margin-top:1px}

/* divider */
.divider{display:flex;align-items:center;gap:10px;margin:6px 0 20px}
.divider::before,.divider::after{content:'';flex:1;height:1px;background:var(--border)}
.divider span{font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--muted);white-space:nowrap}

/* ── MOOD TEST ── */
.qcard{background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:20px;
  animation:fadeUp .35s cubic-bezier(.16,1,.3,1)}
@keyframes fadeUp{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:translateY(0)}}
.prog-row{display:flex;justify-content:space-between;font-size:.7rem;margin-bottom:7px}
.prog-lbl{font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}
.prog-pct{font-family:var(--mono);color:var(--glow)}
.prog-bar{height:3px;background:var(--border);border-radius:3px;overflow:hidden;margin-bottom:9px}
.prog-fill{height:100%;background:linear-gradient(90deg,var(--fire),var(--glow));border-radius:3px;transition:width .4s}
.dots{display:flex;gap:6px;margin-bottom:16px}
.dot{width:8px;height:8px;border-radius:50%;background:var(--border);transition:all .3s}
.dot.done{background:var(--fire)}
.dot.cur{background:var(--glow);box-shadow:0 0 8px var(--glow);transform:scale(1.25)}
.qnum{font-size:.65rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--glow);margin-bottom:6px}
.qtext{font-size:.97rem;font-weight:600;line-height:1.45;margin-bottom:16px}
.opts{display:flex;flex-direction:column;gap:8px}
.opt{display:flex;align-items:flex-start;gap:11px;background:rgba(255,255,255,.025);
  border:1px solid rgba(255,255,255,.07);border-radius:11px;padding:12px 14px;
  cursor:pointer;transition:all .2s;text-align:left;width:100%;font-family:var(--head)}
.opt:hover{background:rgba(255,87,34,.07);border-color:rgba(255,87,34,.3);transform:translateX(3px)}
.opt.sel{background:rgba(255,87,34,.12);border-color:rgba(255,87,34,.5)}
.okey{display:flex;align-items:center;justify-content:center;width:26px;height:26px;
  border-radius:7px;background:rgba(255,87,34,.1);border:1px solid rgba(255,87,34,.2);
  color:var(--glow);font-weight:700;font-size:.7rem;font-family:var(--mono);flex-shrink:0;margin-top:1px;transition:all .2s}
.opt:hover .okey,.opt.sel .okey{background:var(--fire);color:#fff;border-color:var(--fire)}
.olabel{font-size:.88rem;font-weight:600;line-height:1.3}
.osub{font-size:.73rem;color:var(--muted);margin-top:2px}

/* ── RESULT ── */
.rcard{background:var(--surface);border:1px solid rgba(255,87,34,.25);border-radius:18px;
  overflow:hidden;animation:fadeUp .4s cubic-bezier(.16,1,.3,1);margin-bottom:20px}
.rbanner{padding:26px 22px 20px;text-align:center;position:relative;overflow:hidden}
.rbanner::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 50% 0%,rgba(255,87,34,.18),transparent 70%)}
.ricon{font-size:2.8rem;display:block;animation:pop .5s cubic-bezier(.16,1,.3,1);margin-bottom:8px}
@keyframes pop{from{transform:scale(.4);opacity:0}to{transform:scale(1);opacity:1}}
.rname{font-size:1.3rem;font-weight:700;color:var(--glow);margin-bottom:6px;position:relative}
.rdesc{font-size:.86rem;color:#bbb;line-height:1.6;max-width:400px;margin:0 auto;position:relative}
.rtags{display:flex;flex-wrap:wrap;gap:6px;padding:14px 18px;border-top:1px solid var(--border);border-bottom:1px solid var(--border)}
.rtag{background:rgba(255,87,34,.08);border:1px solid rgba(255,87,34,.2);color:var(--glow);padding:4px 12px;border-radius:20px;font-size:.76rem;font-weight:600}
.rth{padding:12px 18px 8px;font-size:.65rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--muted);display:flex;align-items:center;gap:8px}
.rth::after{content:'';flex:1;height:1px;background:var(--border)}
.tlist{padding:0 10px 14px;display:flex;flex-direction:column;gap:5px}
.trow{display:flex;align-items:center;background:rgba(255,255,255,.025);border:1px solid rgba(255,255,255,.05);
  border-radius:10px;text-decoration:none;color:#fff;transition:all .22s;overflow:hidden}
.trow:hover{background:rgba(255,87,34,.07);border-color:rgba(255,87,34,.35);transform:translateX(3px)}
.tthumb-wrap{position:relative;flex-shrink:0;width:86px;height:54px}
.tthumb{width:86px;height:54px;object-fit:cover;display:block}
.tthumb-ph{width:86px;height:54px;background:var(--surface2);display:flex;align-items:center;justify-content:center;font-size:1.3rem}
.tnum{position:absolute;bottom:3px;right:3px;min-width:17px;height:17px;background:rgba(0,0,0,.8);
  border-radius:4px;font-size:.58rem;font-weight:700;display:flex;align-items:center;justify-content:center;color:#fff;padding:0 3px}
.tinfo{flex:1;min-width:0;padding:0 11px}
.ttitle{font-weight:600;font-size:.85rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;color:#f0f0f0}
.tartist{font-size:.7rem;color:var(--muted);margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.tyt{flex-shrink:0;font-family:var(--mono);font-size:.62rem;font-weight:700;background:rgba(255,0,0,.1);
  border-left:1px solid rgba(255,255,255,.05);color:#ff5555;padding:0 12px;height:54px;display:flex;align-items:center;transition:background .2s}
.trow:hover .tyt{background:rgba(255,0,0,.2)}
.retry-row{display:flex;gap:9px}
.rbtn{flex:1;background:none;border:1px solid var(--border);color:var(--muted);padding:11px 16px;
  border-radius:11px;font-family:var(--head);font-size:.86rem;font-weight:600;cursor:pointer;transition:all .2s}
.rbtn:hover{border-color:var(--fire);color:var(--text)}
.rbtn.pri{background:linear-gradient(135deg,var(--fire),var(--glow));border-color:transparent;color:#fff}
.rbtn.pri:hover{opacity:.9;transform:translateY(-1px);box-shadow:0 6px 20px rgba(255,87,34,.3)}

/* ── MUSIC INFO PAGE ── */
.iwelcome{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:22px 20px;margin-bottom:18px}
.iwelcome-icon{font-size:2rem;margin-bottom:8px}
.iwelcome-title{font-size:1.15rem;font-weight:700;margin-bottom:4px}
.iwelcome-sub{color:var(--muted);font-size:.85rem;line-height:1.55}
.ichips{display:flex;gap:7px;flex-wrap:wrap;margin-top:12px}
.ichip{background:rgba(255,87,34,.08);border:1px solid rgba(255,87,34,.2);color:var(--glow);
  padding:6px 12px;border-radius:20px;font-size:.78rem;cursor:pointer;transition:all .2s}
.ichip:hover{background:rgba(255,87,34,.16);border-color:var(--fire)}
.isearch{display:flex;align-items:center;gap:8px;background:var(--surface);border:1px solid var(--border);
  border-radius:13px;padding:4px 4px 4px 14px;margin-bottom:18px;transition:border-color .2s}
.isearch:focus-within{border-color:var(--fire)}
.sinput{flex:1;background:none;border:none;outline:none;color:var(--text);font-family:var(--head);
  font-size:.93rem;padding:8px 0}
.sinput::placeholder{color:var(--muted)}
.sbtn{width:42px;height:42px;border-radius:10px;background:linear-gradient(135deg,var(--fire),var(--glow));
  border:none;cursor:pointer;display:flex;align-items:center;justify-content:center;color:#fff;flex-shrink:0;transition:transform .2s}
.sbtn:hover{transform:scale(1.05)}
.sbtn:disabled{background:var(--surface2);color:var(--muted);cursor:not-allowed}
.sbtn svg{width:17px;height:17px}
.iresults{display:flex;flex-direction:column;gap:14px}

/* info card */
.icard{background:var(--surface);border:1px solid var(--border);border-radius:16px;overflow:hidden;animation:fadeUp .35s cubic-bezier(.16,1,.3,1)}
.icard-hdr{padding:18px;display:flex;align-items:center;gap:14px;border-bottom:1px solid var(--border);
  background:linear-gradient(135deg,rgba(255,87,34,.07),transparent)}
.icard-photo{width:64px;height:64px;border-radius:12px;object-fit:cover;border:2px solid rgba(255,87,34,.35);flex-shrink:0}
.icard-emoji{width:64px;height:64px;border-radius:12px;background:var(--surface2);border:2px solid var(--border);
  display:flex;align-items:center;justify-content:center;font-size:2.2rem;flex-shrink:0}
.icard-name{font-size:1.1rem;font-weight:700;margin-bottom:3px}
.icard-tag{font-size:.8rem;color:var(--muted);line-height:1.4}
.icard-body{padding:16px 18px}
.isec{margin-bottom:14px}.isec:last-child{margin-bottom:0}
.isec-title{font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--glow);
  margin-bottom:9px;display:flex;align-items:center;gap:7px}
.isec-title::after{content:'';flex:1;height:1px;background:rgba(255,87,34,.15)}
.ifact{display:flex;gap:8px;margin-bottom:5px;align-items:flex-start}
.ifact-k{font-size:.76rem;color:var(--muted);min-width:88px;flex-shrink:0}
.ifact-v{font-size:.83rem;color:var(--text);font-weight:500}
.iprose{font-size:.88rem;color:#ccc;line-height:1.65}
.ialbums{display:grid;grid-template-columns:repeat(auto-fill,minmax(120px,1fr));gap:7px;margin-top:4px}
.ialbum{background:var(--surface2);border:1px solid var(--border);border-radius:9px;padding:10px;text-align:center}
.ialbum-name{font-size:.8rem;font-weight:600;margin-bottom:3px}
.ialbum-year{font-size:.7rem;color:var(--glow);font-family:var(--mono)}
.itags{display:flex;flex-wrap:wrap;gap:5px;margin-top:4px}
.itag{background:rgba(255,87,34,.08);border:1px solid rgba(255,87,34,.2);color:var(--glow);padding:4px 10px;border-radius:20px;font-size:.74rem}
.itrack{display:flex;align-items:center;background:rgba(255,255,255,.025);border:1px solid rgba(255,255,255,.05);
  border-radius:9px;text-decoration:none;color:#fff;transition:all .22s;overflow:hidden;margin-bottom:5px}
.itrack:hover{background:rgba(255,87,34,.07);border-color:rgba(255,87,34,.35);transform:translateX(3px)}
.itrack-thumb{width:78px;height:50px;object-fit:cover;display:block;flex-shrink:0}
.itrack-ph{width:78px;height:50px;background:var(--surface2);display:flex;align-items:center;justify-content:center;font-size:1.2rem;flex-shrink:0}
.itrack-num{position:absolute;bottom:2px;right:2px;min-width:16px;height:16px;background:rgba(0,0,0,.8);
  border-radius:3px;font-size:.56rem;font-weight:700;display:flex;align-items:center;justify-content:center;color:#fff;padding:0 3px}
.itrack-info{flex:1;min-width:0;padding:0 11px}
.itrack-title{font-weight:600;font-size:.84rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;color:#f0f0f0}
.itrack-yt{flex-shrink:0;font-family:var(--mono);font-size:.6rem;font-weight:700;background:rgba(255,0,0,.1);
  border-left:1px solid rgba(255,255,255,.05);color:#ff5555;padding:0 11px;height:50px;display:flex;align-items:center;white-space:nowrap;transition:background .2s}
.itrack:hover .itrack-yt{background:rgba(255,0,0,.2)}
.isummary{margin-top:4px;padding:10px 14px;background:rgba(255,87,34,.05);border-left:3px solid var(--fire);
  border-radius:0 8px 8px 0;font-size:.86rem;color:#bbb;line-height:1.6}
.inot-found{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:28px;text-align:center;color:var(--muted)}

/* typing */
.typing{display:flex;gap:5px;align-items:center;padding:14px 18px;background:var(--surface);
  border:1px solid var(--border);border-radius:14px}
.typing span{width:7px;height:7px;border-radius:50%;background:var(--muted);animation:bonce 1.2s infinite ease-in-out}
.typing span:nth-child(2){animation-delay:.15s}.typing span:nth-child(3){animation-delay:.3s}
@keyframes bonce{0%,100%{transform:translateY(0)}50%{transform:translateY(-7px)}}

/* genre modal */
.overlay{position:fixed;inset:0;background:rgba(0,0,0,.85);backdrop-filter:blur(8px);
  z-index:9999;display:none;align-items:center;justify-content:center;padding:20px}
.overlay.on{display:flex}
.modal{background:var(--surface);border:1px solid var(--border);border-radius:18px;
  max-width:500px;width:100%;max-height:80vh;overflow-y:auto;animation:fadeUp .3s cubic-bezier(.16,1,.3,1)}
.modal-hdr{padding:16px 18px 12px;border-bottom:1px solid var(--border);position:sticky;top:0;
  background:var(--surface);z-index:2;display:flex;align-items:center;justify-content:space-between}
.modal-lbl{font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--glow)}
.modal-title{font-size:.95rem;font-weight:700}
.modal-x{background:var(--surface2);border:1px solid var(--border);color:var(--muted);
  width:32px;height:32px;border-radius:50%;cursor:pointer;font-size:1rem;display:flex;align-items:center;justify-content:center;transition:all .2s}
.modal-x:hover{border-color:var(--fire);color:#fff}
.modal-list{padding:12px;display:flex;flex-direction:column;gap:7px}
.mtrack{display:flex;align-items:center;gap:10px;background:rgba(255,255,255,.03);
  border:1px solid rgba(255,255,255,.06);padding:9px 12px;border-radius:9px;
  text-decoration:none;color:#fff;transition:all .2s}
.mtrack:hover{background:rgba(255,87,34,.1);border-color:var(--fire);transform:translateX(3px)}
.mnum{width:22px;height:22px;background:var(--surface2);border:1px solid var(--border);
  border-radius:50%;font-size:.67rem;font-weight:700;color:var(--glow);display:flex;align-items:center;justify-content:center;flex-shrink:0}
.mthumb{width:60px;height:40px;border-radius:6px;object-fit:cover;flex-shrink:0;background:var(--surface2)}
.mthumb-ph{width:60px;height:40px;border-radius:6px;background:var(--surface2);display:flex;align-items:center;justify-content:center;font-size:1.1rem;flex-shrink:0;border:1px solid var(--border)}
.minfo{flex:1;min-width:0}
.mtitle{font-size:.85rem;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.martist{font-size:.72rem;color:var(--muted);margin-top:1px}
.myt{background:rgba(255,0,0,.12);border:1px solid rgba(255,0,0,.3);color:#ff4444;
  padding:4px 9px;border-radius:18px;font-size:.67rem;font-weight:700;white-space:nowrap;flex-shrink:0}

::-webkit-scrollbar{width:4px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:#333;border-radius:4px}
</style>
</head>
<body>

<div class="hdr">
  <div class="logo">
    <div class="wings"><div class="w l"></div><div class="w r"></div></div>
    MoodTune<em>AI</em>
  </div>
  <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap">
    <div class="nav">
      <button class="ntab on" onclick="goPage('home',this)">🎵 Musiqa</button>
      <button class="ntab" onclick="goPage('info',this)">🎤 Music Info</button>
    </div>
    <div class="langs" id="langs">
      <button class="lb on" data-l="uz">UZ</button>
      <button class="lb" data-l="ru">RU</button>
      <button class="lb" data-l="en">EN</button>
    </div>
  </div>
</div>

<!-- PAGE: HOME -->
<div class="page on" id="pg-home">
  <div class="wrap">
    <div class="sec-label" id="trend-lbl">🔥 Trending hozir — bosing va tinglang</div>
    <div class="grid4" id="genre-grid"></div>
    <div class="divider"><span id="mood-divider-lbl">🎭 Kayfiyat Testi</span></div>
    <div id="test-sec"></div>
  </div>
</div>

<!-- PAGE: INFO -->
<div class="page" id="pg-info">
  <div class="wrap">
    <div class="iwelcome" id="iwelcome">
      <div class="iwelcome-icon">🎤</div>
      <div class="iwelcome-title" id="iwtitle">Music Info Assistant</div>
      <div class="iwelcome-sub" id="iwsub">Artist, albom yoki qo'shiq haqida biror narsa so'rang.</div>
      <div class="ichips">
        <span class="ichip" onclick="doSearch('The Weeknd')">The Weeknd</span>
        <span class="ichip" onclick="doSearch('Eminem')">Eminem</span>
        <span class="ichip" onclick="doSearch('Billie Eilish')">Billie Eilish</span>
        <span class="ichip" onclick="doSearch('Drake')">Drake</span>
        <span class="ichip" onclick="doSearch('Скриптонит')">Скриптонит</span>
        <span class="ichip" onclick="doSearch('BAKR')">BAKR</span>
        <span class="ichip" onclick="doSearch('Michael Jackson')">Michael Jackson</span>
        <span class="ichip" onclick="doSearch('Coldplay')">Coldplay</span>
      </div>
    </div>
    <div class="isearch">
      <input class="sinput" id="sinput" type="text" placeholder="Artist, albom yoki qo'shiq nomi..." autocomplete="off"/>
      <button class="sbtn" id="sbtn" onclick="doSearch('')">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
        </svg>
      </button>
    </div>
    <div class="iresults" id="iresults"></div>
  </div>
</div>

<!-- MODAL -->
<div class="overlay" id="overlay" onclick="closeModal(event)">
  <div class="modal">
    <div class="modal-hdr">
      <div>
        <div class="modal-lbl" id="mlbl"></div>
        <div class="modal-title" id="mtitle"></div>
      </div>
      <button class="modal-x" onclick="closeModal()">✕</button>
    </div>
    <div class="modal-list" id="mlist"></div>
  </div>
</div>

<script>
// ════════════════════════════════════════════
// DATA
// ════════════════════════════════════════════
const GENRES = [
  {label:"Pop / R&B",   icon:"🎶", track:"Blinding Lights", artist:"The Weeknd",  ytId:"4NRXx6U8ABQ"},
  {label:"Rap / Hip-Hop",icon:"🎤", track:"God's Plan",      artist:"Drake",       ytId:"xpVfcZ0ZcFM"},
  {label:"Classic Rock", icon:"🎸", track:"Bohemian Rhapsody",artist:"Queen",      ytId:"fJ9rUzIMcZQ"},
  {label:"Nostalgic",    icon:"🌅", track:"Hotel California", artist:"Eagles",     ytId:"BciS5krYL80"}
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
    {title:"Come On Eileen",artist:"Dexys Midnight Runners",ytId:"qpbIaE5Bhdk"},
    {title:"Kokomo",artist:"The Beach Boys",ytId:"pAwR6C82TCI"},
    {title:"867-5309/Jenny",artist:"Tommy Tutone",ytId:"6dx_8mHxMI0"}
  ]
};

// ── MOOD TEST ──────────────────────────────
const Q = {
  uz:[
    {t:"Hozir ichingizdagi qaysi emotsiya birinchi o'rinda turibdi?",o:[
      {k:"A",l:"😤 Jahl, asabiylik yoki stress",s:"Hamma narsa asabga tegyapti"},
      {k:"B",l:"⚡ Energiya to'lib-toshayapti",s:"Harakat qilgim kelyapti"},
      {k:"C",l:"😴 Charchoq va bo'shashish",s:"Miyaga sokinlik kerak"},
      {k:"D",l:"🌙 Zerikish yoki mayuslik",s:"Xayol surish kayfiyati"}
    ]},
    {t:"Sizga hozir qanday ritm kerak?",o:[
      {k:"A",l:"💥 Juda tez va shovqinli",s:""},
      {k:"B",l:"🕺 Ritmli, sho'x",s:"Lekin asabga tegmaydigan"},
      {k:"C",l:"〰️ Bir tekisda ketadigan",s:"Sokin fon"},
      {k:"D",l:"🌊 Sekin va mayin",s:""}
    ]},
    {t:"Qo'shiqda so'zlar bo'lishi shartmi?",o:[
      {k:"A",l:"🔥 Farqi yo'q",s:"Asosiysi drayv bo'lsa bo'ldi"},
      {k:"B",l:"🎉 Ha, sho'x so'zlar",s:"Qo'shilib aytishga oson"},
      {k:"C",l:"🎹 Umuman bo'lmasin",s:"Yoki chet tilida"},
      {k:"D",l:"📖 Ha, ma'noli chuqur so'zlar",s:""}
    ]},
    {t:"Musiqa sizni hozir qayerga yetaklashi kerak?",o:[
      {k:"A",l:"💢 Negativni tashqariga chiqarishga",s:"Baqirib-chaqirib"},
      {k:"B",l:"💃 To'g'ri raqs maydonchasiga",s:"Divandan turib ketishga"},
      {k:"C",l:"🛋️ Divanga yotib dam olishga",s:"Ko'zni yumib"},
      {k:"D",l:"💭 Shirin xayollarga",s:"O'tmish yoki kelajak haqida"}
    ]}
  ],
  ru:[
    {t:"Какая эмоция сейчас у вас на первом месте?",o:[
      {k:"A",l:"😤 Злость, раздражение или стресс",s:"Всё достало"},
      {k:"B",l:"⚡ Переполняет энергия",s:"Хочется действовать"},
      {k:"C",l:"😴 Усталость и расслабленность",s:"Нужен покой"},
      {k:"D",l:"🌙 Скука или лёгкая грусть",s:"Настрой на мечты"}
    ]},
    {t:"Какой темп нужен прямо сейчас?",o:[
      {k:"A",l:"💥 Очень быстрый и громкий",s:""},
      {k:"B",l:"🕺 Ритмичный, весёлый",s:"Но не раздражающий"},
      {k:"C",l:"〰️ Равномерный, спокойный фон",s:""},
      {k:"D",l:"🌊 Медленный и мягкий",s:""}
    ]},
    {t:"Нужны ли слова в песне?",o:[
      {k:"A",l:"🔥 Неважно",s:"Главное — драйв"},
      {k:"B",l:"🎉 Да, весёлые слова",s:"Чтобы подпевать"},
      {k:"C",l:"🎹 Нет, без слов",s:"Или на непонятном языке"},
      {k:"D",l:"📖 Да, глубокие и смысловые",s:""}
    ]},
    {t:"Куда должна привести тебя музыка?",o:[
      {k:"A",l:"💢 Выплеснуть весь негатив",s:"Кричать и бесноваться"},
      {k:"B",l:"💃 Прямо на танцпол",s:"Встать с дивана"},
      {k:"C",l:"🛋️ Лечь и отдохнуть",s:"Закрыть глаза"},
      {k:"D",l:"💭 В сладкие мечты",s:"О прошлом или будущем"}
    ]}
  ],
  en:[
    {t:"Which emotion is on top right now?",o:[
      {k:"A",l:"😤 Anger, irritation or stress",s:"Everything is getting on my nerves"},
      {k:"B",l:"⚡ Bursting with energy",s:"I want to move"},
      {k:"C",l:"😴 Tired and relaxed",s:"Need some quiet"},
      {k:"D",l:"🌙 Boredom or mild sadness",s:"Daydreaming mood"}
    ]},
    {t:"What kind of tempo do you need right now?",o:[
      {k:"A",l:"💥 Very fast and loud",s:""},
      {k:"B",l:"🕺 Rhythmic and upbeat",s:"But not overwhelming"},
      {k:"C",l:"〰️ Steady, calm background",s:""},
      {k:"D",l:"🌊 Slow and gentle",s:""}
    ]},
    {t:"Do you need lyrics in the song?",o:[
      {k:"A",l:"🔥 Doesn't matter",s:"As long as it has drive"},
      {k:"B",l:"🎉 Yes, fun lyrics to sing along",s:""},
      {k:"C",l:"🎹 No lyrics at all",s:"Or in a foreign language"},
      {k:"D",l:"📖 Yes, deep and meaningful",s:""}
    ]},
    {t:"Where should the music take you right now?",o:[
      {k:"A",l:"💢 Release all the negativity",s:"Scream it out"},
      {k:"B",l:"💃 Straight to the dance floor",s:"Get off the couch"},
      {k:"C",l:"🛋️ Lie down and rest",s:"Close your eyes"},
      {k:"D",l:"💭 Into sweet daydreams",s:"About past or future"}
    ]}
  ]
};

const RES = {
  uz:{
    A:{v:"Asabga qarshi dori",i:"🔥",d:"Siz hozir portlash arafasidasiz. Ikkita yo'l bor: energiyani chiqarib yuborish yoki tinchlanish.",g:["Phonk","Heavy Metal","Lo-Fi Ambient","Dark Techno"],
      t:[{tt:"DEAF KEV - Invincible",ar:"DEAF KEV",id:"J2X5mJ3HDYE"},{tt:"Linkin Park - In The End",ar:"Linkin Park",id:"eVTXPUF4Oz4"},{tt:"Linkin Park - Numb",ar:"Linkin Park",id:"kXYiU_JCYtU"},{tt:"Three Days Grace - I Hate Everything About You",ar:"Three Days Grace",id:"nRmAEgIpGiU"},{tt:"Disturbed - Down With The Sickness",ar:"Disturbed",id:"08dn6eNpTX4"},{tt:"Rage Against The Machine - Killing In The Name",ar:"RATM",id:"bWXazVeVnYA"},{tt:"System Of A Down - Chop Suey",ar:"System Of A Down",id:"CSvFpBOe8eY"},{tt:"Slipknot - Wait And Bleed",ar:"Slipknot",id:"sSFTMbGlRY8"},{tt:"Night Lovell - Dark Light",ar:"Night Lovell",id:"j-_7hqnHMbE"},{tt:"Freddie Dredd - Gottage Inn",ar:"Freddie Dredd",id:"JhFbRBfqkbg"}]},
    B:{v:"Raqs va Kayfiyat",i:"💃",d:"Energiya bor, lekin qo'shiq yo'q. Ssenariy emas — faqat raqs va quvnoqlik.",g:["Dance Pop","Club Music","EDM","Remix"],
      t:[{tt:"Dua Lipa - Levitating",ar:"Dua Lipa",id:"TUVcZfQe-Kw"},{tt:"Bruno Mars - Uptown Funk",ar:"Bruno Mars",id:"OPf0YbXqDm0"},{tt:"The Weeknd - Blinding Lights",ar:"The Weeknd",id:"4NRXx6U8ABQ"},{tt:"Dua Lipa - Don't Start Now",ar:"Dua Lipa",id:"oygrmKOqttA"},{tt:"Harry Styles - As It Was",ar:"Harry Styles",id:"H5v3kku4y6Q"},{tt:"Calvin Harris - Summer",ar:"Calvin Harris",id:"ebXbLfLACGM"},{tt:"Kygo - Firestone",ar:"Kygo",id:"9Sc-ir2UwGU"},{tt:"Avicii - Wake Me Up",ar:"Avicii",id:"IcrbM1l_BoI"},{tt:"Martin Garrix - Animals",ar:"Martin Garrix",id:"gCYcHz2k5x0"},{tt:"Ariana Grande - 7 rings",ar:"Ariana Grande",id:"QYh6mYIJG2Y"}]},
    C:{v:"Miyaga Perekur",i:"🧠",d:"Ishdan, o'qishdan yoki odamlardan charchagansiz. Miyani yuklamaydigan yoqimli fon kerak.",g:["Lo-Fi Hip-Hop","Deep House","Mayin Jazz","Ambient"],
      t:[{tt:"Lofi Girl - Chill Beats",ar:"Lofi Girl",id:"jfKfPfyJRdk"},{tt:"Nujabes - Feather",ar:"Nujabes",id:"RKoriT3NNOE"},{tt:"Norah Jones - Don't Know Why",ar:"Norah Jones",id:"tO4dxvguQDk"},{tt:"Bonobo - Kong",ar:"Bonobo",id:"7GF3Gg7IUi0"},{tt:"Tycho - Awake",ar:"Tycho",id:"lAb-xDIXv6c"},{tt:"Washed Out - Feel It All Around",ar:"Washed Out",id:"Tc0oJPJGSmo"},{tt:"Still Woozy - Goodie Bag",ar:"Still Woozy",id:"oVvDKpS7Tj4"},{tt:"Rex Orange County - Corduroy Dreams",ar:"Rex Orange County",id:"g9foCk25Y5Y"},{tt:"J Dilla - So Far to Go",ar:"J Dilla",id:"jfJnMDdKgY0"},{tt:"Sleepy Fish - (lofi)",ar:"Sleepy Fish",id:"UiTBNVHUGbc"}]},
    D:{v:"Lirika / Sokinlik",i:"🌙",d:"Bir oz yolg'izlik yoki sokin hayotiy kayfiyat. Naushnikda yolg'iz eshitiladigan treklar.",g:["Indie Folk","Acoustic","Soul","Sad Pop"],
      t:[{tt:"Billie Eilish - When The Party's Over",ar:"Billie Eilish",id:"pbMwTqkKSps"},{tt:"The Weeknd - Call Out My Name",ar:"The Weeknd",id:"P9t9jHus3EU"},{tt:"Lewis Capaldi - Someone You Loved",ar:"Lewis Capaldi",id:"zABZyAoxXqk"},{tt:"Olivia Rodrigo - drivers license",ar:"Olivia Rodrigo",id:"ZmDBbnmKpqQ"},{tt:"Hozier - Take Me To Church",ar:"Hozier",id:"PVjiKRfKpPI"},{tt:"Bon Iver - Skinny Love",ar:"Bon Iver",id:"ssdgMomZqMI"},{tt:"Ed Sheeran - The A Team",ar:"Ed Sheeran",id:"UAWcs5H-qgQ"},{tt:"Phoebe Bridgers - Motion Sickness",ar:"Phoebe Bridgers",id:"GwLMDpbHvSY"},{tt:"Sufjan Stevens - Death With Dignity",ar:"Sufjan Stevens",id:"lN0uOKPxGcE"},{tt:"Damien Rice - The Blower's Daughter",ar:"Damien Rice",id:"RWJ8TqLMeAo"}]}
  }
};
RES.ru={
  A:{...RES.uz.A,v:"Антидот от стресса",d:"Вы сейчас на грани взрыва. Два пути: выплеснуть или успокоиться."},
  B:{...RES.uz.B,v:"Танцы и кайф",d:"Энергия есть, а музыки — нет. Никаких сценариев, только танец."},
  C:{...RES.uz.C,v:"Перекур для мозга",d:"Устали от работы, учёбы или людей. Нужен приятный, ненавязчивый фон."},
  D:{...RES.uz.D,v:"Лирика / Тишина",d:"Немного одиноко или тихое жизненное настроение. Треки для наушников."}
};
RES.en={
  A:{...RES.uz.A,v:"Stress Antidote",d:"You're on the verge of exploding. Two paths: release it or calm down."},
  B:{...RES.uz.B,v:"Dance & Vibes",d:"Energy is here, music is not. No script — just pure dance."},
  C:{...RES.uz.C,v:"Brain Break",d:"Tired of work, study or people. Just need a pleasant, non-demanding background."},
  D:{...RES.uz.D,v:"Lyrics & Silence",d:"A little lonely or quiet life mood. Tracks for headphones, alone."}
};

const LT = {
  uz:{trend:"🔥 Trending hozir — bosing va tinglang",q:"Savol",of:"dan",restart:"🔄 Qaytadan boshlash",songs:"🎧 Siz uchun qo'shiqlar",mdiv:"🎭 Kayfiyat Testi",iph:"Artist, albom yoki qo'shiq nomi...",isub:"Artist, albom yoki qo'shiq haqida biror narsa so'rang."},
  ru:{trend:"🔥 Сейчас в тренде — нажмите и слушайте",q:"Вопрос",of:"из",restart:"🔄 Начать заново",songs:"🎧 Треки для вас",mdiv:"🎭 Тест настроения",iph:"Имя артиста, альбома или песни...",isub:"Расскажи об артисте, альбоме или песне."},
  en:{trend:"🔥 Trending Now — click and listen",q:"Question",of:"of",restart:"🔄 Start Over",songs:"🎧 Songs for you",mdiv:"🎭 Mood Test",iph:"Artist, album or song name...",isub:"Ask about any artist, album or song."}
};

// ── MUSIC DB ────────────────────────────────
const DB = [
  {n:"The Weeknd",a:["the weeknd","weeknd","уикенд"],e:"🌃",p:"https://img.youtube.com/vi/4NRXx6U8ABQ/mqdefault.jpg",
   tg:"Kanadalik R&B/Pop yulduzi",
   f:[{k:"Janr",v:"R&B, Pop, Synth-pop"},{k:"Mamlakat",v:"Kanada"},{k:"Faoliyati",v:"2010 - hozirgacha"}],
   s:[{t:"Biografiya",i:"📖",tp:"prose",c:"Abel Tesfaye (The Weeknd) - zamonaviy R&B sohasidagi eng katta yulduzlardan biri. Uning 80-yillar sintipopiga yaqin uslubi butun dunyo bo'ylab milliardlab tinglashlarga ega bo'ldi."},
     {t:"Albomlar",i:"💿",tp:"albums",c:[{n:"Beauty Behind the Madness",y:"2015"},{n:"Starboy",y:"2016"},{n:"After Hours",y:"2020"},{n:"Dawn FM",y:"2022"}]},
     {t:"Top qo'shiqlar",i:"🎵",tp:"tracks",c:[{t:"Blinding Lights",id:"4NRXx6U8ABQ"},{t:"Starboy",id:"34Na4j8AVgA"},{t:"The Hills",id:"yzTuBuRdAyA"},{t:"Can't Feel My Face",id:"KEI4qSrkPAs"},{t:"Save Your Tears",id:"XXYlFuWEuKI"}]}],
   sm:"The Weeknd zamonaviy pop/R&B sahnasidagi eng nufuzli ijrochilardan biri."},
  {n:"Drake",a:["drake","дрейк"],e:"🦉",p:"https://img.youtube.com/vi/xpVfcZ0ZcFM/mqdefault.jpg",
   tg:"Kanadalik rap yulduzi, eng ko'p Billboard rekordlari sohibi",
   f:[{k:"Janr",v:"Hip-Hop, R&B"},{k:"Mamlakat",v:"Kanada"},{k:"Faoliyati",v:"2006 - hozirgacha"}],
   s:[{t:"Biografiya",i:"📖",tp:"prose",c:"Drake zamonaviy hip-hop sanoatining eng muvaffaqiyatli va eng ko'p Billboard rekordlarini o'rnatgan artistlaridan biri."},
     {t:"Albomlar",i:"💿",tp:"albums",c:[{n:"Take Care",y:"2011"},{n:"Views",y:"2016"},{n:"Scorpion",y:"2018"},{n:"Certified Lover Boy",y:"2021"}]},
     {t:"Top qo'shiqlar",i:"🎵",tp:"tracks",c:[{t:"God's Plan",id:"xpVfcZ0ZcFM"},{t:"One Dance",id:"iHCn3a3YIOU"},{t:"Hotline Bling",id:"uxpDa-c-4Mc"},{t:"In My Feelings",id:"DRS_PpOrUZ4"},{t:"Started From the Bottom",id:"RubczQuh47k"}]}],
   sm:"Drake hip-hop sanoatining eng nufuzli figuralaridan biri."},
  {n:"Eminem",a:["eminem","эминем","marshall mathers"],e:"🎤",p:"https://img.youtube.com/vi/_Yhyp-_hX2s/mqdefault.jpg",
   tg:"Rap legendasi, eng ko'p sotilgan reperlardan biri",
   f:[{k:"Janr",v:"Hip-Hop, Rap"},{k:"Mamlakat",v:"AQSH"},{k:"Faoliyati",v:"1996 - hozirgacha"}],
   s:[{t:"Biografiya",i:"📖",tp:"prose",c:"Eminem tezkor va texnik jihatdan murakkab rep uslubi bilan hip-hop tarixidagi eng nufuzli artistlardan biriga aylandi."},
     {t:"Albomlar",i:"💿",tp:"albums",c:[{n:"The Marshall Mathers LP",y:"2000"},{n:"The Eminem Show",y:"2002"},{n:"Recovery",y:"2010"},{n:"Curtain Call",y:"2005"}]},
     {t:"Top qo'shiqlar",i:"🎵",tp:"tracks",c:[{t:"Lose Yourself",id:"_Yhyp-_hX2s"},{t:"Not Afraid",id:"j5-yKhDd64s"},{t:"Stan",id:"gOMhN-hfMtY"},{t:"Without Me",id:"YVkUvmDQ3HY"},{t:"Love the Way You Lie",id:"uelHwf8o7_U"}]}],
   sm:"Eminem hip-hop tarixidagi eng texnik va ta'sirli reperlardan biri."},
  {n:"Billie Eilish",a:["billie eilish","билли айлиш"],e:"🖤",p:"https://img.youtube.com/vi/DyDfgMOUjCI/mqdefault.jpg",
   tg:"Amerikalik pop yulduzi, alternativ uslubi bilan tanilgan",
   f:[{k:"Janr",v:"Pop, Alternative"},{k:"Mamlakat",v:"AQSH"},{k:"Faoliyati",v:"2015 - hozirgacha"}],
   s:[{t:"Biografiya",i:"📖",tp:"prose",c:"Billie Eilish o'zining shivirlovchi vokal uslubi va qoraygan, alternativ pop sound'i bilan yosh avlod orasida juda mashhur bo'ldi."},
     {t:"Albomlar",i:"💿",tp:"albums",c:[{n:"When We All Fall Asleep",y:"2019"},{n:"Happier Than Ever",y:"2021"},{n:"Hit Me Hard and Soft",y:"2024"}]},
     {t:"Top qo'shiqlar",i:"🎵",tp:"tracks",c:[{t:"Bad Guy",id:"DyDfgMOUjCI"},{t:"Ocean Eyes",id:"viimfQi_pUw"},{t:"Happier Than Ever",id:"5GJWxDKyk3A"},{t:"Birds of a Feather",id:"_XYLD-gOe0I"},{t:"Lovely",id:"AKlqpxFtS2k"}]}],
   sm:"Billie Eilish zamonaviy alternativ pop sohasining eng noyob ovozlaridan biri."},
  {n:"Taylor Swift",a:["taylor swift","тейлор свифт"],e:"🎀",p:"https://img.youtube.com/vi/nfWlot6h_JM/mqdefault.jpg",
   tg:"Amerikalik pop/country yulduzi, eng ko'p mukofotga ega",
   f:[{k:"Janr",v:"Pop, Country, Folk-pop"},{k:"Mamlakat",v:"AQSH"},{k:"Faoliyati",v:"2006 - hozirgacha"}],
   s:[{t:"Biografiya",i:"📖",tp:"prose",c:"Taylor Swift country sahnasidan boshlab, pop musiqaning eng yirik yulduziga aylangan. U o'z qo'shiqlarini o'zi yozadi."},
     {t:"Albomlar",i:"💿",tp:"albums",c:[{n:"1989",y:"2014"},{n:"Reputation",y:"2017"},{n:"Folklore",y:"2020"},{n:"Midnights",y:"2022"}]},
     {t:"Top qo'shiqlar",i:"🎵",tp:"tracks",c:[{t:"Shake It Off",id:"nfWlot6h_JM"},{t:"Blank Space",id:"e-ORhEE9VVg"},{t:"Anti-Hero",id:"b1kbLwvqugk"},{t:"Love Story",id:"8xg3vE8Ie_E"},{t:"Cruel Summer",id:"ic8j13piAhQ"}]}],
   sm:"Taylor Swift zamonaviy pop musiqaning eng nufuzli ijrochisi hisoblanadi."},
  {n:"Ed Sheeran",a:["ed sheeran","эд ширан"],e:"🎸",p:"https://img.youtube.com/vi/JGwWNGJdvx8/mqdefault.jpg",
   tg:"Britaniyalik pop/akustik gitarachi va bastakor",
   f:[{k:"Janr",v:"Pop, Folk-pop, Acoustic"},{k:"Mamlakat",v:"Buyuk Britaniya"},{k:"Faoliyati",v:"2011 - hozirgacha"}],
   s:[{t:"Biografiya",i:"📖",tp:"prose",c:"Ed Sheeran gitara bilan kontsert berishdan boshlab, dunyo bo'ylab eng ko'p sotuvchi pop artistlardan biriga aylandi."},
     {t:"Albomlar",i:"💿",tp:"albums",c:[{n:"+ (Plus)",y:"2011"},{n:"x (Multiply)",y:"2014"},{n:"÷ (Divide)",y:"2017"},{n:"= (Equals)",y:"2021"}]},
     {t:"Top qo'shiqlar",i:"🎵",tp:"tracks",c:[{t:"Shape of You",id:"JGwWNGJdvx8"},{t:"Perfect",id:"2Vv-BfVoq4g"},{t:"Thinking Out Loud",id:"lp-EO5I60KA"},{t:"Photograph",id:"nSDgHBxUbVQ"},{t:"Bad Habits",id:"orJSJGHjBLI"}]}],
   sm:"Ed Sheeran zamonaviy pop musiqaning eng yumshoq va ommabop ovozlaridan biri."},
  {n:"Adele",a:["adele","адель"],e:"🎤",p:"https://img.youtube.com/vi/rYEDA3JcQqw/mqdefault.jpg",
   tg:"Britaniyalik soul/pop, kuchli vokal ovozi",
   f:[{k:"Janr",v:"Soul, Pop, Ballad"},{k:"Mamlakat",v:"Buyuk Britaniya"},{k:"Faoliyati",v:"2006 - hozirgacha"}],
   s:[{t:"Biografiya",i:"📖",tp:"prose",c:"Adele o'zining kuchli va his-tuyg'uga boy ovozi bilan butun dunyoda tanilgan."},
     {t:"Albomlar",i:"💿",tp:"albums",c:[{n:"19",y:"2008"},{n:"21",y:"2011"},{n:"25",y:"2015"},{n:"30",y:"2021"}]},
     {t:"Top qo'shiqlar",i:"🎵",tp:"tracks",c:[{t:"Rolling in the Deep",id:"rYEDA3JcQqw"},{t:"Someone Like You",id:"hLQl3WQQoQ0"},{t:"Hello",id:"YQHsXMglC9A"},{t:"Set Fire to the Rain",id:"Ri7-vnrJD3k"},{t:"Easy on Me",id:"U3ASj1L6_sY"}]}],
   sm:"Adele zamonaviy soul-pop musiqaning eng kuchli ovozlaridan biri."},
  {n:"Ariana Grande",a:["ariana grande","ариана гранде"],e:"🎀",p:"https://img.youtube.com/vi/gl1aHhXnN1k/mqdefault.jpg",
   tg:"Amerikalik pop/R&B, keng diapazonli ovoz",
   f:[{k:"Janr",v:"Pop, R&B"},{k:"Mamlakat",v:"AQSH"},{k:"Faoliyati",v:"2008 - hozirgacha"}],
   s:[{t:"Biografiya",i:"📖",tp:"prose",c:"Ariana Grande aktrisalikdan musiqaga o'tib, zamonaviy pop musiqaning yetakchi ovozlaridan biriga aylandi."},
     {t:"Albomlar",i:"💿",tp:"albums",c:[{n:"Dangerous Woman",y:"2016"},{n:"Sweetener",y:"2018"},{n:"Thank U, Next",y:"2019"},{n:"Eternal Sunshine",y:"2024"}]},
     {t:"Top qo'shiqlar",i:"🎵",tp:"tracks",c:[{t:"Thank U, Next",id:"gl1aHhXnN1k"},{t:"7 Rings",id:"QYh6mYIJG2Y"},{t:"No Tears Left to Cry",id:"ffxKSjUwKdU"},{t:"Problem",id:"iS1g8G_njx8"},{t:"Positions",id:"tcYodQoapMg"}]}],
   sm:"Ariana Grande zamonaviy pop-R&B sohasining eng kuchli vokalchilaridan biri."},
  {n:"Beyoncé",a:["beyonce","beyoncé","бейонсе"],e:"👑",p:"https://img.youtube.com/vi/bnVUHWCynig/mqdefault.jpg",
   tg:"Amerikalik R&B/Pop qirolichasi, Grammy rekordchisi",
   f:[{k:"Janr",v:"R&B, Pop, Soul"},{k:"Mamlakat",v:"AQSH"},{k:"Faoliyati",v:"1997 - hozirgacha"}],
   s:[{t:"Biografiya",i:"📖",tp:"prose",c:"Beyoncé Destiny's Child guruhidan boshlab, mustaqil ravishda zamonaviy R&B va pop musiqaning eng nufuzli ovozlaridan biriga aylandi."},
     {t:"Albomlar",i:"💿",tp:"albums",c:[{n:"Dangerously in Love",y:"2003"},{n:"Lemonade",y:"2016"},{n:"Renaissance",y:"2022"},{n:"Cowboy Carter",y:"2024"}]},
     {t:"Top qo'shiqlar",i:"🎵",tp:"tracks",c:[{t:"Halo",id:"bnVUHWCynig"},{t:"Single Ladies",id:"4m1EFMoRFvY"},{t:"Crazy in Love",id:"ViwtNLUqkMY"},{t:"Formation",id:"WDZJPJV__bQ"},{t:"Texas Hold 'Em",id:"SdMODhMlyMY"}]}],
   sm:"Beyoncé zamonaviy musiqa sanoatining eng ko'p mukofotlangan yulduzlaridan biri."},
  {n:"Michael Jackson",a:["michael jackson","майкл джексон"],e:"🕺",p:"https://img.youtube.com/vi/Zi_XLOBDo_Y/mqdefault.jpg",
   tg:"'Pop qiroli', musiqa tarixidagi eng ta'sirli san'atkor",
   f:[{k:"Janr",v:"Pop, R&B, Funk"},{k:"Mamlakat",v:"AQSH"},{k:"Faoliyati",v:"1964-2009"}],
   s:[{t:"Biografiya",i:"📖",tp:"prose",c:"Michael Jackson dunyo tarixidagi eng katta sotuvchi va eng ta'sirli pop ijrochisiga aylandi. Raqs uslubi va video-kliplari musiqa sanoatini o'zgartirdi."},
     {t:"Albomlar",i:"💿",tp:"albums",c:[{n:"Off the Wall",y:"1979"},{n:"Thriller",y:"1982"},{n:"Bad",y:"1987"},{n:"Dangerous",y:"1991"}]},
     {t:"Top qo'shiqlar",i:"🎵",tp:"tracks",c:[{t:"Billie Jean",id:"Zi_XLOBDo_Y"},{t:"Thriller",id:"sOnqjkJTMaA"},{t:"Beat It",id:"oRdxUFDoQe0"},{t:"Smooth Criminal",id:"h_D3VFfhvs4"},{t:"Man in the Mirror",id:"PivWY9wn5ps"}]}],
   sm:"Michael Jackson 'Pop qiroli' sifatida musiqa tarixiga abadiy muhrlangan."},
  {n:"Bruno Mars",a:["bruno mars","бруно марс"],e:"🎩",p:"https://img.youtube.com/vi/OPf0YbXqDm0/mqdefault.jpg",
   tg:"Amerikalik pop/funk, sahna mahorati bilan tanilgan",
   f:[{k:"Janr",v:"Pop, Funk, R&B"},{k:"Mamlakat",v:"AQSH"},{k:"Faoliyati",v:"2004 - hozirgacha"}],
   s:[{t:"Biografiya",i:"📖",tp:"prose",c:"Bruno Mars zamonaviy pop musiqaga 70-80-yillar funk va soul uslublarini qaytargan ijrochi."},
     {t:"Albomlar",i:"💿",tp:"albums",c:[{n:"Doo-Wops & Hooligans",y:"2010"},{n:"Unorthodox Jukebox",y:"2012"},{n:"24K Magic",y:"2016"}]},
     {t:"Top qo'shiqlar",i:"🎵",tp:"tracks",c:[{t:"Uptown Funk",id:"OPf0YbXqDm0"},{t:"24K Magic",id:"UqyT8IEBkvY"},{t:"Just the Way You Are",id:"LjhCEhWiKXk"},{t:"That's What I Like",id:"PMivT7MJ41M"},{t:"Grenade",id:"XjVNlgyjcpM"}]}],
   sm:"Bruno Mars zamonaviy pop-funk uslubining eng ko'zga ko'ringan vakili."},
  {n:"Coldplay",a:["coldplay","колдплей"],e:"🌈",p:"https://img.youtube.com/vi/dvgZkm1xWPE/mqdefault.jpg",
   tg:"Britaniyalik rok guruhi, eng ko'p tinglanadigan jamoalardan biri",
   f:[{k:"Janr",v:"Alternative Rock, Pop Rock"},{k:"Mamlakat",v:"Buyuk Britaniya"},{k:"Faoliyati",v:"1996 - hozirgacha"}],
   s:[{t:"Biografiya",i:"📖",tp:"prose",c:"Coldplay - Chris Martin boshchiligidagi guruh, katta stadion kontsertlari bilan mashhur."},
     {t:"Albomlar",i:"💿",tp:"albums",c:[{n:"Parachutes",y:"2000"},{n:"A Rush of Blood",y:"2002"},{n:"Viva la Vida",y:"2008"},{n:"Music of the Spheres",y:"2021"}]},
     {t:"Top qo'shiqlar",i:"🎵",tp:"tracks",c:[{t:"Yellow",id:"yKNxeF4KMsY"},{t:"Viva la Vida",id:"dvgZkm1xWPE"},{t:"The Scientist",id:"RB-RcX5DS5A"},{t:"Paradise",id:"1G4isv_Fylg"},{t:"Hymn for the Weekend",id:"YykjpeuMNEk"}]}],
   sm:"Coldplay dunyodagi eng katta stadion-rok guruhlaridan biri."},
  {n:"Imagine Dragons",a:["imagine dragons","имеджин драгонс"],e:"🐉",p:"https://img.youtube.com/vi/W2TE0DjdNqI/mqdefault.jpg",
   tg:"Amerikalik rok guruhi, anthem-xitlari bilan tanilgan",
   f:[{k:"Janr",v:"Alternative Rock, Electronic"},{k:"Mamlakat",v:"AQSH"},{k:"Faoliyati",v:"2008 - hozirgacha"}],
   s:[{t:"Biografiya",i:"📖",tp:"prose",c:"Imagine Dragons rok va elektron musiqani birlashtirib, kuchli va keng auditoriyaga mos qo'shiqlar yaratadi."},
     {t:"Albomlar",i:"💿",tp:"albums",c:[{n:"Night Visions",y:"2012"},{n:"Evolve",y:"2017"},{n:"Mercury Act 1",y:"2021"},{n:"Mercury Act 2",y:"2022"}]},
     {t:"Top qo'shiqlar",i:"🎵",tp:"tracks",c:[{t:"Believer",id:"W2TE0DjdNqI"},{t:"Radioactive",id:"ktvTqknDobU"},{t:"Thunder",id:"fKopy74weus"},{t:"Demons",id:"mWRsgZuwf_8"},{t:"Enemy",id:"D9G1VOjN_84"}]}],
   sm:"Imagine Dragons zamonaviy alternativ-pop-rok sohasining eng ommabop guruhlaridan biri."},
  {n:"Dua Lipa",a:["dua lipa","дуа липа"],e:"✨",p:"https://img.youtube.com/vi/DyHkM3YFQVY/mqdefault.jpg",
   tg:"Britaniyalik pop/disko-pop yulduzi",
   f:[{k:"Janr",v:"Pop, Disco-pop, Dance"},{k:"Mamlakat",v:"Buyuk Britaniya"},{k:"Faoliyati",v:"2015 - hozirgacha"}],
   s:[{t:"Biografiya",i:"📖",tp:"prose",c:"Dua Lipa zamonaviy pop musiqaga 70-80-yillar disko ta'sirini qaytargan eng yorqin ovozlardan biri."},
     {t:"Albomlar",i:"💿",tp:"albums",c:[{n:"Dua Lipa",y:"2017"},{n:"Future Nostalgia",y:"2020"},{n:"Radical Optimism",y:"2024"}]},
     {t:"Top qo'shiqlar",i:"🎵",tp:"tracks",c:[{t:"Levitating",id:"TUVcZfQe-Kw"},{t:"Don't Start Now",id:"oygrmKOqttA"},{t:"New Rules",id:"k2qgadSvNyU"},{t:"IDGAF",id:"DyHkM3YFQVY"},{t:"Houdini",id:"5OBDFaLCDzQ"}]}],
   sm:"Dua Lipa 2020-yillar pop-disko uyg'onishining yetakchi ovozi."},
  {n:"Rihanna",a:["rihanna","рианна"],e:"💎",p:"https://img.youtube.com/vi/CvBqzbB9-rk/mqdefault.jpg",
   tg:"Barbadoslik pop/R&B yulduzi va tadbirkor",
   f:[{k:"Janr",v:"Pop, R&B, Dancehall"},{k:"Mamlakat",v:"Barbados"},{k:"Faoliyati",v:"2005 - hozirgacha"}],
   s:[{t:"Biografiya",i:"📖",tp:"prose",c:"Rihanna 2000-yillar oxiri va 2010-yillarning eng muvaffaqiyatli pop yulduzlaridan biri, keyinchalik Fenty brendi orqali biznesda ham muvaffaqiyatga erishdi."},
     {t:"Albomlar",i:"💿",tp:"albums",c:[{n:"Good Girl Gone Bad",y:"2007"},{n:"Loud",y:"2010"},{n:"Talk That Talk",y:"2011"},{n:"Anti",y:"2016"}]},
     {t:"Top qo'shiqlar",i:"🎵",tp:"tracks",c:[{t:"Umbrella",id:"CvBqzbB9-rk"},{t:"Diamonds",id:"lWA2pjMjpBs"},{t:"We Found Love",id:"tg00YEETFzg"},{t:"Work",id:"HL1UzIK-flA"},{t:"Stay",id:"JF8BRvqGCNs"}]}],
   sm:"Rihanna 2000-2010 yillar pop musiqasining eng muhim ovozlaridan biri."},
  {n:"Скриптонит",a:["скриптонит","scriptonite","адиль жалелов"],e:"🎙️",p:"https://img.youtube.com/vi/lFYCMo3UGCY/mqdefault.jpg",
   tg:"Qozoqstonlik reper, MDH hip-hopiga katta ta'sir ko'rsatgan",
   f:[{k:"Janr",v:"Hip-Hop, Trip-hop"},{k:"Mamlakat",v:"Qozoqiston"},{k:"Faoliyati",v:"2010 - hozirgacha"}],
   s:[{t:"Biografiya",i:"📖",tp:"prose",c:"Скриптонит (Adil Jalelov) o'ziga xos atmosferik prodyuserlik va melanxolik rep uslubi bilan butun MDH hududidagi hip-hop sahnasiga katta ta'sir ko'rsatgan."},
     {t:"Albomlar",i:"💿",tp:"albums",c:[{n:"Кто убил Марка?",y:"2014"},{n:"Праздник",y:"2017"}]},
     {t:"Top qo'shiqlar",i:"🎵",tp:"tracks",c:[{t:"Чёрный лексус"},{t:"Юность"},{t:"Иногда"},{t:"Слова"},{t:"Розовое вино"}]}],
   sm:"Скриптонит Qozoqistondan chiqqan, MDH hip-hop sahnasiga eng katta ta'sir ko'rsatgan reperlardan biri."},
  {n:"BAKR",a:["bakr","бакр","bakar"],e:"🎙️",p:"https://img.youtube.com/vi/Rn5GNpGSrMQ/mqdefault.jpg",
   tg:"Qirg'izistonlik reper, qirg'iz trap sahnasining yetakchisi",
   f:[{k:"Janr",v:"Hip-Hop, Trap"},{k:"Mamlakat",v:"Qirg'iziston"},{k:"Faoliyati",v:"2015 - hozirgacha"}],
   s:[{t:"Biografiya",i:"📖",tp:"prose",c:"BAKR — Qirg'izistondan chiqqan zamonaviy trap va hip-hop ijrochisi. Qirg'iz va rus tillarida ijro etib, MDH yoshlari orasida katta muxlislar to'plagan."},
     {t:"Top qo'shiqlar",i:"🎵",tp:"tracks",c:[{t:"BAKR - Пустота",id:"Rn5GNpGSrMQ"},{t:"BAKR - Больно"},{t:"BAKR - Холодно"},{t:"BAKR - Дорога"},{t:"BAKR - Небо"}]},
     {t:"Uslub",i:"🎨",tp:"tags",c:["Trap","Hip-Hop","Qirg'iz rap","MDH rap","Yoshlar"]}],
   sm:"BAKR Qirg'iziston rap sahnasining eng tanilgan vakili."},
  {n:"Ulukmanapo",a:["ulukmanapo","улукманапо","улук"],e:"🎙️",p:"https://img.youtube.com/vi/2K7PPMdFOq0/mqdefault.jpg",
   tg:"Qirg'izistonlik rep/trap ijrochisi",
   f:[{k:"Janr",v:"Rap, Trap"},{k:"Mamlakat",v:"Qirg'iziston"},{k:"Faoliyati",v:"2015 - hozirgacha"}],
   s:[{t:"Biografiya",i:"📖",tp:"prose",c:"Ulukmanapo — qirg'iz trap va rep musiqasining eng yorqin vakili. Qirg'iz va rus tillarida ijro etib, katta auditoriya to'plagan."},
     {t:"Top qo'shiqlar",i:"🎵",tp:"tracks",c:[{t:"Бишкек",id:"2K7PPMdFOq0"},{t:"Улук",id:"dP1sSZZkDr4"},{t:"Асфальт",id:"XMh4GqWJVFk"},{t:"Мечта",id:"HVLyO2jAMiw"},{t:"Горы"}]},
     {t:"Uslub",i:"🎨",tp:"tags",c:["Trap","Qirg'iz rap","Street","Yoshlar"]}],
   sm:"Ulukmanapo qirg'iz rep sahnasida o'z yo'lini topgan ijrochi."},
  {n:"Земфира",a:["земфира","zemfira"],e:"🎸",p:"https://img.youtube.com/vi/vTQXMRYol5E/mqdefault.jpg",
   tg:"Rossiyalik rok qo'shiqchisi, 90-2000-yillar sahnasining legendasi",
   f:[{k:"Janr",v:"Alternative Rock"},{k:"Mamlakat",v:"Rossiya"},{k:"Faoliyati",v:"1999 - hozirgacha"}],
   s:[{t:"Biografiya",i:"📖",tp:"prose",c:"Земфира rus tilidagi alternativ-rok sahnasining eng nufuzli ijrochilaridan biri. Matnlari chuqur shaxsiy va shoirona uslubda."},
     {t:"Albomlar",i:"💿",tp:"albums",c:[{n:"Zemfira",y:"1999"},{n:"Прости меня моя любовь",y:"2000"},{n:"Спасибо",y:"2007"}]},
     {t:"Top qo'shiqlar",i:"🎵",tp:"tracks",c:[{t:"Хочешь?"},{t:"Аривидерчи"},{t:"Искала"},{t:"Сигареты"},{t:"Малыш"}]}],
   sm:"Земфира rus rok musiqasining eng nufuzli ovozlaridan biri."},
  {n:"Моргенштерн",a:["моргенштерн","morgenshtern"],e:"🔥",p:"https://img.youtube.com/vi/kKFiGSCMHkI/mqdefault.jpg",
   tg:"Rossiyalik reper va shou-biznes yulduzi",
   f:[{k:"Janr",v:"Hip-Hop, Trap"},{k:"Mamlakat",v:"Rossiya"},{k:"Faoliyati",v:"2017 - hozirgacha"}],
   s:[{t:"Biografiya",i:"📖",tp:"prose",c:"Моргенштерн (Алишер Валеев) provokatsion uslubi bilan rus trap-rep sahnasining eng yirik yulduzlaridan biriga aylandi."},
     {t:"Albomlar",i:"💿",tp:"albums",c:[{n:"Million Dollar: Original",y:"2021"}]},
     {t:"Top qo'shiqlar",i:"🎵",tp:"tracks",c:[{t:"Cadillac"},{t:"Show"},{t:"Bling-Bling"},{t:"Кто бы мог подумать"},{t:"Family"}]}],
   sm:"Моргенштерн 2020-yillar rus trap-rep madaniyatining eng ko'zga ko'ringan vakili."},
  {n:"Макс Корж",a:["макс корж","max korzh"],e:"🎸",
   tg:"Belarusiyalik pop-rep ijrochisi",
   f:[{k:"Janr",v:"Hip-Hop, Pop-rap"},{k:"Mamlakat",v:"Belarus"},{k:"Faoliyati",v:"2010 - hozirgacha"}],
   s:[{t:"Biografiya",i:"📖",tp:"prose",c:"Макс Корж rus tilidagi pop-rep sahnasida juda katta muxlislar bazasiga ega, katta stadion kontsertlari bilan mashhur."},
     {t:"Top qo'shiqlar",i:"🎵",tp:"tracks",c:[{t:"Сэнсэй"},{t:"Гнев"},{t:"Розовое вино"},{t:"Огонь"},{t:"Иногда"}]}],
   sm:"Макс Корж rus tilidagi pop-rep sahnasining eng katta stadion yulduzlaridan biri."}
];

// ════════════════════════════════════════════
// STATE
// ════════════════════════════════════════════
let lang = "uz";
let ans = [], done = false;

// ════════════════════════════════════════════
// PAGE NAV
// ════════════════════════════════════════════
function goPage(id, btn){
  document.querySelectorAll(".page").forEach(p=>p.classList.remove("on"));
  document.querySelectorAll(".ntab").forEach(b=>b.classList.remove("on"));
  document.getElementById("pg-"+id).classList.add("on");
  if(btn) btn.classList.add("on");
}

// ════════════════════════════════════════════
// LANG
// ════════════════════════════════════════════
document.getElementById("langs").addEventListener("click", e=>{
  const b = e.target.closest(".lb"); if(!b) return;
  document.querySelectorAll(".lb").forEach(x=>x.classList.remove("on"));
  b.classList.add("on");
  lang = b.dataset.l;
  const t = LT[lang];
  document.getElementById("trend-lbl").textContent = t.trend;
  document.getElementById("mood-divider-lbl").textContent = t.mdiv;
  document.getElementById("iwsub").textContent = t.isub;
  document.getElementById("sinput").placeholder = t.iph;
  renderTest();
});

// ════════════════════════════════════════════
// GENRE GRID
// ════════════════════════════════════════════
function buildGrid(){
  const g = document.getElementById("genre-grid");
  GENRES.forEach(genre=>{
    const c = document.createElement("div");
    c.className = "gcard";
    c.innerHTML = `<img src="https://img.youtube.com/vi/${genre.ytId}/mqdefault.jpg" alt=""
      onerror="this.outerHTML='<div class=gcard-ph>${genre.icon}</div>'">
      <div class="gcard-info">
        <div class="glabel">${genre.label}</div>
        <div class="gtrack">${genre.track}</div>
        <div class="gartist">${genre.artist}</div>
      </div>`;
    c.onclick = ()=>openModal(genre);
    g.appendChild(c);
  });
}

function openModal(genre){
  const songs = GENRE_SONGS[genre.label]||[];
  document.getElementById("mlbl").textContent = genre.label;
  document.getElementById("mtitle").innerHTML = `${genre.icon} Top ${songs.length} Qo'shiqlar`;
  const list = document.getElementById("mlist");
  list.innerHTML = "";
  songs.forEach((s,i)=>{
    const a = document.createElement("a");
    a.className = "mtrack"; a.href = `https://www.youtube.com/watch?v=${s.ytId}`;
    a.target = "_blank"; a.rel = "noopener";
    a.innerHTML = `<div class="mnum">${i+1}</div>
      <img class="mthumb" src="https://img.youtube.com/vi/${s.ytId}/mqdefault.jpg"
        onerror="this.outerHTML='<div class=mthumb-ph>🎵</div>'">
      <div class="minfo"><div class="mtitle">${s.title}</div><div class="martist">${s.artist}</div></div>
      <span class="myt">▶ YT</span>`;
    list.appendChild(a);
  });
  document.getElementById("overlay").classList.add("on");
  document.body.style.overflow = "hidden";
}
function closeModal(e){
  if(!e || e.target===document.getElementById("overlay")){
    document.getElementById("overlay").classList.remove("on");
    document.body.style.overflow = "";
  }
}

// ════════════════════════════════════════════
// MOOD TEST
// ════════════════════════════════════════════
function renderTest(){
  const sec = document.getElementById("test-sec");
  sec.innerHTML = "";
  if(done){ renderResult(sec); return; }
  const t = LT[lang], qs = Q[lang], cur = ans.length;
  const pct = Math.round((cur/4)*100);
  const dots = [0,1,2,3].map(i=>`<div class="dot ${i<cur?'done':i===cur?'cur':''}"></div>`).join("");
  const card = document.createElement("div");
  card.className = "qcard";
  card.innerHTML = `
    <div class="prog-row"><span class="prog-lbl">${t.q} ${cur+1} ${t.of} 4</span><span class="prog-pct">${pct}%</span></div>
    <div class="prog-bar"><div class="prog-fill" style="width:${pct}%"></div></div>
    <div class="dots">${dots}</div>
    <div class="qnum">${t.q} ${cur+1}</div>
    <div class="qtext">${qs[cur].t}</div>
    <div class="opts" id="qopts"></div>`;
  sec.appendChild(card);
  const opts = document.getElementById("qopts");
  qs[cur].o.forEach(o=>{
    const btn = document.createElement("button");
    btn.className = "opt";
    btn.innerHTML = `<div class="okey">${o.k}</div><div class="opt-content"><div class="olabel">${o.l}</div>${o.s?`<div class="osub">${o.s}</div>`:""}</div>`;
    btn.onclick = ()=>{
      opts.querySelectorAll(".opt").forEach(b=>b.classList.remove("sel"));
      btn.classList.add("sel");
      setTimeout(()=>{ ans.push(o.k); if(ans.length===4)done=true; renderTest(); }, 280);
    };
    opts.appendChild(btn);
  });
}

function winner(){
  const c={A:0,B:0,C:0,D:0}; ans.forEach(a=>c[a]++);
  return Object.entries(c).sort((x,y)=>y[1]-x[1])[0][0];
}

function renderResult(sec){
  const w = winner(), r = RES[lang][w], t = LT[lang];
  const tags = r.g.map(g=>`<span class="rtag">${g}</span>`).join("");
  const tracks = r.t.map((tr,i)=>{
    const url = tr.id ? `https://www.youtube.com/watch?v=${tr.id}` : `https://www.youtube.com/results?search_query=${encodeURIComponent(tr.tt+" "+tr.ar)}`;
    const thumb = tr.id ? `<img class="tthumb" src="https://img.youtube.com/vi/${tr.id}/mqdefault.jpg" loading="lazy" onerror="this.style.display='none';this.nextElementSibling.style.display='flex'">` : "";
    return `<a class="trow" href="${url}" target="_blank" rel="noopener">
      <div class="tthumb-wrap">
        ${thumb}
        <div class="tthumb-ph" style="${tr.id?"display:none":""}">🎵</div>
        <span class="tnum">${i+1}</span>
      </div>
      <div class="tinfo"><div class="ttitle">${tr.tt}</div><div class="tartist">${tr.ar}</div></div>
      <div class="tyt">▶ YT</div>
    </a>`;
  }).join("");
  sec.innerHTML = `
    <div class="rcard">
      <div class="rbanner">
        <span class="ricon">${r.i}</span>
        <div class="rname">${r.v}</div>
        <div class="rdesc">${r.d}</div>
      </div>
      <div class="rtags">${tags}</div>
      <div class="rth">${t.songs}</div>
      <div class="tlist">${tracks}</div>
    </div>
    <div class="retry-row">
      <button class="rbtn pri" onclick="ans=[];done=false;renderTest()">🔄 ${t.restart}</button>
    </div>`;
}

// ════════════════════════════════════════════
// MUSIC INFO
// ════════════════════════════════════════════
function lev(a,b){
  const m=a.length,n=b.length;
  const d=Array.from({length:m+1},(_,i)=>Array.from({length:n+1},(_,j)=>i===0?j:j===0?i:0));
  for(let i=1;i<=m;i++)for(let j=1;j<=n;j++)d[i][j]=a[i-1]===b[j-1]?d[i-1][j-1]:1+Math.min(d[i-1][j],d[i][j-1],d[i-1][j-1]);
  return d[m][n];
}

function findArtist(text){
  const q = text.toLowerCase().trim();
  let best=null, bestLen=0;
  for(const ar of DB){
    for(const al of ar.a){
      if(q.includes(al.toLowerCase())&&al.length>bestLen){best=ar;bestLen=al.length;}
    }
  }
  if(best) return {ar:best,fuzzy:false};
  let closest=null, minD=Infinity;
  for(const ar of DB){
    for(const al of ar.a){
      const d=lev(q,al.toLowerCase());
      if(d<minD){minD=d;closest=ar;}
    }
  }
  if(closest&&minD<=3) return {ar:closest,fuzzy:true};
  return null;
}

function mkCard(ar, fuzzyQ){
  let h = `<div class="icard">`;
  const photo = ar.p ? `<img class="icard-photo" src="${ar.p}" alt="${ar.n}" onerror="this.outerHTML='<div class=icard-emoji>${ar.e||'🎵'}</div>'">` : `<div class="icard-emoji">${ar.e||'🎵'}</div>`;
  h += `<div class="icard-hdr">${photo}<div><div class="icard-name">${ar.n}</div><div class="icard-tag">${ar.tg||""}</div></div></div>`;
  if(fuzzyQ) h += `<div style="padding:9px 18px 0;font-size:.78rem;color:var(--muted);background:rgba(255,145,0,.06);border-bottom:1px solid var(--border)">🔍 "<b>${fuzzyQ}</b>" topilmadi — <b>${ar.n}</b> ko'rsatilmoqda</div>`;
  h += `<div class="icard-body">`;
  if(ar.f&&ar.f.length){
    h += `<div class="isec"><div class="isec-title"><span>📋</span> Asosiy ma'lumotlar</div>`;
    ar.f.forEach(f=>h+=`<div class="ifact"><span class="ifact-k">${f.k}</span><span class="ifact-v">${f.v}</span></div>`);
    h += `</div>`;
  }
  (ar.s||[]).forEach(sec=>{
    h += `<div class="isec"><div class="isec-title"><span>${sec.i||"📌"}</span> ${sec.t}</div>`;
    if(sec.tp==="prose") h += `<div class="iprose">${sec.c}</div>`;
    else if(sec.tp==="tags") h += `<div class="itags">${sec.c.map(x=>`<span class="itag">${x}</span>`).join("")}</div>`;
    else if(sec.tp==="albums") h += `<div class="ialbums">${sec.c.map(al=>`<div class="ialbum"><div class="ialbum-name">${al.n||al.t||""}</div><div class="ialbum-year">${al.y||""}</div></div>`).join("")}</div>`;
    else if(sec.tp==="tracks") sec.c.forEach((tr,i)=>{
      const hasId = tr.id&&tr.id.length===11;
      const url = hasId ? `https://www.youtube.com/watch?v=${tr.id}` : `https://www.youtube.com/results?search_query=${encodeURIComponent(tr.t||tr)}`;
      const thumb = hasId ? `<img class="itrack-thumb" src="https://img.youtube.com/vi/${tr.id}/mqdefault.jpg" loading="lazy" onerror="this.outerHTML='<div class=itrack-ph>🎵</div>'">` : `<div class="itrack-ph">🎵</div>`;
      h += `<a class="itrack" href="${url}" target="_blank" rel="noopener">
        <div style="position:relative;flex-shrink:0">${thumb}<span class="itrack-num">${i+1}</span></div>
        <div class="itrack-info"><div class="itrack-title">${tr.t||tr}</div></div>
        <div class="itrack-yt">▶ YT</div></a>`;
    });
    h += `</div>`;
  });
  if(ar.sm) h += `<div class="isummary">${ar.sm}</div>`;
  h += `</div></div>`;
  return h;
}

function doSearch(q){
  if(!q) q = document.getElementById("sinput").value.trim();
  if(!q) return;
  document.getElementById("sinput").value = "";
  document.getElementById("iwelcome").style.display = "none";
  const sbtn = document.getElementById("sbtn");
  sbtn.disabled = true;
  const res = document.getElementById("iresults");
  const typing = document.createElement("div");
  typing.className = "typing"; typing.id = "typing-ind";
  typing.innerHTML = `<span></span><span></span><span></span>`;
  res.prepend(typing);
  setTimeout(()=>{
    document.getElementById("typing-ind")?.remove();
    const found = findArtist(q);
    if(found){
      const div = document.createElement("div");
      div.innerHTML = mkCard(found.ar, found.fuzzy?q:null);
      res.prepend(div.firstElementChild);
    } else {
      const nf = document.createElement("div");
      nf.className = "inot-found";
      nf.innerHTML = `<div style="font-size:2rem;margin-bottom:10px">🔍</div><b>"${q}"</b> topilmadi<br><span style="font-size:.83rem;margin-top:5px;display:block">Boshqa nom bilan urinib ko'ring</span>`;
      res.prepend(nf);
    }
    sbtn.disabled = false;
  }, 500);
}

document.getElementById("sinput").addEventListener("keydown", e=>{ if(e.key==="Enter"){e.preventDefault();doSearch("");}});

// ════════════════════════════════════════════
// INIT
// ════════════════════════════════════════════
buildGrid();
renderTest();
</script>
</body>
</html>"""

components.html(HTML, height=3000, scrolling=True)
PYEOF
echo "Lines: $(wc -l < /home/claude/final_app.py)"
