import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="MoodTune AI",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Streamlit standart elementlarini yashirish
st.markdown("""
<style>
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { display: none; }
div[data-testid="stToolbar"] { display: none; }
.stApp { background: #060606 !important; }
</style>
""", unsafe_allow_html=True)

HTML = r"""<!DOCTYPE html>
<html lang="uz">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta http-equiv="Content-Security-Policy" content="default-src * 'unsafe-inline' 'unsafe-eval' data: blob:;">
<title>MoodTune AI</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet" />
<style>
  :root {
    --bg:        #060606;
    --surface:   #111111;
    --surface2:  #1a1a1a;
    --border:    #222222;
    --fire:      #ff5722;
    --fire-glow: #ff9100;
    --text:      #f5f5f5;
    --muted:     #777777;
    --radius:    16px;
    --font-head: 'Space Grotesk', sans-serif;
    --font-mono: 'Space Mono', monospace;
  }
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  body { background: var(--bg); color: var(--text); font-family: var(--font-head); min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }

  /* HEADER */
  header { display: flex; align-items: center; justify-content: space-between; padding: 18px 32px; border-bottom: 1px solid var(--border); position: sticky; top: 0; background: rgba(6,6,6,0.95); backdrop-filter: blur(16px); z-index: 100; flex-wrap: wrap; gap: 10px; }
  .logo-area { display: flex; align-items: center; gap: 14px; }
  .fire-wings { display: flex; align-items: center; width: 44px; height: 24px; }
  .wing { width: 20px; height: 20px; background: linear-gradient(45deg, var(--fire), var(--fire-glow)); filter: drop-shadow(0 0 8px var(--fire)); }
  .wing.left { border-radius: 0 100% 30% 100%; animation: flapLeft 3s ease-in-out infinite alternate; }
  .wing.right { border-radius: 100% 0 100% 30%; animation: flapRight 3s ease-in-out infinite alternate; }
  @keyframes flapLeft { 0% { transform: rotate(-25deg) scaleY(0.9); } 100% { transform: rotate(-5deg) scaleY(1.1); } }
  @keyframes flapRight { 0% { transform: rotate(25deg) scaleY(0.9); } 100% { transform: rotate(5deg) scaleY(1.1); } }
  .logo-text { font-weight: 700; font-size: 1.25rem; letter-spacing: -0.03em; }
  .logo-text span { color: transparent; background: linear-gradient(to right, var(--fire-glow), #fff); -webkit-background-clip: text; background-clip: text; }
  .header-right { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }
  .nav-tabs { display: flex; gap: 4px; background: var(--surface); padding: 4px; border-radius: 10px; border: 1px solid var(--border); }
  .nav-tab { background: none; border: none; color: var(--muted); font-family: var(--font-head); font-size: 0.82rem; font-weight: 600; padding: 7px 14px; cursor: pointer; border-radius: 6px; transition: all 0.2s; white-space: nowrap; }
  .nav-tab.active { background: var(--surface2); color: var(--fire-glow); border: 1px solid rgba(255,87,34,0.2); }
  .lang-panel { display: flex; gap: 4px; background: var(--surface); padding: 4px; border-radius: 10px; border: 1px solid var(--border); }
  .lang-btn { background: none; border: none; color: var(--muted); font-family: var(--font-mono); font-size: 0.75rem; padding: 6px 10px; cursor: pointer; border-radius: 6px; transition: all 0.2s; }
  .lang-btn.active { background: var(--surface2); color: var(--fire-glow); border: 1px solid rgba(255,87,34,0.2); }

  /* PAGES */
  .page { display: none; flex: 1; flex-direction: column; }
  .page.active { display: flex; }

  /* TRENDING & GENRES */
  .trending-section { max-width: 720px; margin: 0 auto; padding: 28px 20px 0; width: 100%; }
  .trending-title { font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; color: var(--muted); margin-bottom: 14px; display: flex; align-items: center; gap: 10px; }
  .trending-title::after { content: ''; flex: 1; height: 1px; background: var(--border); }
  .genre-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin-bottom: 20px; }
  .genre-card { background: var(--surface); border: 1px solid var(--border); border-radius: 12px; overflow: hidden; cursor: pointer; transition: all 0.25s; text-decoration: none; display: block; }
  .genre-card:hover { border-color: var(--fire); transform: translateY(-2px); box-shadow: 0 8px 24px rgba(255,87,34,0.12); }
  .genre-thumb { width: 100%; aspect-ratio: 16/9; object-fit: cover; display: block; background: var(--surface2); }
  .genre-info { padding: 10px 12px; }
  .genre-label { font-size: 0.68rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--fire-glow); margin-bottom: 3px; }
  .genre-track { font-size: 0.85rem; font-weight: 600; color: var(--text); line-height: 1.3; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .genre-artist { font-size: 0.75rem; color: var(--muted); margin-top: 1px; }

  /* CHAT CONTAINER */
  .chat-container { max-width: 720px; margin: 0 auto; padding: 20px 20px 190px; width: 100%; flex: 1; display: flex; flex-direction: column; }
  .messages { display: flex; flex-direction: column; gap: 20px; }
  .msg { display: flex; gap: 14px; max-width: 85%; animation: slideUp 0.4s cubic-bezier(0.16,1,0.3,1); }
  @keyframes slideUp { from { opacity: 0; transform: translateY(16px); } to { opacity: 1; transform: translateY(0); } }
  .msg.bot { align-self: flex-start; }
  .msg.user { align-self: flex-end; flex-direction: row-reverse; }
  .avatar { width: 38px; height: 38px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.1rem; flex-shrink: 0; border: 1px solid var(--border); }
  .msg.bot .avatar { background: linear-gradient(135deg,#222,#111); box-shadow: 0 0 10px rgba(255,87,34,0.15); border-color: rgba(255,87,34,0.3); }
  .msg.user .avatar { background: #ffffff10; }
  .bubble { padding: 14px 20px; border-radius: var(--radius); font-size: 0.98rem; line-height: 1.6; white-space: pre-wrap; word-break: break-word; }
  .msg.bot .bubble { background: var(--surface); border: 1px solid var(--border); border-top-left-radius: 4px; color: #e0e0e0; }
  .msg.user .bubble { background: linear-gradient(135deg, var(--fire), #d84315); color: #fff; border-top-right-radius: 4px; box-shadow: 0 4px 12px rgba(255,87,34,0.2); }

  /* ANALYSIS REPORT & TRACKS */
  .analysis-report { margin-top: 12px; background: rgba(255,255,255,0.01); border: 1px solid rgba(255,87,34,0.2); border-radius: 16px; overflow: hidden; }
  .report-header { background: linear-gradient(135deg, rgba(255,87,34,0.12), rgba(255,145,0,0.06)); padding: 14px 18px; border-bottom: 1px solid rgba(255,87,34,0.15); display: flex; align-items: center; gap: 10px; }
  .report-title { font-weight: 700; font-size: 1rem; color: var(--fire-glow); margin: 0; }
  .mood-meta { padding: 12px 14px 8px; display: flex; flex-wrap: wrap; gap: 7px; }
  .mood-tag { display: inline-flex; align-items: baseline; gap: 5px; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 20px; padding: 5px 11px; }
  .mood-tag-label { color: var(--muted); font-size: 0.68rem; text-transform: uppercase; letter-spacing: 0.07em; }
  .mood-tag-val { color: var(--text); font-weight: 600; font-size: 0.8rem; }
  .tracks-header { padding: 6px 14px 8px; font-size: 0.68rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: var(--muted); display: flex; align-items: center; gap: 8px; }
  .tracks-header::after { content:''; flex:1; height:1px; background: var(--border); }
  .music-card-list { padding: 0 10px 12px; display: flex; flex-direction: column; gap: 5px; }
  .music-track { display: flex; align-items: center; background: rgba(255,255,255,0.025); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px; text-decoration: none; color: #fff; transition: all 0.22s; overflow: hidden; }
  .music-track:hover { background: rgba(255,87,34,0.07); border-color: rgba(255,87,34,0.35); transform: translateX(3px); box-shadow: 0 4px 16px rgba(255,87,34,0.1); }
  .track-thumb-wrap { position: relative; flex-shrink: 0; width: 88px; height: 56px; background: #111; }
  .track-thumb { width: 88px; height: 56px; object-fit: cover; display: block; }
  .track-num-badge { position: absolute; bottom: 3px; right: 3px; min-width: 18px; height: 18px; background: rgba(0,0,0,0.78); border-radius: 4px; font-size: 0.6rem; font-weight: 700; display: flex; align-items: center; justify-content: center; color: #fff; padding: 0 4px; backdrop-filter: blur(4px); }
  .track-info { flex: 1; min-width: 0; padding: 0 12px; }
  .track-title { font-weight: 600; font-size: 0.87rem; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; color: #f0f0f0; }
  .track-artist { font-size: 0.72rem; color: var(--muted); margin-top: 3px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .track-link-icon { flex-shrink: 0; display: flex; align-items: center; gap: 5px; font-family: var(--font-mono); font-size: 0.65rem; font-weight: 700; background: rgba(255,0,0,0.1); border-left: 1px solid rgba(255,255,255,0.05); color: #ff5555; padding: 0 14px; height: 56px; white-space: nowrap; transition: background 0.2s; }
  .music-track:hover .track-link-icon { background: rgba(255,0,0,0.2); }

  /* MUSIC INFO - YANGILANGAN DIZAYN (RASMLAR VA INTERAKTIV DIAGRAMMALAR) */
  .info-rich { margin-top: 4px; }
  .info-artist-banner { display: flex; gap: 20px; background: linear-gradient(135deg, var(--surface2), var(--surface)); border: 1px solid var(--border); border-radius: 16px; padding: 16px; margin-bottom: 20px; align-items: center; }
  .info-artist-img { width: 110px; height: 110px; border-radius: 12px; object-fit: cover; border: 2px solid rgba(255, 87, 34, 0.4); box-shadow: 0 0 15px rgba(255, 87, 34, 0.2); background: #222; }
  
  .info-section { margin-bottom: 16px; }
  .info-section-title { font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: var(--fire-glow); margin-bottom: 10px; display: flex; align-items: center; gap: 6px; }
  .info-section-title::after { content:''; flex:1; height:1px; background: rgba(255,87,34,0.15); }
  
  /* Jonli Diagramma Stili */
  .music-diagram-container { background: var(--surface); border: 1px solid var(--border); border-radius: 14px; padding: 16px; margin: 5px 0 15px 0; }
  .diagram-row { margin-bottom: 12px; }
  .diagram-row:last-child { margin-bottom: 0; }
  .diagram-label-wrap { display: flex; justify-content: space-between; font-size: 0.8rem; margin-bottom: 5px; }
  .diagram-label { font-weight: 600; color: var(--text); }
  .diagram-value { font-family: var(--font-mono); color: var(--fire-glow); font-weight: 700; }
  .diagram-bar-bg { height: 8px; background: #222; border-radius: 4px; overflow: hidden; position: relative; }
  .diagram-bar-fill { height: 100%; background: linear-gradient(90deg, var(--fire), var(--fire-glow)); border-radius: 4px; width: 0%; transition: width 1s cubic-bezier(0.1, 1, 0.1, 1); box-shadow: 0 0 8px var(--fire-glow); }

  /* Albomlar Paneli */
  .info-album-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(130px, 1fr)); gap: 10px; margin-top: 6px; }
  .info-album-card { background: var(--surface2); border: 1px solid var(--border); border-radius: 12px; padding: 8px; font-size: 0.82rem; text-align: center; transition: transform 0.2s, border-color 0.2s; }
  .info-album-card:hover { transform: scale(1.03); border-color: var(--fire); }
  .info-album-img { width: 100%; aspect-ratio: 1/1; object-fit: cover; border-radius: 8px; margin-bottom: 8px; background: #111; display: block; }
  .info-album-name { font-weight: 600; color: var(--text); margin-bottom: 2px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .info-album-year { font-size: 0.72rem; color: var(--muted); }
  
  .info-tag-list { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; }
  .info-tag { background: rgba(255,87,34,0.08); border: 1px solid rgba(255,87,34,0.2); color: var(--fire-glow); padding: 4px 10px; border-radius: 20px; font-size: 0.76rem; }
  .info-prose { font-size: 0.9rem; color: #d0d0d0; line-height: 1.65; }

  /* TYPING LOADER */
  .typing-loader { display: flex; align-items: center; gap: 4px; padding: 6px 4px; }
  .dot { width: 6px; height: 6px; border-radius: 50%; background: var(--muted); animation: wave 1.2s infinite ease-in-out; }
  .dot:nth-child(2) { animation-delay: 0.15s; } .dot:nth-child(3) { animation-delay: 0.3s; }
  @keyframes wave { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-6px); } }

  /* BOTTOM CONTROL PANEL */
  .control-panel { position: fixed; bottom: 0; left: 0; right: 0; background: rgba(6,6,6,0.93); backdrop-filter: blur(20px); border-top: 1px solid var(--border); padding: 14px 20px 18px; z-index: 99; }
  .quick-actions { max-width: 720px; margin: 0 auto 10px; display: flex; gap: 8px; overflow-x: auto; padding-bottom: 2px; scrollbar-width: none; }
  .quick-actions::-webkit-scrollbar { display: none; }
  .recommend-chip { background: rgba(255,87,34,0.1); border: 1px solid rgba(255,87,34,0.3); color: var(--fire-glow); padding: 9px 18px; border-radius: 20px; font-size: 0.86rem; font-weight: 600; cursor: pointer; white-space: nowrap; transition: all 0.3s; display: flex; align-items: center; gap: 6px; }
  .recommend-chip:hover:not(:disabled) { background: var(--fire); color: #fff; box-shadow: 0 0 14px rgba(255,87,34,0.4); transform: translateY(-1px); }
  .input-box { max-width: 720px; margin: 0 auto; display: flex; gap: 10px; align-items: flex-end; }
  .text-box { flex: 1; background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); color: var(--text); font-family: var(--font-head); font-size: 1rem; padding: 13px 16px; resize: none; outline: none; min-height: 50px; max-height: 140px; line-height: 1.5; transition: border-color 0.2s; }
  .text-box:focus { border-color: var(--fire); }
  .action-btn { width: 50px; height: 50px; border-radius: var(--radius); background: linear-gradient(135deg, var(--fire), var(--fire-glow)); border: none; cursor: pointer; display: flex; align-items: center; justify-content: center; color: #fff; transition: transform 0.2s; flex-shrink: 0; }
  .action-btn:hover { transform: scale(1.04); } :disabled { opacity: 0.5; cursor: not-allowed; }
  .action-btn svg { width: 20px; height: 20px; }

  /* GENRE MODAL */
  .genre-modal-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.85); backdrop-filter: blur(8px); z-index: 200; display: none; align-items: center; justify-content: center; padding: 20px; }
  .genre-modal-overlay.open { display: flex; }
  .genre-modal { background: var(--surface); border: 1px solid var(--border); border-radius: 20px; max-width: 520px; width: 100%; max-height: 82vh; overflow-y: auto; position: relative; animation: slideUp 0.35s cubic-bezier(0.16,1,0.3,1); }
  .genre-modal-header { padding: 20px 20px 14px; border-bottom: 1px solid var(--border); position: sticky; top: 0; background: var(--surface); z-index: 2; display: flex; align-items: center; justify-content: space-between; }
  .genre-modal-title { font-size: 1rem; font-weight: 700; }
  .genre-modal-close { background: var(--surface2); border: 1px solid var(--border); color: var(--muted); width: 34px; height: 34px; border-radius: 50%; cursor: pointer; display: flex; align-items: center; justify-content: center; font-size: 1.1rem; }
  .genre-modal-list { padding: 14px; display: flex; flex-direction: column; gap: 8px; }
  .modal-track { display: flex; align-items: center; gap: 12px; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06); padding: 10px 13px; border-radius: 10px; text-decoration: none; color: #fff; transition: all 0.2s; }
  .modal-track:hover { background: rgba(255,87,34,0.1); border-color: var(--fire); transform: translateX(3px); }
  .modal-track-num { width: 24px; height: 24px; background: var(--surface2); border: 1px solid var(--border); border-radius: 50%; font-size: 0.7rem; font-weight: 700; color: var(--fire-glow); display: flex; align-items: center; justify-content: center; }
  .modal-track-thumb { width: 64px; height: 42px; border-radius: 7px; object-fit: cover; background: var(--surface2); }
  .modal-track-info { flex: 1; min-width: 0; }
  .modal-track-title { font-size: 0.88rem; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .modal-track-artist { font-size: 0.75rem; color: var(--muted); margin-top: 2px; }
  .modal-yt-btn { background: rgba(255,0,0,0.12); border: 1px solid rgba(255,0,0,0.3); color: #ff4444; padding: 5px 10px; border-radius: 20px; font-size: 0.7rem; font-weight: 700; }

  /* INFO WELCOME CARD */
  .info-welcome { max-width: 720px; margin: 0 auto; padding: 36px 20px 0; width: 100%; }
  .info-welcome-card { background: var(--surface); border: 1px solid var(--border); border-radius: 16px; padding: 26px 22px; margin-bottom: 16px; }
  .info-welcome-title { font-size: 1.25rem; font-weight: 700; margin-bottom: 6px; }
  .info-welcome-sub { color: var(--muted); font-size: 0.88rem; line-height: 1.55; }
  .info-chips { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 14px; }
  .info-chip { background: rgba(255,87,34,0.08); border: 1px solid rgba(255,87,34,0.2); color: var(--fire-glow); padding: 7px 13px; border-radius: 20px; font-size: 0.8rem; cursor: pointer; transition: all
