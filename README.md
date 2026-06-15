# MoodTune AI — Streamlit versiyasi

## O'rnatish va ishga tushirish

### 1. Kutubxonalarni o'rnatish
```bash
pip install -r requirements.txt
```

### 2. API kalitini sozlash
```bash
# Linux/Mac
export ANTHROPIC_API_KEY="sk-ant-..."

# Windows (PowerShell)
$env:ANTHROPIC_API_KEY="sk-ant-..."
```

### 3. Ilovani ishga tushirish
```bash
streamlit run app.py
```

Brauzer avtomatik ochiladi: `http://localhost:8501`

---

## Xususiyatlar

- 🎵 **Mood Chat** — AI bilan suhbat orqali musiqa tavsiya
- 🎭 **Mood Test** — 4 savollik interaktiv test (YANGI!)
- 🎤 **Music Info** — Artist/albom/qo'shiq haqida ma'lumot
- 🔥 **Trending** — Trend qo'shiqlarni YouTube da tinglash
- 🌐 **Ko'p tilli** — UZ/RU/EN (Mood Chat da)

## Loyiha tuzilmasi
```
app.py          ← Asosiy Streamlit ilovasi
requirements.txt← Kerakli kutubxonalar
README.md       ← Ushbu fayl
```

## Texnik ma'lumot
- Backend: Python + Anthropic SDK
- Frontend: Streamlit + Custom CSS
- Model: claude-sonnet-4-6
- API CORS muammosi yo'q (server tomonida chaqiriladi)
