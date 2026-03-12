# 🛡️ SomaliTutor

> Connecting Somali diaspora families with verified teachers for **Quran, Somali Language & Arabic**.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB)](https://python.org)

---

## 🚀 One-Click Deploy to Streamlit Cloud

1. **Fork this repo** on GitHub
2. Go to **[share.streamlit.io](https://share.streamlit.io)**
3. Click **"New app"**
4. Select your forked repo → branch `main` → main file `app.py`
5. Click **"Deploy"** — done in ~60 seconds ✅

---

## 💻 Run Locally

```bash
# 1. Clone
git clone https://github.com/YOUR_USERNAME/somalitutor.git
cd somalitutor

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run
streamlit run app.py
```

Opens at **http://localhost:8501**

---

## 🔐 Demo Login Accounts

| Role    | Email                | Password   |
|---------|----------------------|------------|
| 👩 Parent  | parent@demo.com   | demo1234   |
| 👩‍🏫 Teacher | teacher@demo.com  | demo1234   |
| ⚙️ Admin   | admin@demo.com    | admin1234  |

---

## 📁 File Structure

```
somalitutor/
├── app.py                  ← Entire app (single file, Streamlit Cloud compatible)
├── requirements.txt        ← Python dependencies
├── README.md
├── .gitignore
└── .streamlit/
    ├── config.toml         ← Theme + server settings
    └── secrets.toml        ← API keys (gitignored, set on Streamlit Cloud)
```

> **Why single file?** Streamlit Cloud has issues resolving relative imports
> from subfolders. One `app.py` = zero import errors, guaranteed deployment.

---

## ✨ Features

| Page | What it does |
|------|-------------|
| 🏠 Home | Hero, stats counter, featured teachers, testimonials |
| 🔍 Find a Tutor | Search + filter by subject, price, rating, gender, availability |
| 🤖 AI Matching | 6-question wizard → compatibility scoring → ranked matches |
| 📅 My Bookings | Upcoming/past lessons, book new lesson with date picker |
| 📊 Progress | Skill tree, badge collection, Plotly charts |
| 💳 Pricing | 4 plans, monthly/annual toggle, promo codes (SOMALI10, FIRST20) |
| 🔐 Login | Demo accounts, form validation |
| ✍️ Sign Up | Role selection (parent/teacher), account creation |
| 👤 My Account | Profile, subscription, notification preferences |
| 🎓 Teacher Hub | Earnings dashboard, student list, withdrawal, profile settings |
| ⚙️ Admin | KPIs, moderation, disputes, finance, analytics charts |

---

## 🛣️ Roadmap

- [x] Streamlit MVP with all 11 pages
- [ ] Connect Supabase (real database + auth)
- [ ] Stripe payments (real checkout)
- [ ] Live video via Agora/Twilio
- [ ] Push notifications via WhatsApp API
- [ ] iOS & Android mobile apps

---

## 📄 License

MIT © 2025 SomaliTutor

*Built with ❤️ for the Somali diaspora community 🇸🇴*
