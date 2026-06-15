import streamlit as st
import anthropic
import json
import re

# ── PAGE CONFIG ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="MoodTune AI",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── ANTHROPIC CLIENT ───────────────────────────────────────────────────────────
client = anthropic.Anthropic()

# ── SYSTEM PROMPTS ─────────────────────────────────────────────────────────────
MOOD_SYSTEM = """SEN AI MUSIC RECOMMENDATION ASSISTANT'SAN.
Foydalanuvchining hissiy holati va musiqa maqsadini 3 savol bilan aniqlaysan va keyin 15 ta HIT qo'shiq tavsiya qilasan.

SAVOLLAR TARTIBI:
1. "Hozir ichingizdagi eng yaqin hissiyot qaysi?"
2. "Shu holatda musiqa sizga nima uchun kerak?"
3. "Energiya beradigan musiqami yoki tinchlantiradiganmi?"

3-savolga javob olgandan yoki "Musiqa tavsiya qil" buyrug'i kelganda, FAQAT quyidagi formatda javob ber (boshqa hech narsa qo'shma):

[REPORT_START]
### Kayfiyat Tahlili
**Mood:** ...
**Musiqa uslubi:** ...
**Janrlar:** ...

[TRACKS_START]
[
  {"title":"Artist - Track","search":"Artist Track official audio","ytId":"REAL_YT_ID"},
  {"title":"Artist - Track","search":"Artist Track official audio","ytId":"REAL_YT_ID"},
  {"title":"Artist - Track","search":"Artist Track official audio","ytId":"REAL_YT_ID"},
  {"title":"Artist - Track","search":"Artist Track official audio","ytId":"REAL_YT_ID"},
  {"title":"Artist - Track","search":"Artist Track official audio","ytId":"REAL_YT_ID"},
  {"title":"Artist - Track","search":"Artist Track official audio","ytId":"REAL_YT_ID"},
  {"title":"Artist - Track","search":"Artist Track official audio","ytId":"REAL_YT_ID"},
  {"title":"Artist - Track","search":"Artist Track official audio","ytId":"REAL_YT_ID"},
  {"title":"Artist - Track","search":"Artist Track official audio","ytId":"REAL_YT_ID"},
  {"title":"Artist - Track","search":"Artist Track official audio","ytId":"REAL_YT_ID"},
  {"title":"Artist - Track","search":"Artist Track official audio","ytId":"REAL_YT_ID"},
  {"title":"Artist - Track","search":"Artist Track official audio","ytId":"REAL_YT_ID"},
  {"title":"Artist - Track","search":"Artist Track official audio","ytId":"REAL_YT_ID"},
  {"title":"Artist - Track","search":"Artist Track official audio","ytId":"REAL_YT_ID"},
  {"title":"Artist - Track","search":"Artist Track official audio","ytId":"REAL_YT_ID"}
]
[TRACKS_END]
[REPORT_END]

JUDA MUHIM QOIDALAR:
1. Har doim AYNAN 15 ta track ber, kamroq bo'lmasin!
2. ytId — bu YouTube video URL dagi 11 belgili kod. Masalan: https://youtube.com/watch?v=dQw4w9WgXcQ => ytId = "dQw4w9WgXcQ"
3. Faqat 100% ishonchli ytId yoz. Bilmasang "SEARCH" yoz — ilovamiz avtomatik qidiradi.
4. Faqat dunyo miqyosida mashhur hitlar (millionlar tinglagan).
5. JSON formatini buzma — [] ichida 15 ta {} bo'lsin.

Mashhur ytId misollar: Blinding Lights=4NRXx6U8ABQ, Shape of You=JGwWNGJdvx8, Bohemian Rhapsody=fJ9rUzIMcZQ, God's Plan=xpVfcZ0ZcFM, Uptown Funk=OPf0YbXqDm0, Rolling in the Deep=rYEDA3JcQqw"""

INFO_SYSTEM = """Sen musiqa bo'yicha ekspert AI assistantsan. Sening ichingda juda ko'p musiqa biliming bor.

Foydalanuvchi artist, albom yoki qo'shiq haqida so'raganda, O'Z BILIMINGDAN foydalanib FAQAT quyidagi JSON formatida javob ber (boshqa hech narsa qo'shma, markdown ham emas):

{
  "type": "artist" | "album" | "track" | "general",
  "name": "...",
  "emoji": "bitta emoji",
  "tagline": "qisqa ta'rif (1 gap)",
  "stats": [
    {"num": "...", "label": "..."}
  ],
  "facts": [
    {"key": "...", "val": "..."}
  ],
  "sections": [
    {
      "title": "Bo'lim nomi",
      "icon": "emoji",
      "type": "prose" | "tags" | "albums" | "tracks",
      "content": "matn (prose uchun)" | ["massiv (tags uchun)"] | [{"name":"...","year":"..."}] | [{"title":"..."}]
    }
  ],
  "summary": "yakuniy xulosa 1-2 gap"
}

Foydalanuvchi qaysi tilda yozsa, shu tilda javob ber. Barcha maydonlar shu tilda bo'lsin.
FAQAT JSON, boshqa hech narsa."""

MOOD_TEST_SYSTEM = """Sen kayfiyat asosida musiqa tavsiya qiluvchi AI assistantsan.

Foydalanuvchi 4 savolga javob berdi. Ularning javoblarini tahlil qilib, FAQAT quyidagi JSON formatida javob ber:

{
  "vibe": "Asabga qarshi dori" | "Raqs va Kayfiyat" | "Miyaga Perekur" | "Lirika / Sokinlik",
  "description": "1-2 gap tavsif",
  "genres": ["janr1", "janr2", "janr3"],
  "tracks": [
    {"title": "Artist - Track", "ytId": "YouTube_ID_OR_SEARCH", "search": "qidiruv so'zi"}
  ]
}

tracks massivida 10 ta qo'shiq bo'lsin. ytId bilmasang "SEARCH" yoz.
FAQAT JSON, boshqa hech narsa."""

# ── SESSION STATE ──────────────────────────────────────────────────────────────
if "mood_history" not in st.session_state:
    st.session_state.mood_history = []
if "mood_msg_count" not in st.session_state:
    st.session_state.mood_msg_count = 0
if "info_history" not in st.session_state:
    st.session_state.info_history = []
if "current_page" not in st.session_state:
    st.session_state.current_page = "mood"
if "current_lang" not in st.session_state:
    st.session_state.current_lang = "uz"
if "test_active" not in st.session_state:
    st.session_state.test_active = False
if "test_answers" not in st.session_state:
    st.session_state.test_answers = {}
if "test_done" not in st.session_state:
    st.session_state.test_done = False
if "test_result" not in st.session_state:
    st.session_state.test_result = None

# ── CLAUDE API CALL ────────────────────────────────────────────────────────────
def claude_call(history, system, max_tokens=2000):
    msgs = [{"role": m["role"], "content": m["content"]} for m in history]
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=max_tokens,
        system=system,
        messages=msgs
    )
    return response.content[0].text

def mood_test_call(answers):
    prompt = f"""Foydalanuvchi quyidagi savollarga javob berdi:

1. Hozir ichingizdagi qaysi emotsiya birinchi o'rinda turibdi?
   Javob: {answers.get('q1', '')}

2. Sizga hozir qanday ritm (sur'at) kerak?
   Javob: {answers.get('q2', '')}

3. Qo'shiqda so'zlar (matn) bo'lishi shartmi?
   Javob: {answers.get('q3', '')}

4. Musiqa sizni hozir qayerga yetaklashi kerak?
   Javob: {answers.get('q4', '')}

Shu javoblar asosida musiqa tavsiya qil."""
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1500,
        system=MOOD_TEST_SYSTEM,
        messages=[{"role": "user", "content": prompt}]
    )
    raw = response.content[0].text
    raw = re.sub(r'```json|```', '', raw).strip()
    return json.loads(raw)

# ── PARSE MOOD REPLY ───────────────────────────────────────────────────────────
def parse_mood_reply(raw):
    if "[REPORT_START]" not in raw:
        return {"type": "text", "content": raw}
    try:
        seg = raw.split("[REPORT_START]")[1].split("[REPORT_END]")[0]
        analysis = seg
        tracks = None
        if "[TRACKS_START]" in seg:
            parts = seg.split("[TRACKS_START]")
            analysis = parts[0]
            json_str = parts[1].split("[TRACKS_END]")[0].strip()
            json_str = re.sub(r'```json|```', '', json_str).strip()
            tracks = json.loads(json_str)
        def extract_field(text, label):
            m = re.search(r'\*\*' + label + r':\*\*\s*(.+)', text, re.IGNORECASE)
            return m.group(1).strip() if m else None
        mood = extract_field(analysis, "Mood")
        style = extract_field(analysis, "Musiqa uslubi")
        genres = extract_field(analysis, "Janrlar")
        return {"type": "report", "mood": mood, "style": style, "genres": genres, "tracks": tracks}
    except Exception as e:
        return {"type": "text", "content": raw}

# ── TEST QUESTIONS ─────────────────────────────────────────────────────────────
TEST_QUESTIONS = [
    {
        "id": "q1",
        "text": "🎭 Hozir ichingizdagi qaysi emotsiya birinchi o'rinda turibdi?",
        "options": [
            {"key": "A", "label": "😤 Jahl, asabiylik yoki stress", "sub": "Hamma narsa asabga tegyapti"},
            {"key": "B", "label": "⚡ Energiya to'lib-toshayapti", "sub": "Harakat qilgim kelyapti"},
            {"key": "C", "label": "😴 Charchoq va bo'shashish", "sub": "Miyaga sokinlik kerak"},
            {"key": "D", "label": "🌙 Bir oz zerikish yoki mayuslik", "sub": "Xayol surish kayfiyati"},
        ]
    },
    {
        "id": "q2",
        "text": "🎵 Sizga hozir qanday ritm (sur'at) kerak?",
        "options": [
            {"key": "A", "label": "💥 Juda tez va shovqinli", "sub": ""},
            {"key": "B", "label": "🕺 Ritmli, sho'x", "sub": "Lekin asabga tegmaydigan"},
            {"key": "C", "label": "〰️ Bir tekisda ketadigan", "sub": "Sokin fon"},
            {"key": "D", "label": "🌊 Sekin va mayin", "sub": ""},
        ]
    },
    {
        "id": "q3",
        "text": "🎤 Qo'shiqda so'zlar (matn) bo'lishi shartmi?",
        "options": [
            {"key": "A", "label": "🔥 Farqi yo'q", "sub": "Asosiysi drayv bo'lsa bo'ldi"},
            {"key": "B", "label": "🎉 Ha, sho'x so'zlar bo'lsin", "sub": "Qo'shilib aytishga oson"},
            {"key": "C", "label": "🎹 Yo'q", "sub": "So'zlar umuman bo'lmasin yoki chet tilida"},
            {"key": "D", "label": "📖 Ha, ma'noli chuqur so'zlar", "sub": ""},
        ]
    },
    {
        "id": "q4",
        "text": "🚀 Musiqa sizni hozir qayerga yetaklashi kerak?",
        "options": [
            {"key": "A", "label": "💢 Negativni tashqariga chiqarishga", "sub": "Baqirib-chaqirib"},
            {"key": "B", "label": "💃 To'g'ri raqs maydonchasiga", "sub": "Divandan turib ketishga"},
            {"key": "C", "label": "🛋️ Divanga yotib dam olishga", "sub": "Ko'zni yumib"},
            {"key": "D", "label": "💭 Shirin xayollarga", "sub": "O'tmish yoki kelajak haqida"},
        ]
    }
]

VIBE_INFO = {
    "Asabga qarshi dori": {"emoji": "🔥", "color": "#ff5722"},
    "Raqs va Kayfiyat": {"emoji": "💃", "color": "#ff9100"},
    "Miyaga Perekur": {"emoji": "🧠", "color": "#4caf50"},
    "Lirika / Sokinlik": {"emoji": "🌙", "color": "#7c4dff"},
}

# ── CSS ────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&display=swap');

:root {
  --bg: #060606; --surface: #111111; --surface2: #1a1a1a;
  --border: #222222; --fire: #ff5722; --fire-glow: #ff9100;
  --text: #f5f5f5; --muted: #777777; --radius: 16px;
  --font-head: 'Space Grotesk', sans-serif;
  --font-mono: 'Space Mono', monospace;
}

html, body, [class*="css"], .stApp {
  background: var(--bg) !important;
  color: var(--text) !important;
  font-family: var(--font-head) !important;
}

.stApp { background: var(--bg) !important; }

/* Hide Streamlit branding */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { display: none; }
div[data-testid="stToolbar"] { display: none; }

/* TOP HEADER */
.mt-header {
  display: flex; align-items: center; justify-content: space-between;
  padding: 14px 28px; border-bottom: 1px solid var(--border);
  background: rgba(6,6,6,0.97); backdrop-filter: blur(16px);
  position: sticky; top: 0; z-index: 100; flex-wrap: wrap; gap: 10px;
}
.mt-logo { display: flex; align-items: center; gap: 12px; }
.mt-logo-fire { font-size: 1.6rem; animation: pulse 2s infinite; }
@keyframes pulse { 0%,100%{transform:scale(1)} 50%{transform:scale(1.1)} }
.mt-logo-text { font-weight: 700; font-size: 1.2rem; letter-spacing:-0.03em; }
.mt-logo-text span { 
  background: linear-gradient(to right, var(--fire-glow), #fff);
  -webkit-background-clip: text; background-clip: text; color: transparent;
}

/* PAGE CONTENT */
.mt-page { max-width: 760px; margin: 0 auto; padding: 24px 20px 120px; }

/* CHAT MESSAGES */
.mt-msg { display: flex; gap: 12px; margin-bottom: 18px; animation: slideUp 0.4s ease; }
@keyframes slideUp { from{opacity:0;transform:translateY(14px)} to{opacity:1;transform:translateY(0)} }
.mt-msg.user { flex-direction: row-reverse; }
.mt-avatar {
  width: 36px; height: 36px; border-radius: 50%; display: flex;
  align-items: center; justify-content: center; font-size: 1rem;
  flex-shrink: 0; border: 1px solid var(--border);
}
.mt-msg.bot .mt-avatar { 
  background: linear-gradient(135deg,#222,#111); 
  box-shadow: 0 0 10px rgba(255,87,34,0.15);
  border-color: rgba(255,87,34,0.3);
}
.mt-msg.user .mt-avatar { background: #ffffff10; }
.mt-bubble {
  padding: 12px 18px; border-radius: 14px; font-size: 0.95rem;
  line-height: 1.6; white-space: pre-wrap; word-break: break-word;
  max-width: 78%;
}
.mt-msg.bot .mt-bubble { 
  background: var(--surface); border: 1px solid var(--border);
  border-top-left-radius: 4px; color: #e0e0e0;
}
.mt-msg.user .mt-bubble {
  background: linear-gradient(135deg, var(--fire), #d84315);
  color: #fff; border-top-right-radius: 4px;
  box-shadow: 0 4px 12px rgba(255,87,34,0.2);
}

/* ANALYSIS REPORT */
.mt-report {
  margin-top: 10px; background: rgba(255,255,255,0.01);
  border: 1px solid rgba(255,87,34,0.2); border-radius: 16px; overflow: hidden;
}
.mt-report-header {
  background: linear-gradient(135deg, rgba(255,87,34,0.12), rgba(255,145,0,0.06));
  padding: 12px 16px; border-bottom: 1px solid rgba(255,87,34,0.15);
  display: flex; align-items: center; gap: 10px;
}
.mt-report-title { font-weight: 700; font-size: 0.95rem; color: var(--fire-glow); }
.mt-mood-meta {
  padding: 10px 14px; display: flex; flex-wrap: wrap; gap: 7px;
}
.mt-mood-tag {
  display: inline-flex; align-items: baseline; gap: 5px;
  background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08);
  border-radius: 20px; padding: 4px 10px;
}
.mt-tag-lbl { color: var(--muted); font-size: 0.66rem; text-transform: uppercase; letter-spacing: 0.07em; }
.mt-tag-val { color: var(--text); font-weight: 600; font-size: 0.78rem; }
.mt-tracks-header {
  padding: 6px 14px 8px; font-size: 0.66rem; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.1em; color: var(--muted);
}
.mt-track-list { padding: 0 10px 12px; display: flex; flex-direction: column; gap: 5px; }

/* TRACK CARD */
.mt-track {
  display: flex; align-items: center; gap: 0;
  background: rgba(255,255,255,0.025); border: 1px solid rgba(255,255,255,0.05);
  border-radius: 10px; text-decoration: none; color: #fff;
  transition: all 0.22s; overflow: hidden; cursor: pointer;
}
.mt-track:hover { 
  background: rgba(255,87,34,0.07); border-color: rgba(255,87,34,0.35);
  transform: translateX(3px);
}
.mt-track-thumb { 
  width: 84px; height: 54px; object-fit: cover; display: block; flex-shrink: 0;
}
.mt-track-ph { 
  width: 84px; height: 54px; background: linear-gradient(135deg,#1a1a1a,#0d0d0d);
  display: flex; align-items: center; justify-content: center; font-size: 1.3rem; flex-shrink: 0;
}
.mt-track-info { flex: 1; min-width: 0; padding: 0 12px; }
.mt-track-title { font-weight: 600; font-size: 0.84rem; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.mt-track-artist { font-size: 0.7rem; color: var(--muted); margin-top: 2px; }
.mt-track-yt { 
  flex-shrink: 0; background: rgba(255,0,0,0.1);
  border-left: 1px solid rgba(255,255,255,0.05); color: #ff5555;
  padding: 0 12px; height: 54px; display: flex; align-items: center;
  font-family: var(--font-mono); font-size: 0.62rem; font-weight: 700; white-space: nowrap;
}

/* TRENDING SECTION */
.mt-trending-title {
  font-size: 0.72rem; font-weight: 600; text-transform: uppercase;
  letter-spacing: 0.1em; color: var(--muted); margin-bottom: 14px;
  display: flex; align-items: center; gap: 10px;
}
.mt-trending-title::after { content: ''; flex: 1; height: 1px; background: var(--border); }
.mt-genre-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin-bottom: 24px; }
.mt-genre-card {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 12px; overflow: hidden; cursor: pointer; transition: all 0.25s;
  text-decoration: none;
}
.mt-genre-card:hover { border-color: var(--fire); transform: translateY(-2px); box-shadow: 0 8px 24px rgba(255,87,34,0.12); }
.mt-genre-ph { 
  width: 100%; aspect-ratio: 16/9; display: flex; align-items: center;
  justify-content: center; font-size: 2.2rem;
  background: linear-gradient(135deg, var(--surface2), #0d0d0d);
}
.mt-genre-info { padding: 10px 12px; }
.mt-genre-label { font-size: 0.66rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--fire-glow); margin-bottom: 3px; }
.mt-genre-track { font-size: 0.83rem; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.mt-genre-artist { font-size: 0.73rem; color: var(--muted); margin-top: 1px; }

/* MOOD TEST */
.mt-test-card {
  background: var(--surface); border: 1px solid rgba(255,87,34,0.3);
  border-radius: 18px; padding: 22px; margin-bottom: 24px;
}
.mt-test-header { 
  background: linear-gradient(135deg, rgba(255,87,34,0.15), rgba(255,145,0,0.08));
  border-radius: 12px; padding: 14px 18px; margin-bottom: 20px;
  border: 1px solid rgba(255,87,34,0.2);
}
.mt-test-title { font-size: 1.05rem; font-weight: 700; margin-bottom: 4px; }
.mt-test-sub { font-size: 0.83rem; color: var(--muted); }
.mt-q-text { font-size: 0.95rem; font-weight: 600; margin-bottom: 12px; }
.mt-q-progress { 
  font-size: 0.7rem; color: var(--muted); margin-bottom: 16px;
  display: flex; align-items: center; gap: 6px;
}
.mt-progress-dots { display: flex; gap: 5px; }
.mt-dot { width: 7px; height: 7px; border-radius: 50%; background: var(--border); }
.mt-dot.done { background: var(--fire); }
.mt-dot.current { background: var(--fire-glow); box-shadow: 0 0 6px var(--fire-glow); }
.mt-opt-btn {
  width: 100%; text-align: left; background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.07); border-radius: 10px;
  padding: 11px 14px; margin-bottom: 8px; cursor: pointer; transition: all 0.2s;
  color: var(--text); font-family: var(--font-head); font-size: 0.88rem;
}
.mt-opt-btn:hover { background: rgba(255,87,34,0.08); border-color: rgba(255,87,34,0.3); }
.mt-opt-key { 
  display: inline-flex; align-items: center; justify-content: center;
  width: 22px; height: 22px; border-radius: 6px; background: rgba(255,87,34,0.15);
  color: var(--fire-glow); font-weight: 700; font-size: 0.7rem;
  margin-right: 9px; font-family: var(--font-mono); flex-shrink: 0;
}
.mt-opt-sub { font-size: 0.73rem; color: var(--muted); margin-left: 31px; margin-top: 2px; }

/* RESULT CARD */
.mt-result-card {
  background: var(--surface); border-radius: 18px; overflow: hidden;
  border: 1px solid rgba(255,87,34,0.25); margin-bottom: 24px;
}
.mt-result-header {
  background: linear-gradient(135deg, rgba(255,87,34,0.2), rgba(255,145,0,0.1));
  padding: 20px; border-bottom: 1px solid rgba(255,87,34,0.15);
  text-align: center;
}
.mt-result-vibe { font-size: 2rem; margin-bottom: 6px; }
.mt-result-title { font-size: 1.2rem; font-weight: 700; color: var(--fire-glow); }
.mt-result-desc { font-size: 0.85rem; color: #bbb; margin-top: 6px; line-height: 1.5; }
.mt-result-genres { 
  display: flex; flex-wrap: wrap; gap: 7px; 
  padding: 14px; border-bottom: 1px solid var(--border);
}
.mt-result-genre-tag {
  background: rgba(255,87,34,0.1); border: 1px solid rgba(255,87,34,0.25);
  color: var(--fire-glow); padding: 4px 12px; border-radius: 20px; font-size: 0.78rem;
}

/* NAV TABS */
.mt-nav { display: flex; gap: 4px; background: var(--surface); padding: 4px; border-radius: 10px; border: 1px solid var(--border); }
.mt-nav-tab { 
  background: none; border: none; color: var(--muted);
  font-family: var(--font-head); font-size: 0.8rem; font-weight: 600;
  padding: 7px 14px; cursor: pointer; border-radius: 6px;
  transition: all 0.2s;
}
.mt-nav-tab.active { 
  background: var(--surface2); color: var(--fire-glow);
  border: 1px solid rgba(255,87,34,0.2);
}

/* INFO CHAT */
.mt-info-rich { padding: 4px 0; }
.mt-info-stat-row { display: flex; gap: 10px; flex-wrap: wrap; margin: 10px 0; }
.mt-info-stat { 
  background: var(--surface2); border: 1px solid var(--border);
  border-radius: 8px; padding: 8px 14px; text-align: center;
}
.mt-info-stat-num { font-size: 1.05rem; font-weight: 700; color: var(--fire-glow); }
.mt-info-stat-lbl { font-size: 0.68rem; color: var(--muted); margin-top: 1px; }
.mt-info-section { margin-bottom: 14px; }
.mt-info-sec-title { 
  font-size: 0.7rem; font-weight: 700; text-transform: uppercase;
  letter-spacing: 0.1em; color: var(--fire-glow); margin-bottom: 8px;
  padding-bottom: 6px; border-bottom: 1px solid rgba(255,87,34,0.15);
}
.mt-info-fact-row { display: flex; gap: 6px; margin-bottom: 5px; }
.mt-info-fact-key { font-size: 0.76rem; color: var(--muted); min-width: 85px; }
.mt-info-fact-val { font-size: 0.83rem; color: var(--text); font-weight: 500; }
.mt-info-album-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(120px,1fr)); gap: 8px; }
.mt-info-album-card { background: var(--surface2); border: 1px solid var(--border); border-radius: 8px; padding: 9px; }
.mt-info-album-name { font-weight: 600; font-size: 0.8rem; }
.mt-info-album-year { font-size: 0.7rem; color: var(--muted); margin-top: 3px; }
.mt-info-tag-list { display: flex; flex-wrap: wrap; gap: 6px; }
.mt-info-tag { 
  background: rgba(255,87,34,0.08); border: 1px solid rgba(255,87,34,0.2);
  color: var(--fire-glow); padding: 4px 10px; border-radius: 20px; font-size: 0.74rem;
}
.mt-info-prose { font-size: 0.88rem; color: #d0d0d0; line-height: 1.65; }

/* CHIP BUTTONS */
.mt-chip-row { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 16px; }
.mt-chip { 
  background: rgba(255,87,34,0.08); border: 1px solid rgba(255,87,34,0.2);
  color: var(--fire-glow); padding: 7px 13px; border-radius: 20px;
  font-size: 0.78rem; cursor: pointer; transition: all 0.2s;
}
.mt-chip:hover { background: rgba(255,87,34,0.16); border-color: var(--fire); }

/* Streamlit button overrides */
.stButton button {
  background: none !important;
  border: none !important;
  padding: 0 !important;
  font-size: inherit !important;
}
.stTextArea textarea {
  background: #111111 !important;
  color: #f5f5f5 !important;
  border: 1px solid #222222 !important;
  border-radius: 14px !important;
  font-family: 'Space Grotesk', sans-serif !important;
  font-size: 0.95rem !important;
}
.stTextArea textarea:focus {
  border-color: #ff5722 !important;
  box-shadow: none !important;
}

/* Scrollbar */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: #333; border-radius: 5px; }
</style>
""", unsafe_allow_html=True)

# ── RENDER TRACKS ──────────────────────────────────────────────────────────────
def render_tracks_html(tracks, num_offset=0):
    html = ""
    for i, t in enumerate(tracks):
        yt_id = t.get("ytId", "SEARCH")
        title = t.get("title", "")
        parts = title.split(" - ", 1)
        artist_name = parts[0].strip() if len(parts) > 1 else ""
        song_name = parts[1].strip() if len(parts) > 1 else title
        search_q = t.get("search", title)
        if yt_id and yt_id != "SEARCH" and len(yt_id) == 11:
            yt_url = f"https://www.youtube.com/watch?v={yt_id}"
            thumb = f'<img src="https://img.youtube.com/vi/{yt_id}/mqdefault.jpg" class="mt-track-thumb" loading="lazy" onerror="this.parentElement.innerHTML=\'<div class=mt-track-ph>🎵</div>\'">'
        else:
            yt_url = f"https://www.youtube.com/results?search_query={search_q.replace(' ', '+')}"
            thumb = '<div class="mt-track-ph">🎵</div>'
        artist_html = f'<div class="mt-track-artist">{artist_name}</div>' if artist_name else ""
        html += f'''<a href="{yt_url}" target="_blank" rel="noopener" class="mt-track">
            {thumb}
            <div class="mt-track-info">
                <div class="mt-track-title">{song_name}</div>
                {artist_html}
            </div>
            <div class="mt-track-yt">▶ YouTube</div>
        </a>'''
    return html

# ── RENDER INFO CARD ───────────────────────────────────────────────────────────
def render_info_card(data):
    html = '<div class="mt-info-rich">'
    emoji = data.get("emoji", "🎵")
    name = data.get("name", "")
    tagline = data.get("tagline", "")
    html += f'''<div style="display:flex;align-items:center;gap:14px;margin-bottom:16px">
        <span style="font-size:2.5rem;width:56px;height:56px;display:flex;align-items:center;justify-content:center;background:var(--surface2);border-radius:12px;border:2px solid var(--border);flex-shrink:0">{emoji}</span>
        <div>
            <div style="font-size:1.05rem;font-weight:700">{name}</div>
            <div style="font-size:0.8rem;color:var(--muted);margin-top:3px">{tagline}</div>
        </div>
    </div>'''
    stats = data.get("stats", [])
    if stats:
        html += '<div class="mt-info-stat-row">'
        for s in stats:
            html += f'<div class="mt-info-stat"><div class="mt-info-stat-num">{s["num"]}</div><div class="mt-info-stat-lbl">{s["label"]}</div></div>'
        html += '</div>'
    facts = data.get("facts", [])
    if facts:
        html += '<div class="mt-info-section"><div class="mt-info-sec-title">📋 Asosiy ma\'lumotlar</div>'
        for f in facts:
            html += f'<div class="mt-info-fact-row"><span class="mt-info-fact-key">{f["key"]}</span><span class="mt-info-fact-val">{f["val"]}</span></div>'
        html += '</div>'
    for sec in data.get("sections", []):
        icon = sec.get("icon", "📌")
        title = sec.get("title", "")
        stype = sec.get("type", "prose")
        content = sec.get("content", "")
        html += f'<div class="mt-info-section"><div class="mt-info-sec-title">{icon} {title}</div>'
        if stype == "prose":
            html += f'<div class="mt-info-prose">{str(content).replace(chr(10), "<br>")}</div>'
        elif stype == "tags" and isinstance(content, list):
            html += '<div class="mt-info-tag-list">'
            for tag in content:
                html += f'<span class="mt-info-tag">{tag}</span>'
            html += '</div>'
        elif stype == "albums" and isinstance(content, list):
            html += '<div class="mt-info-album-grid">'
            for al in content:
                n = al.get("name", al.get("title", ""))
                y = al.get("year", "")
                html += f'<div class="mt-info-album-card"><div class="mt-info-album-name">{n}</div><div class="mt-info-album-year">{y}</div></div>'
            html += '</div>'
        elif stype == "tracks" and isinstance(content, list):
            for tr in content:
                if isinstance(tr, dict):
                    yt_id = tr.get("ytId", "")
                    t_title = tr.get("title", "")
                else:
                    yt_id = ""
                    t_title = str(tr)
                if yt_id and len(yt_id) == 11:
                    yt_url = f"https://www.youtube.com/watch?v={yt_id}"
                    thumb = f'<img src="https://img.youtube.com/vi/{yt_id}/mqdefault.jpg" style="width:64px;height:42px;border-radius:7px;object-fit:cover;flex-shrink:0" loading="lazy">'
                else:
                    yt_url = f"https://www.youtube.com/results?search_query={t_title.replace(' ', '+')}"
                    thumb = '<div style="width:64px;height:42px;background:var(--surface2);border-radius:7px;display:flex;align-items:center;justify-content:center;font-size:1.1rem;flex-shrink:0">🎵</div>'
                html += f'''<a href="{yt_url}" target="_blank" rel="noopener" class="mt-track" style="margin-bottom:5px">
                    {thumb}
                    <div class="mt-track-info"><div class="mt-track-title">{t_title}</div></div>
                    <div class="mt-track-yt">▶ YouTube</div>
                </a>'''
        html += '</div>'
    summary = data.get("summary", "")
    if summary:
        html += f'<div style="margin-top:10px;padding:10px 14px;background:rgba(255,87,34,0.05);border-left:3px solid var(--fire);border-radius:0 8px 8px 0;font-size:0.86rem;color:#bbb;line-height:1.6">{summary}</div>'
    html += '</div>'
    return html

# ── HEADER ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="mt-header">
    <div class="mt-logo">
        <div class="mt-logo-fire">🔥</div>
        <div class="mt-logo-text">MoodTune<span>AI</span></div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── NAVIGATION ─────────────────────────────────────────────────────────────────
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 2])
with col1:
    if st.button("🎵 Mood Chat", key="nav_mood"):
        st.session_state.current_page = "mood"
        st.rerun()
with col2:
    if st.button("🎭 Mood Test", key="nav_test"):
        st.session_state.current_page = "test"
        st.session_state.test_active = True
        st.session_state.test_answers = {}
        st.session_state.test_done = False
        st.session_state.test_result = None
        st.rerun()
with col3:
    if st.button("🎤 Music Info", key="nav_info"):
        st.session_state.current_page = "info"
        st.rerun()

# Active page indicator
active_css = ""
if st.session_state.current_page == "mood":
    active_css = "nav_mood"
elif st.session_state.current_page == "test":
    active_css = "nav_test"
elif st.session_state.current_page == "info":
    active_css = "nav_info"

st.markdown("<hr style='border:none;border-top:1px solid #222;margin:0 0 8px'>", unsafe_allow_html=True)

# ── PAGE: MOOD CHAT ────────────────────────────────────────────────────────────
if st.session_state.current_page == "mood":
    with st.container():
        st.markdown('<div class="mt-page">', unsafe_allow_html=True)

        # TRENDING GENRES
        GENRES = [
            {"label": "Pop / R&B", "icon": "🎶", "track": "Blinding Lights", "artist": "The Weeknd", "ytId": "4NRXx6U8ABQ"},
            {"label": "Rap / Hip-Hop", "icon": "🎤", "track": "God's Plan", "artist": "Drake", "ytId": "xpVfcZ0ZcFM"},
            {"label": "Classic", "icon": "🎻", "track": "Bohemian Rhapsody", "artist": "Queen", "ytId": "fJ9rUzIMcZQ"},
            {"label": "Nostalgic", "icon": "🌅", "track": "Hotel California", "artist": "Eagles", "ytId": "BciS5krYL80"},
        ]
        genre_html = '<div class="mt-trending-title">🔥 Trending hozir — bosing va tinglang</div><div class="mt-genre-grid">'
        for g in GENRES:
            yt_url = f"https://www.youtube.com/watch?v={g['ytId']}"
            genre_html += f'''<a href="{yt_url}" target="_blank" rel="noopener" class="mt-genre-card">
                <div class="mt-genre-ph">{g["icon"]}</div>
                <div class="mt-genre-info">
                    <div class="mt-genre-label">{g["label"]}</div>
                    <div class="mt-genre-track">{g["track"]}</div>
                    <div class="mt-genre-artist">{g["artist"]}</div>
                </div>
            </a>'''
        genre_html += '</div>'
        st.markdown(genre_html, unsafe_allow_html=True)

        # CHAT MESSAGES
        if not st.session_state.mood_history:
            greeting = "Hozir ichingizdagi eng yaqin hissiyot qaysi?"
            st.session_state.mood_history.append({"role": "assistant", "content": greeting})

        chat_html = ""
        for msg in st.session_state.mood_history:
            role = msg["role"]
            content = msg["content"]
            css_cls = "bot" if role == "assistant" else "user"
            avatar = "🔥" if role == "assistant" else "👤"
            if msg.get("html"):
                bubble = f'<div class="mt-bubble">{content}</div>'
            else:
                safe_content = content.replace("<", "&lt;").replace(">", "&gt;")
                bubble = f'<div class="mt-bubble">{safe_content}</div>'
            chat_html += f'<div class="mt-msg {css_cls}"><div class="mt-avatar">{avatar}</div>{bubble}</div>'
        if chat_html:
            st.markdown(chat_html, unsafe_allow_html=True)

        # QUICK ACTIONS
        col_rec, col_reset = st.columns([3, 1])
        with col_rec:
            can_rec = st.session_state.mood_msg_count >= 2
            if can_rec:
                if st.button("✨ Musiqa tavsiya qil", key="rec_btn"):
                    st.session_state.mood_history.append({"role": "user", "content": "Musiqa tavsiya qil"})
                    try:
                        reply = claude_call(
                            st.session_state.mood_history,
                            MOOD_SYSTEM,
                            max_tokens=2500
                        )
                        st.session_state.mood_history.append({"role": "assistant", "content": reply})
                        parsed = parse_mood_reply(reply)
                        if parsed["type"] == "report":
                            report_html = f'''<div class="mt-report">
                                <div class="mt-report-header">▶ <span class="mt-report-title">Mood Analysis & Music Picks</span></div>
                                <div class="mt-mood-meta">'''
                            if parsed.get("mood"):
                                report_html += f'<span class="mt-mood-tag"><span class="mt-tag-lbl">😌 Kayfiyat</span><span class="mt-tag-val">{parsed["mood"]}</span></span>'
                            if parsed.get("style"):
                                report_html += f'<span class="mt-mood-tag"><span class="mt-tag-lbl">🎨 Uslub</span><span class="mt-tag-val">{parsed["style"]}</span></span>'
                            if parsed.get("genres"):
                                report_html += f'<span class="mt-mood-tag"><span class="mt-tag-lbl">🎵 Janr</span><span class="mt-tag-val">{parsed["genres"]}</span></span>'
                            report_html += '</div><div class="mt-tracks-header">🎧 Tavsiya etiladigan qo\'shiqlar</div>'
                            report_html += '<div class="mt-track-list">'
                            if parsed.get("tracks"):
                                report_html += render_tracks_html(parsed["tracks"])
                            report_html += '</div></div>'
                            st.session_state.mood_history[-1] = {"role": "assistant", "content": report_html, "html": True}
                    except Exception as e:
                        st.error(f"Xatolik: {e}")
                    st.rerun()
            else:
                remaining = 2 - st.session_state.mood_msg_count
                st.markdown(f'<div style="color:var(--muted);font-size:0.84rem;padding:10px 0">🔒 Yana {remaining} ta javob bering</div>', unsafe_allow_html=True)
        with col_reset:
            if st.button("🔄 Yangilash", key="mood_reset"):
                st.session_state.mood_history = []
                st.session_state.mood_msg_count = 0
                st.rerun()

        # INPUT
        user_text = st.text_area(
            "", 
            placeholder="Javobingizni erkin yozing...",
            key="mood_input",
            label_visibility="collapsed",
            height=80
        )
        send_col, _ = st.columns([1, 5])
        with send_col:
            if st.button("➤ Yuborish", key="mood_send"):
                text = user_text.strip()
                if text:
                    st.session_state.mood_msg_count += 1
                    st.session_state.mood_history.append({"role": "user", "content": text})
                    try:
                        reply = claude_call(st.session_state.mood_history, MOOD_SYSTEM)
                        parsed = parse_mood_reply(reply)
                        if parsed["type"] == "report":
                            report_html = f'''<div class="mt-report">
                                <div class="mt-report-header">▶ <span class="mt-report-title">Mood Analysis & Music Picks</span></div>
                                <div class="mt-mood-meta">'''
                            if parsed.get("mood"):
                                report_html += f'<span class="mt-mood-tag"><span class="mt-tag-lbl">😌 Kayfiyat</span><span class="mt-tag-val">{parsed["mood"]}</span></span>'
                            if parsed.get("style"):
                                report_html += f'<span class="mt-mood-tag"><span class="mt-tag-lbl">🎨 Uslub</span><span class="mt-tag-val">{parsed["style"]}</span></span>'
                            if parsed.get("genres"):
                                report_html += f'<span class="mt-mood-tag"><span class="mt-tag-lbl">🎵 Janr</span><span class="mt-tag-val">{parsed["genres"]}</span></span>'
                            report_html += '</div><div class="mt-tracks-header">🎧 Tavsiya etiladigan qo\'shiqlar</div>'
                            report_html += '<div class="mt-track-list">'
                            if parsed.get("tracks"):
                                report_html += render_tracks_html(parsed["tracks"])
                            report_html += '</div></div>'
                            st.session_state.mood_history.append({"role": "assistant", "content": report_html, "html": True})
                        else:
                            st.session_state.mood_history.append({"role": "assistant", "content": parsed["content"]})
                    except Exception as e:
                        st.session_state.mood_history.append({"role": "assistant", "content": f"⚠️ Xatolik: {e}"})
                    st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

# ── PAGE: MOOD TEST ────────────────────────────────────────────────────────────
elif st.session_state.current_page == "test":
    st.markdown('<div class="mt-page">', unsafe_allow_html=True)

    if not st.session_state.test_done:
        # Progress
        answered = len(st.session_state.test_answers)
        current_q_idx = answered  # 0-based

        # Test Header
        st.markdown(f'''<div class="mt-test-card">
            <div class="mt-test-header">
                <div class="mt-test-title">🎭 Kayfiyat Testi</div>
                <div class="mt-test-sub">4 ta savol asosida musiqa tavsiya qilamiz</div>
            </div>''', unsafe_allow_html=True)

        # Progress dots
        dots_html = '<div class="mt-q-progress"><div class="mt-progress-dots">'
        for i in range(4):
            if i < answered:
                cls = "done"
            elif i == answered:
                cls = "current"
            else:
                cls = ""
            dots_html += f'<div class="mt-dot {cls}"></div>'
        dots_html += f'</div> Savol {min(answered+1, 4)} / 4</div>'
        st.markdown(dots_html, unsafe_allow_html=True)

        if current_q_idx < 4:
            q = TEST_QUESTIONS[current_q_idx]
            st.markdown(f'<div class="mt-q-text">{q["text"]}</div>', unsafe_allow_html=True)

            for opt in q["options"]:
                sub_html = f'<div class="mt-opt-sub">{opt["sub"]}</div>' if opt["sub"] else ""
                btn_html = f'''<div class="mt-opt-btn" style="cursor:pointer">
                    <span class="mt-opt-key">{opt["key"]}</span>{opt["label"]}{sub_html}
                </div>'''
                if st.button(f'{opt["key"]}) {opt["label"]}', key=f'q{current_q_idx}_{opt["key"]}'):
                    st.session_state.test_answers[q["id"]] = f'{opt["key"]}) {opt["label"]}'
                    if len(st.session_state.test_answers) == 4:
                        st.session_state.test_done = True
                        # Get result from Claude
                        try:
                            result = mood_test_call(st.session_state.test_answers)
                            st.session_state.test_result = result
                        except Exception as e:
                            st.session_state.test_result = {
                                "vibe": "Lirika / Sokinlik",
                                "description": "Sizning kayfiyatingizga mos musiqa tavsiya qilamiz.",
                                "genres": ["Pop", "Indie", "Acoustic"],
                                "tracks": []
                            }
                    st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

    else:
        # RESULT
        result = st.session_state.test_result
        if result:
            vibe = result.get("vibe", "")
            vibe_meta = VIBE_INFO.get(vibe, {"emoji": "🎵", "color": "#ff9100"})
            desc = result.get("description", "")
            genres = result.get("genres", [])
            tracks = result.get("tracks", [])

            genres_html = "".join([f'<span class="mt-result-genre-tag">{g}</span>' for g in genres])
            st.markdown(f'''<div class="mt-result-card">
                <div class="mt-result-header">
                    <div class="mt-result-vibe">{vibe_meta["emoji"]}</div>
                    <div class="mt-result-title">{vibe}</div>
                    <div class="mt-result-desc">{desc}</div>
                </div>
                <div class="mt-result-genres">{genres_html}</div>
                <div style="padding:4px 10px 12px">
                    <div class="mt-tracks-header">🎧 Siz uchun qo\'shiqlar</div>
                    <div class="mt-track-list">{render_tracks_html(tracks)}</div>
                </div>
            </div>''', unsafe_allow_html=True)

        col_retry, col_mood = st.columns(2)
        with col_retry:
            if st.button("🔄 Testni qayta o'tkazish", key="retry_test"):
                st.session_state.test_answers = {}
                st.session_state.test_done = False
                st.session_state.test_result = None
                st.rerun()
        with col_mood:
            if st.button("💬 Mood Chat ga o'tish", key="go_mood"):
                st.session_state.current_page = "mood"
                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ── PAGE: MUSIC INFO ───────────────────────────────────────────────────────────
elif st.session_state.current_page == "info":
    st.markdown('<div class="mt-page">', unsafe_allow_html=True)

    # Welcome + chips
    if not st.session_state.info_history:
        st.markdown('''<div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:24px;margin-bottom:20px">
            <div style="font-size:2rem;margin-bottom:10px">🎤</div>
            <div style="font-size:1.15rem;font-weight:700;margin-bottom:6px">Music Info Assistant</div>
            <div style="color:var(--muted);font-size:0.86rem">Artist, albom yoki qo\'shiq haqida biror narsa so\'rang.</div>
        </div>''', unsafe_allow_html=True)

        chips = ["The Weeknd", "Eminem", "Billie Eilish", "Drake", "Скриптонит", "BAKR", "Michael Jackson", "Taylor Swift"]
        chip_cols = st.columns(4)
        for i, chip in enumerate(chips):
            with chip_cols[i % 4]:
                if st.button(chip, key=f"chip_{chip}"):
                    query = f"{chip} haqida aytib ber"
                    st.session_state.info_history.append({"role": "user", "content": query})
                    try:
                        raw = claude_call(st.session_state.info_history, INFO_SYSTEM, max_tokens=1500)
                        raw = re.sub(r'```json|```', '', raw).strip()
                        data = json.loads(raw)
                        card_html = render_info_card(data)
                        st.session_state.info_history.append({"role": "assistant", "content": card_html, "html": True})
                    except Exception as e:
                        st.session_state.info_history.append({"role": "assistant", "content": f"⚠️ Xatolik: {e}"})
                    st.rerun()

    # Chat messages
    chat_html = ""
    for msg in st.session_state.info_history:
        role = msg["role"]
        content = msg["content"]
        css_cls = "bot" if role == "assistant" else "user"
        avatar = "🎤" if role == "assistant" else "👤"
        if msg.get("html"):
            bubble = f'<div class="mt-bubble">{content}</div>'
        else:
            safe_content = content.replace("<", "&lt;").replace(">", "&gt;")
            bubble = f'<div class="mt-bubble">{safe_content}</div>'
        chat_html += f'<div class="mt-msg {css_cls}"><div class="mt-avatar">{avatar}</div>{bubble}</div>'
    if chat_html:
        st.markdown(chat_html, unsafe_allow_html=True)

    # Reset
    if st.session_state.info_history:
        if st.button("🔄 Suhbatni yangilash", key="info_reset"):
            st.session_state.info_history = []
            st.rerun()

    # Input
    info_text = st.text_area(
        "",
        placeholder="Artist, albom yoki qo'shiq haqida so'rang...",
        key="info_input",
        label_visibility="collapsed",
        height=80
    )
    send_col2, _ = st.columns([1, 5])
    with send_col2:
        if st.button("➤ Yuborish", key="info_send"):
            text = info_text.strip()
            if text:
                st.session_state.info_history.append({"role": "user", "content": text})
                try:
                    raw = claude_call(st.session_state.info_history, INFO_SYSTEM, max_tokens=1500)
                    raw = re.sub(r'```json|```', '', raw).strip()
                    data = json.loads(raw)
                    card_html = render_info_card(data)
                    st.session_state.info_history.append({"role": "assistant", "content": card_html, "html": True})
                except Exception as e:
                    error_msg = f"⚠️ Xatolik: {e}"
                    try:
                        # Fallback: plain text
                        raw_text = claude_call(
                            st.session_state.info_history,
                            "Sen musiqa bo'yicha ekspert assistantsan. Qisqa va aniq javob ber.",
                            max_tokens=800
                        )
                        st.session_state.info_history.append({"role": "assistant", "content": raw_text})
                    except:
                        st.session_state.info_history.append({"role": "assistant", "content": error_msg})
                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
