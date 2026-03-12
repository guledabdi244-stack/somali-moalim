“”“SomaliTutor — Streamlit App (single-file, Streamlit Cloud compatible)”””
import streamlit as st
import pandas as pd
import plotly.express as px
import time
import datetime
import random

st.set_page_config(
page_title=“SomaliTutor — Verified Somali Teachers Worldwide”,
page_icon=“🛡️”,
layout=“wide”,
initial_sidebar_state=“expanded”,
)

st.markdown(”””

<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700;800&family=Playfair+Display:wght@700;800;900&display=swap');

html, body, [class*="css"] { font-family: 'Sora', sans-serif !important; color: #0B1429 !important; }
#MainMenu {visibility: hidden;} footer {visibility: hidden;} .stDeployButton {display: none;}
.main .block-container { padding: 2rem 2.5rem 4rem !important; max-width: 1300px !important; }

/* SIDEBAR */
[data-testid="stSidebar"] { background: #FFFFFF !important; border-right: 2px solid #E8EDF5 !important; }
[data-testid="stSidebar"] .stRadio label {
    font-size: 14px !important; font-weight: 600 !important; color: #1E293B !important;
    padding: 8px 12px !important; border-radius: 8px !important; white-space: nowrap !important;
    display: flex !important; align-items: center !important; gap: 8px !important;
}
[data-testid="stSidebar"] .stCaption { color: #64748B !important; font-size: 12px !important; }

/* BUTTONS */
.stButton > button {
    font-family: 'Sora', sans-serif !important; font-weight: 700 !important; font-size: 14px !important;
    border-radius: 12px !important; padding: 10px 20px !important; transition: all 0.2s !important;
    border: 2px solid #E4E9F2 !important; color: #1E293B !important; background: white !important;
}
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #0F9B58, #13C46E) !important;
    border: none !important; color: white !important;
    box-shadow: 0 4px 14px rgba(15,155,88,0.3) !important;
}
.stButton > button[kind="primary"]:hover { transform: translateY(-2px) !important; box-shadow: 0 6px 20px rgba(15,155,88,0.4) !important; }

/* METRIC CARDS */
[data-testid="stMetric"] {
    background: white !important; border: 1px solid #E4E9F2 !important;
    border-radius: 16px !important; padding: 20px 24px !important;
    box-shadow: 0 2px 12px rgba(11,31,74,0.07) !important;
}
[data-testid="stMetricLabel"] p { font-weight: 700 !important; font-size: 12px !important; text-transform: uppercase !important; letter-spacing: 0.06em !important; color: #64748B !important; }
[data-testid="stMetricValue"] { font-family: 'Playfair Display', serif !important; font-size: 2rem !important; font-weight: 900 !important; color: #0B1F4A !important; }

/* TABS */
.stTabs [data-baseweb="tab-list"] { gap: 6px !important; background: #F8FAFC !important; border-radius: 12px !important; padding: 6px !important; }
.stTabs [data-baseweb="tab"] { border-radius: 8px !important; font-weight: 700 !important; font-size: 14px !important; color: #64748B !important; padding: 8px 16px !important; background: transparent !important; }
.stTabs [aria-selected="true"] { background: white !important; color: #0F9B58 !important; box-shadow: 0 2px 8px rgba(11,31,74,0.08) !important; }

/* INPUTS */
.stTextInput input, .stTextArea textarea, .stNumberInput input {
    font-family: 'Sora', sans-serif !important; border-radius: 10px !important;
    border: 2px solid #E4E9F2 !important; font-size: 14px !important; color: #0B1429 !important; background: white !important;
}
label { font-weight: 600 !important; font-size: 14px !important; color: #1E293B !important; }

/* ALERTS */
.stAlert { border-radius: 12px !important; font-size: 14px !important; }

/* EXPANDER */
.streamlit-expanderHeader { font-weight: 700 !important; font-size: 15px !important; color: #0B1F4A !important; }

/* PROGRESS */
.stProgress > div > div { background: linear-gradient(90deg, #0F9B58, #13C46E) !important; border-radius: 6px !important; }

/* TYPOGRAPHY */
h1 { font-family: 'Playfair Display', serif !important; color: #0B1F4A !important; font-weight: 900 !important; }
h2 { color: #0B1F4A !important; font-weight: 800 !important; }
h3 { color: #0B1F4A !important; font-weight: 700 !important; }
p  { color: #1E293B !important; line-height: 1.7 !important; }
hr { border-color: #E8EDF5 !important; }

/* CUSTOM CARDS */
.hero {
    background: linear-gradient(155deg, #0B1F4A 0%, #152D6E 55%, #1A4A9F 100%);
    border-radius: 24px; padding: 52px; color: white; margin-bottom: 28px;
    box-shadow: 0 8px 32px rgba(11,31,74,0.25);
}
.hero h1 { font-family: 'Playfair Display', serif; font-size: 2.8rem; font-weight: 900; color: white !important; margin-bottom: 14px; line-height: 1.15; }
.hero p  { font-size: 1.05rem; color: rgba(255,255,255,0.8) !important; line-height: 1.75; }
.tc {
    background: white; border: 1px solid #E8EDF5; border-radius: 20px; padding: 24px;
    box-shadow: 0 2px 14px rgba(11,31,74,0.07); margin-bottom: 12px;
}
.sc {
    background: white; border: 1px solid #E8EDF5; border-radius: 16px; padding: 22px;
    box-shadow: 0 2px 10px rgba(11,31,74,0.06); margin-bottom: 14px;
}
.nv {
    background: linear-gradient(135deg, #0B1F4A, #152D6E); border-radius: 20px;
    padding: 32px; color: white; margin-bottom: 16px; box-shadow: 0 6px 24px rgba(11,31,74,0.2);
}
.stCheckbox label { font-size: 14px !important; color: #1E293B !important; font-weight: 500 !important; }
</style>

“””, unsafe_allow_html=True)

# ── DATA ──────────────────────────────────────────────────────────────────────

TEACHERS = [
{“id”:1,“name”:“Khadra Hassan”,“emoji”:“👩🏽‍🏫”,“headline”:“Quran & Somali Expert”,“subjects”:[“Quran”,“Somali”,“Arabic”],“rating”:4.9,“reviews”:127,“lessons”:380,“price”:15,“verify_level”:5,“online”:True,“badge”:“diamond”,“rebooking”:92,“completion”:99,“response_time”:”<30 min”,“bio”:“Hafidha with Ijaazah. 10+ years teaching diaspora children Quran with beautiful Tajweed.”,“gender”:“female”,“age_groups”:[“5-8”,“9-12”,“13+”],“next_slot”:“Today 4 PM”},
{“id”:2,“name”:“Ahmed Farah”,“emoji”:“👨🏽‍🏫”,“headline”:“Somali & English Tutor”,“subjects”:[“Somali”,“English”,“Math”],“rating”:4.8,“reviews”:89,“lessons”:215,“price”:12,“verify_level”:4,“online”:False,“badge”:“gold”,“rebooking”:78,“completion”:97,“response_time”:”<1 hr”,“bio”:“8 years experience. Fun structured lessons for diaspora kids aged 7–14.”,“gender”:“male”,“age_groups”:[“7-10”,“11-14”],“next_slot”:“Tomorrow 10 AM”},
{“id”:3,“name”:“Hodan Warsame”,“emoji”:“👩🏾‍🏫”,“headline”:“Quran Memorisation Specialist”,“subjects”:[“Quran”,“Arabic”,“Islamic Studies”],“rating”:4.9,“reviews”:204,“lessons”:501,“price”:18,“verify_level”:5,“online”:True,“badge”:“diamond”,“rebooking”:95,“completion”:99,“response_time”:”<30 min”,“bio”:“Hafidha helping 50+ children complete their full Quran journey with confidence.”,“gender”:“female”,“age_groups”:[“5-8”,“9-12”,“13+”],“next_slot”:“Today 6 PM”},
{“id”:4,“name”:“Abdi Nur”,“emoji”:“👨🏾‍🎓”,“headline”:“Math & Somali for Teens”,“subjects”:[“Math”,“Somali”],“rating”:4.6,“reviews”:34,“lessons”:48,“price”:10,“verify_level”:3,“online”:True,“badge”:“rising”,“rebooking”:65,“completion”:94,“response_time”:”<3 hr”,“bio”:“Education student. Energetic and relatable for teens.”,“gender”:“male”,“age_groups”:[“11-14”,“15+”],“next_slot”:“Fri 3 PM”},
{“id”:5,“name”:“Safia Omar”,“emoji”:“👩🏽‍💼”,“headline”:“Arabic & Islamic Studies”,“subjects”:[“Arabic”,“Quran”,“Islamic Studies”],“rating”:4.7,“reviews”:67,“lessons”:142,“price”:14,“verify_level”:4,“online”:False,“badge”:“trusted”,“rebooking”:80,“completion”:96,“response_time”:”<1 hr”,“bio”:“Classical Arabic teacher trained in Cairo. Makes Arabic accessible for all ages.”,“gender”:“female”,“age_groups”:[“5-8”,“9-12”,“13+”],“next_slot”:“Sat 11 AM”},
{“id”:6,“name”:“Faarax Ali”,“emoji”:“👨🏾‍🏫”,“headline”:“Somali Culture & Language”,“subjects”:[“Somali”,“History”],“rating”:4.5,“reviews”:22,“lessons”:31,“price”:8,“verify_level”:2,“online”:False,“badge”:“new”,“rebooking”:55,“completion”:90,“response_time”:”<6 hr”,“bio”:“Native speaker sharing Somali heritage through oral storytelling.”,“gender”:“male”,“age_groups”:[“9-12”,“13+”],“next_slot”:“Mon 5 PM”},
]

PLANS = [
{“id”:“starter”,“name”:“Starter”,“emoji”:“🌱”,“pm”:0,“pa”:0,“popular”:False,“features”:[“1 free trial lesson”,“Browse all tutors”,“Basic progress tracking”,“Email support”]},
{“id”:“family”,“name”:“Family”,“emoji”:“👨‍👩‍👧”,“pm”:49,“pa”:39,“popular”:True,“features”:[“Up to 3 children”,“8 lessons/month”,“AI teacher matching”,“Recordings 30 days”,“Progress PDF reports”,“Priority booking”,“Cancel anytime”]},
{“id”:“premium”,“name”:“Premium”,“emoji”:“💎”,“pm”:89,“pa”:71,“popular”:False,“features”:[“Unlimited children”,“Unlimited lessons”,“AI matching + scheduling”,“Recordings forever”,“Weekly parent call”,“Dedicated account manager”,“Group classes”,“24/7 support”]},
{“id”:“school”,“name”:“School / Org”,“emoji”:“🏫”,“pm”:None,“pa”:None,“popular”:False,“features”:[“Bulk student accounts”,“Admin dashboard”,“Custom reporting”,“API access”,“Invoice billing”,“SLA guarantee”,“Onboarding support”]},
]

AI_QS = [
{“id”:“age”,    “q”:“How old is your child?”,                  “opts”:[“3–6 years”,“7–10 years”,“11–14 years”,“15+ years”]},
{“id”:“subject”,“q”:“What subject are you looking for?”,       “opts”:[“Quran & Tajweed”,“Somali Language”,“Arabic”,“Math”,“Multiple subjects”]},
{“id”:“level”,  “q”:“What is your child’s current level?”,     “opts”:[“Complete beginner”,“Some exposure”,“Intermediate”,“Advanced”]},
{“id”:“style”,  “q”:“How does your child learn best?”,         “opts”:[“Visual (pictures, videos)”,“Auditory (listening, repetition)”,“Reading & writing”,“Hands-on activities”]},
{“id”:“gender”, “q”:“Do you prefer a specific teacher gender?”,“opts”:[“Female teacher”,“Male teacher”,“No preference”]},
{“id”:“budget”, “q”:“What is your budget per lesson?”,         “opts”:[“Under $10”,”$10–$15”,”$15–$20”,”$20+”]},
]

DEMO_USERS = {
“parent@demo.com”:  {“id”:“u1”,“name”:“Faadumo Hassan”,“email”:“parent@demo.com”,“role”:“parent”,“password”:“demo1234”,“children”:[{“name”:“Ayaan”,“age”:9,“goal”:“Quran”,“streak”:5,“lessons”:7},{“name”:“Lul”,“age”:7,“goal”:“Somali”,“streak”:3,“lessons”:4}],“plan”:“family”,“avatar”:“👩🏽”},
“teacher@demo.com”: {“id”:“u2”,“name”:“Khadra Hassan”,“email”:“teacher@demo.com”,“role”:“teacher”,“password”:“demo1234”,“teacher_id”:1,“plan”:None,“avatar”:“👩🏽‍🏫”},
“admin@demo.com”:   {“id”:“u3”,“name”:“Admin User”,“email”:“admin@demo.com”,“role”:“admin”,“password”:“admin1234”,“plan”:None,“avatar”:“⚙️”},
}

# ── SESSION ───────────────────────────────────────────────────────────────────

for k,v in {“user”:None,“nav”:“🏠  Home”,“ai_step”:0,“ai_answers”:{},“ai_matches”:[],“wishlist”:[],“promo_discount”:1.0}.items():
if k not in st.session_state: st.session_state[k]=v

def gu(): return st.session_state.get(“user”)
def rl():
if gu(): return True
st.warning(“Please log in to access this page.”)
c1,c2,_=st.columns([1,1,4])
with c1:
if st.button(“Log In”,type=“primary”): st.session_state.nav=“🔐  Login”; st.rerun()
with c2:
if st.button(“Sign Up”): st.session_state.nav=“✍️  Sign Up”; st.rerun()
return False

def match_score(t,ans):
s=70
sm={“Quran & Tajweed”:“Quran”,“Somali Language”:“Somali”,“Arabic”:“Arabic”,“Math”:“Math”}
w=sm.get(ans.get(“subject”,””),””)
if w and w in t[“subjects”]: s+=15
gp=ans.get(“gender”,“No preference”)
if gp==“Female teacher” and t[“gender”]==“female”: s+=8
elif gp==“Male teacher” and t[“gender”]==“male”: s+=8
elif gp==“No preference”: s+=4
b=ans.get(“budget”,””)
if “Under $10” in b and t[“price”]<=10: s+=10
elif “$10–$15” in b and t[“price”]<=15: s+=8
elif “$15–$20” in b and t[“price”]<=20: s+=5
s+=(t[“rating”]-4.0)*5+t[“rebooking”]*0.05+random.uniform(-3,3)
return min(99,max(50,int(s)))

# ── SIDEBAR ───────────────────────────────────────────────────────────────────

with st.sidebar:
st.markdown(”””
<div style='text-align:center; padding:24px 16px 20px; border-bottom:2px solid #E8EDF5; margin-bottom:12px;'>
<div style='font-size:52px; margin-bottom:8px;'>🛡️</div>
<div style='font-size:20px; font-weight:900; color:#0B1F4A; letter-spacing:-0.5px;'>SomaliTutor</div>
<div style='font-size:11px; color:#64748B; margin-top:4px; font-weight:500;'>Verified Teachers Worldwide</div>
</div>
“””, unsafe_allow_html=True)

```
NAVS = [
    "🏠  Home",
    "🔍  Find a Tutor",
    "🤖  AI Matching",
    "📅  My Bookings",
    "📊  Progress",
    "💳  Pricing",
    "🔐  Login",
    "✍️  Sign Up",
    "👤  My Account",
    "🎓  Teacher Hub",
    "⚙️  Admin",
]
idx = NAVS.index(st.session_state.nav) if st.session_state.nav in NAVS else 0
nav = st.radio("Navigation", NAVS, index=idx, label_visibility="collapsed")
st.session_state.nav = nav

st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
st.divider()

user = gu()
if user:
    role_color = {"parent":"#0F9B58","teacher":"#6D28D9","admin":"#DC2626"}.get(user.get("role","parent"),"#0F9B58")
    st.markdown(f"""
    <div style='background:#F0FDF8;border:1px solid #BBF7D0;border-radius:12px;padding:12px 14px;margin:8px 0 12px;'>
        <div style='font-size:13px;color:#064E3B;font-weight:700;'>👋 Welcome back!</div>
        <div style='font-size:15px;color:#0B1F4A;font-weight:800;margin-top:2px;'>{user["name"]}</div>
        <div style='font-size:11px;background:{role_color};color:white;border-radius:20px;padding:2px 10px;display:inline-block;margin-top:6px;font-weight:700;text-transform:uppercase;letter-spacing:0.05em;'>{user.get("role","parent")}</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🚪  Log Out", use_container_width=True):
        st.session_state.user = None; st.session_state.nav = "🏠  Home"; st.rerun()
else:
    st.markdown("<div style='padding:8px 0 4px;font-size:12px;color:#64748B;font-weight:600;text-transform:uppercase;letter-spacing:0.05em;'>Get Started</div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Log In", use_container_width=True): st.session_state.nav = "🔐  Login"; st.rerun()
    with c2:
        if st.button("Sign Up", use_container_width=True, type="primary"): st.session_state.nav = "✍️  Sign Up"; st.rerun()

st.divider()
st.markdown("""
<div style='padding:8px 4px; font-size:12px; color:#94A3B8; line-height:1.8;'>
    📞 support@somalitutor.com<br>
    🌍 somalitutor.com<br>
    <span style='color:#CBD5E1;'>v2.0 · Built with ❤️</span>
</div>
""", unsafe_allow_html=True)
```

# ── HOME ──────────────────────────────────────────────────────────────────────

def page_home():
user=gu()
if user:
st.markdown(f’<div class="hero"><h1>Welcome back, {user[“name”]}! 👋</h1><p>Your child's heritage journey continues. Check bookings, track progress, or find a new teacher.</p></div>’, unsafe_allow_html=True)
else:
st.markdown(’<div class="hero"><h1>Your Child's Bridge to Somali Heritage 🌍</h1><p>Verified Somali teachers for Quran, Somali Language & Arabic. AI-matched live 1-on-1 lessons built for diaspora families worldwide.</p><p style="font-size:13px;margin-top:12px">✅ First lesson free  ·  ✅ No credit card  ·  ✅ Cancel anytime</p></div>’, unsafe_allow_html=True)
c1,c2,*=st.columns([1,1,3])
with c1:
if st.button(“🤖 Get AI-Matched Free”,type=“primary”,use_container_width=True): st.session_state.nav=“🤖  AI Matching”; st.rerun()
with c2:
if st.button(“🔍 Browse Teachers”,use_container_width=True): st.session_state.nav=“🔍  Find a Tutor”; st.rerun()
st.markdown(”—”)
st.markdown(”<p style='font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:0.08em;color:#94A3B8;margin-bottom:16px;'>PLATFORM STATS</p>”, unsafe_allow_html=True)
k1,k2,k3,k4=st.columns(4)
k1.metric(“🌍 Families Enrolled”, “2,000+”, “+12% this month”)
k2.metric(“🎓 Verified Teachers”, “150+”,   “+8 this week”)
k3.metric(“📚 Lessons Completed”,“12,400+”, “98% completion”)
k4.metric(“⭐ Average Rating”,   “4.9 / 5”, “1,204 reviews”)
st.markdown(”—”)
st.subheader(“⭐ Top Rated Teachers This Week”)
cols=st.columns(3)
for i,t in enumerate(sorted(TEACHERS,key=lambda x:-x[“rating”])[:3]):
with cols[i]:
st.markdown(f’<div class="tc"><div style="font-size:48px;text-align:center;margin-bottom:8px">{t[“emoji”]}</div><div style="font-weight:800;font-size:16px;color:#0B1F4A;text-align:center">{t[“name”]}</div><div style="color:#64748B;font-size:12px;text-align:center;margin:4px 0 8px">{t[“headline”]}</div><div style="display:flex;justify-content:space-between;font-size:13px"><span>⭐ {t[“rating”]} ({t[“reviews”]})</span><span style="font-weight:800;color:#0F9B58">${t[“price”]}/hr</span></div><div style="color:#94A3B8;font-size:11px;margin-top:6px">🗓️ Next: {t[“next_slot”]}</div></div>’, unsafe_allow_html=True)
col_a, col_b = st.columns(2)
with col_a:
if st.button(f”📅 Book”, key=f”h_book*{t[‘id’]}”, use_container_width=True, type=“primary”):
st.session_state.nav=“📅  My Bookings”; st.rerun()
with col_b:
wl = st.session_state.wishlist
if st.button(“❤️” if t[“id”] in wl else “🤍”, key=f”h_wish_{t[‘id’]}”, use_container_width=True):
if t[“id”] in wl: wl.remove(t[“id”])
else: wl.append(t[“id”])
st.rerun()
st.markdown(”—”)
st.subheader(“🚀 How It Works”)
s1,s2,s3=st.columns(3)
with s1: st.info(”**Step 1: AI Matches You 🤖**\n\nAnswer 6 questions. Our algorithm finds your top 3 teacher matches instantly.”)
with s2: st.success(”**Step 2: Book Free Trial 🎁**\n\nBook a free 30-minute trial. No payment needed.”)
with s3: st.warning(”**Step 3: Start the Journey 🚀**\n\nTrack progress weekly, celebrate milestones.”)
st.markdown(”—”)
st.subheader(“💬 What Families Say”)
t1,t2,t3=st.columns(3)
for col,(n,loc,txt) in zip([t1,t2,t3],[(“Faadumo Abdi”,“🇬🇧 London, UK”,“My son went from zero Somali to full conversations in 4 months. Incredible!”),(“Mahad Osman”,“🇺🇸 Minneapolis”,“Teacher Hodan is exceptional. My daughter’s Quran improved beyond anything I expected.”),(“Lul Ahmed”,“🇨🇦 Toronto”,“My son completed his full Quran in 18 months with Teacher Khadra.”)]):
with col:
st.markdown(f’<div class="sc"><div>⭐⭐⭐⭐⭐</div><p style="color:#0B1429;font-size:13px;line-height:1.7;margin:10px 0">”{txt}”</p><div style="font-weight:700;font-size:13px;color:#0B1F4A">{n}</div><div style="font-size:11px;color:#64748B">{loc}</div></div>’, unsafe_allow_html=True)

# ── FIND ──────────────────────────────────────────────────────────────────────

def page_find():
st.title(“🔍 Find a Tutor”)
with st.expander(“🎛️ Filters”,expanded=True):
c1,c2,c3,c4=st.columns(4)
with c1: subj=st.selectbox(“Subject”,[“All”,“Quran”,“Somali”,“Arabic”,“Math”,“English”,“Islamic Studies”])
with c2: maxp=st.slider(“Max price/hr ($)”,5,50,50)
with c3: minr=st.select_slider(“Min rating”,[0.0,4.0,4.5,4.8,4.9],0.0,format_func=lambda x:“Any” if x==0 else f”★{x}+”)
with c4: gend=st.selectbox(“Gender”,[“Any”,“Female”,“Male”])
c5,c6=st.columns(2)
with c5: only_on=st.checkbox(“Online now only”)
with c6: sortby=st.selectbox(“Sort by”,[“Top Rated”,“Price ↑”,“Most Lessons”])
ts=[t for t in TEACHERS if(subj==“All” or subj in t[“subjects”]) and t[“price”]<=maxp and t[“rating”]>=(minr or 0) and(gend==“Any” or t[“gender”]==gend.lower()) and(not only_on or t[“online”])]
ts=sorted(ts,key={“Top Rated”:lambda x:-x[“rating”],“Price ↑”:lambda x:x[“price”],“Most Lessons”:lambda x:-x[“lessons”]}[sortby])
st.markdown(f”**{len(ts)} teachers found**”)
if not ts: st.info(“No teachers match your filters.”); return
vw=st.radio(“View”,[“🃏 Cards”,“📋 Table”],horizontal=True,label_visibility=“collapsed”)
if “Table” in vw:
st.dataframe(pd.DataFrame([{“Name”:f”{t[‘emoji’]} {t[‘name’]}”,“Subjects”:”, “.join(t[‘subjects’]),“Rating”:t[“rating”],“Price”:f”${t[‘price’]}/hr”,“Lessons”:t[“lessons”],“Online”:“🟢” if t[“online”] else “⚪”,“Next”:t[“next_slot”]} for t in ts]),use_container_width=True,hide_index=True)
return
for i in range(0,len(ts),2):
cols=st.columns(2)
for j,col in enumerate(cols):
if i+j>=len(ts): break
t=ts[i+j]
with col:
ol_tag=’<span style="background:#E6F9F0;color:#0F9B58;border-radius:20px;padding:2px 8px;font-size:11px;font-weight:700">● Online</span>’ if t[“online”] else “”
subj_html = “”.join(f’<span style="background:#F1F5F9;border-radius:6px;padding:2px 8px;font-size:11px;font-weight:600;color:#0B1F4A">{s}</span>’ for s in t[“subjects”])
shield = “\U0001f6e1\ufe0f” * t[“verify_level”]
html = (
f’’’<div class="tc"><div style="display:flex;gap:14px;align-items:flex-start">’’’
f’’’<span style="font-size:48px">{t[“emoji”]}</span>’’’
f’’’<div style="flex:1"><div style="font-weight:800;font-size:16px;color:#0B1F4A">{t[“name”]} {ol_tag}</div>’’’
f’’’<div style="color:#64748B;font-size:12px;margin:3px 0">{t[“headline”]}</div>’’’
f’’’<div style="font-size:11px;color:#94A3B8">{shield} · {t[“badge”].title()}</div></div>’’’
f’’’<div style="text-align:right"><div style="font-size:24px;font-weight:900;color:#0F9B58">${t[“price”]}</div>’’’
f’’’<div style="font-size:10px;color:#64748B">/hour</div></div></div>’’’
f’’’<p style="color:#0B1429;font-size:13px;line-height:1.6;margin:12px 0 8px">{t[“bio”]}</p>’’’
f’’’<div style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:10px">{subj_html}</div>’’’
f’’’<div style="display:flex;justify-content:space-between;font-size:12px;color:#64748B">’’’
f’’’<span>\u2b50 {t[“rating”]} ({t[“reviews”]})</span><span>\u2705 {t[“completion”]}%</span><span>\U0001f501 {t[“rebooking”]}%</span></div>’’’
f’’’<div style="font-size:11px;color:#0F9B58;margin-top:6px">\U0001f5d3\ufe0f Next: {t[“next_slot”]}</div></div>’’’
)
st.markdown(html, unsafe_allow_html=True)
b1,b2,b3=st.columns(3)
with b1:
if st.button(“📅 Book”,key=f”fb_{t[‘id’]}”,use_container_width=True,type=“primary”): st.success(f”Booking {t[‘name’]}…”)
with b2:
wl=st.session_state.wishlist
if st.button(“❤️” if t[“id”] in wl else “🤍”,key=f”fw_{t[‘id’]}”,use_container_width=True):
if t[“id”] in wl: wl.remove(t[“id”])
else: wl.append(t[“id”])
st.rerun()
with b3:
if st.button(“💬 Chat”,key=f”fc_{t[‘id’]}”,use_container_width=True): st.info(f”Opening chat with {t[‘name’]}…”)

# ── AI MATCHING ───────────────────────────────────────────────────────────────

def page_ai():
st.markdown(’<div class="hero"><h1>🤖 AI Teacher Matching</h1><p>Answer 6 quick questions. Our algorithm analyzes 14 compatibility factors and finds your best matches in seconds.</p></div>’, unsafe_allow_html=True)
step=st.session_state.ai_step; ans=st.session_state.ai_answers; matches=st.session_state.ai_matches
if step==0:
c1,c2=st.columns([2,1])
with c1:
st.markdown(’<div class="sc"><h3 style="color:#0B1F4A;font-weight:800;margin-bottom:12px">How the Algorithm Works</h3><ul style="color:#64748B;font-size:14px;line-height:2.1;padding-left:18px"><li><b>Age-appropriate matching</b> — ranked by success with your child's age group</li><li><b>Subject expertise score</b> — weighted by actual lesson outcomes</li><li><b>Learning style fit</b> — matches teaching method with your child's style</li><li><b>Performance metrics</b> — rating, rebooking, completion, response time</li><li><b>Budget alignment</b> — only shows teachers within your range</li><li><b>Cultural fit</b> — teachers who understand diaspora family experiences</li></ul></div>’, unsafe_allow_html=True)
with c2:
st.markdown(’<div class="sc" style="text-align:center"><div style="font-size:64px;margin-bottom:12px">🤖</div><div style="font-weight:800;color:#0B1F4A">AI Matchmaker</div><div style="color:#64748B;font-size:13px;margin:6px 0">14 factors · 60 seconds</div></div>’, unsafe_allow_html=True)
if st.button(“🤖 Start AI Matching →”,type=“primary”,use_container_width=True):
st.session_state.ai_step=1; st.session_state.ai_answers={}; st.session_state.ai_matches=[]; st.rerun()
return
if 1<=step<=len(AI_QS):
q=AI_QS[step-1]; pct=int((step/len(AI_QS))*100)
st.markdown(f”**Question {step} of {len(AI_QS)}**”); st.progress(pct/100)
st.markdown(f”### {q[‘q’]}”)
di=q[“opts”].index(ans.get(q[“id”])) if ans.get(q[“id”]) in q[“opts”] else 0
chosen=st.radio(””,q[“opts”],index=di,key=f”aiq{step}”,label_visibility=“collapsed”)
c1,c2,c3=st.columns([1,1,4])
with c1:
if step>1 and st.button(“← Back”,use_container_width=True): st.session_state.ai_step-=1; st.rerun()
with c2:
if st.button(“Next →”,type=“primary”,use_container_width=True):
ans[q[“id”]]=chosen; st.session_state.ai_answers=ans
if step==len(AI_QS):
with st.spinner(“🔍 Analysing teachers…”): time.sleep(1.5)
scored=sorted([{**t,“match”:match_score(t,ans)} for t in TEACHERS],key=lambda x:-x[“match”])[:3]
st.session_state.ai_matches=scored; st.session_state.ai_step=99
else: st.session_state.ai_step+=1
st.rerun()
with c3:
if st.button(“Start Over”,use_container_width=True): st.session_state.ai_step=0; st.session_state.ai_answers={}; st.session_state.ai_matches=[]; st.rerun()
return
if step==99:
st.success(“🎯 AI matching complete! Here are your top 3 teacher matches.”)
st.markdown(”**Your profile:** “+”  “.join([f”`{v}`” for v in ans.values()]))
st.markdown(”—”)
for i,t in enumerate(matches):
lbl=“🏆 BEST MATCH” if i==0 else f”#{i+1} Match”; clr=”#0F9B58” if i==0 else “#6D28D9”
with st.expander(f”{lbl} — {t[‘name’]} ({t[‘match’]}% compatibility)”,expanded=(i==0)):
c1,c2=st.columns([3,1])
with c1:
st.markdown(f”### {t[‘emoji’]} {t[‘name’]}”); st.caption(t[“headline”]); st.write(t[“bio”])
m1,m2,m3,m4=st.columns(4)
m1.metric(“⭐ Rating”,t[“rating”]); m2.metric(“✅ Completion”,f”{t[‘completion’]}%”); m3.metric(“🔁 Rebooking”,f”{t[‘rebooking’]}%”); m4.metric(“⚡ Response”,t[“response_time”])
bg=”#E6F9F0” if i==0 else “#EDE9FE”
st.markdown(f’<div style="background:{bg};border-radius:10px;padding:12px 16px;font-size:13px;margin-top:10px">🎯 <b>Why we matched you:</b> {t[“name”]} specializes in {t[“subjects”][0]} with a {t[“rebooking”]}% rebooking rate for similar student profiles.</div>’, unsafe_allow_html=True)
with c2:
st.markdown(f’<div style="text-align:center;background:white;border:2px solid {clr};border-radius:16px;padding:20px"><div style="font-size:40px;font-weight:900;color:{clr}">{t[“match”]}%</div><div style="font-size:11px;color:#64748B;font-weight:700;margin-bottom:10px">MATCH</div><div style="font-size:28px;font-weight:900;color:#0B1F4A">${t[“price”]}</div><div style="font-size:12px;color:#64748B">/hour</div></div>’, unsafe_allow_html=True)
if st.button(“📅 Book”,key=f”mb_{t[‘id’]}”,use_container_width=True,type=“primary”): st.success(f”Booking {t[‘name’]}!”)
wl=st.session_state.wishlist
if st.button(“❤️ Saved” if t[“id”] in wl else “🤍 Save”,key=f”ms_{t[‘id’]}”,use_container_width=True):
if t[“id”] not in wl: wl.append(t[“id”])
st.rerun()
st.markdown(”—”)
if st.button(“🔄 Retake Quiz”,use_container_width=True): st.session_state.ai_step=0; st.session_state.ai_answers={}; st.session_state.ai_matches=[]; st.rerun()

# ── BOOKINGS ──────────────────────────────────────────────────────────────────

def page_bookings():
if not rl(): return
st.title(“📅 My Bookings”)
tab1,tab2,tab3=st.tabs([“Upcoming”,“Past”,“Book New Lesson”])
with tab1:
for b in [{“teacher”:“👩🏽‍🏫 Khadra Hassan”,“subject”:“Somali Language”,“date”:“Fri May 12”,“time”:“4:30 PM”,“price”:”$15”,“child”:“Ayaan”},{“teacher”:“👩🏾‍🏫 Hodan Warsame”,“subject”:“Quran”,“date”:“Sat May 13”,“time”:“10:00 AM”,“price”:”$18”,“child”:“Lul”}]:
st.markdown(f’<div class="sc"><div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px"><div><div style="font-weight:800;font-size:16px;color:#0B1F4A">{b[“teacher”]}</div><div style="color:#64748B;font-size:13px">{b[“subject”]} · {b[“child”]}</div><div style="color:#0F9B58;font-weight:700;font-size:13px">📅 {b[“date”]} at {b[“time”]}</div></div><div style="text-align:right"><div style="font-size:1.3rem;font-weight:900;color:#0B1F4A">{b[“price”]}</div><div style="background:#E6F9F0;color:#0F9B58;border-radius:8px;padding:3px 10px;font-size:11px;font-weight:700;margin-top:4px">Confirmed</div></div></div></div>’, unsafe_allow_html=True)
b1,b2,b3=st.columns(3)
with b1:
if st.button(“🎥 Join Lesson”,key=f”j_{b[‘date’]}”,type=“primary”,use_container_width=True): st.success(“Launching lesson room…”)
with b2:
if st.button(“✏️ Reschedule”,key=f”r_{b[‘date’]}”,use_container_width=True): st.info(“Rescheduling…”)
with b3:
if st.button(“❌ Cancel”,key=f”c_{b[‘date’]}”,use_container_width=True): st.warning(“Lesson cancelled.”)
with tab2:
for b in [{“t”:“👩🏽‍🏫 Khadra Hassan”,“s”:“Somali”,“d”:“May 5”},{“t”:“👩🏾‍🏫 Hodan Warsame”,“s”:“Quran”,“d”:“May 3”}]:
with st.expander(f”{b[‘t’]} — {b[‘s’]} — {b[‘d’]}”):
r=st.slider(“Rate this lesson”,1,5,5,key=f”rt_{b[‘d’]}”)
if st.button(“Submit Rating”,key=f”sr_{b[‘d’]}”): st.success(f”Rated {r}⭐!”)
if st.button(“🔄 Book Again”,key=f”ba_{b[‘d’]}”,type=“primary”): st.success(“Re-booking…”)
with tab3:
c1,c2=st.columns(2)
with c1:
tc=st.selectbox(“Teacher”,[“Khadra Hassan”,“Hodan Warsame”,“Ahmed Farah”,“Safia Omar”])
cc=st.selectbox(“Child”,[“Ayaan”,“Lul”])
sc=st.selectbox(“Subject”,[“Quran”,“Somali”,“Arabic”])
with c2:
ld=st.date_input(“Date”,min_value=datetime.date.today())
lt=st.selectbox(“Time”,[“9:00 AM”,“10:00 AM”,“2:00 PM”,“3:30 PM”,“4:30 PM”,“6:00 PM”])
ltype=st.selectbox(“Type”,[“Regular (60 min)”,“Extended (90 min)”,“Trial (30 min — Free)”])
if st.button(“✅ Confirm Booking”,type=“primary”,use_container_width=True):
st.balloons(); st.success(f”Lesson booked with {tc} on {ld} at {lt}! Check your email.”)

# ── PROGRESS ──────────────────────────────────────────────────────────────────

def page_progress():
if not rl(): return
user=gu(); st.title(“📊 Progress Tracker”)
children=user.get(“children”,[])
if not children: st.info(“No children added yet.”); return
sel=st.selectbox(“Select child”,[c[“name”] for c in children])
child=next(c for c in children if c[“name”]==sel)
k1,k2,k3,k4=st.columns(4)
k1.metric(“📚 Lessons”,child.get(“lessons”,7),”+2 this week”)
k2.metric(“🔥 Streak”,f”{child.get(‘streak’,5)} days”,”+1”)
k3.metric(“🏅 Badges”,“8”,”+1 this week”)
k4.metric(“📈 Progress”,“45%”,”+5%”)
st.markdown(”—”)
tab1,tab2,tab3=st.tabs([“🌳 Skill Tree”,“🏅 Badges”,“📈 Charts”])
with tab1:
subj=st.radio(“Subject”,[“Somali Language”,“Quran Journey”,“Arabic”],horizontal=True)
sm={“Somali Language”:[(“Greetings”,“done”),(“Family & Numbers”,“done”),(“Colours & Animals”,“done”),(“Daily Routines”,“current”),(“Food & Market”,“locked”),(“Storytelling”,“locked”)],“Quran Journey”:[(“Al-Fatiha”,“done”),(“Al-Ikhlas”,“done”),(“Al-Falaq”,“current”),(“An-Nas”,“locked”),(“Al-Kawthar”,“locked”),(“Tajweed”,“locked”)],“Arabic”:[(“Alphabet A-M”,“done”),(“Alphabet N-Y”,“current”),(“Basic Vocab”,“locked”),(“Sentences”,“locked”),(“Reading”,“locked”),(“Writing”,“locked”)]}
skills=sm[subj]; cols=st.columns(len(skills))
for col,(name,status) in zip(cols,skills):
with col:
if status==“done”: st.success(f”✅\n{name}”)
elif status==“current”: st.warning(f”▶️\n{name}”)
else: st.markdown(f’<div style="background:#F1F5F9;border:1px dashed #CBD5E1;border-radius:10px;padding:10px;font-size:11px;color:#94A3B8;text-align:center">🔒<br>{name}</div>’, unsafe_allow_html=True)
done=sum(1 for _,s in skills if s==“done”); st.progress(done/len(skills),text=f”{done}/{len(skills)} skills complete”)
with tab2:
badges=[(“🌟”,“1st Lesson”,True),(“📖”,“5 Lessons”,True),(“🗣️”,“10 Words”,True),(“✅”,“10 Lessons”,True),(“🔥”,“7-Day Streak”,True),(“📿”,“1st Surah”,True),(“🌙”,“Ramadan”,True),(“⭐”,“Top Student”,True),(“🏆”,“25 Lessons”,False),(“💎”,“Hafidh”,False)]
cols=st.columns(5)
for i,(ic,name,earned) in enumerate(badges):
with cols[i%5]:
if earned: st.markdown(f’<div style="text-align:center;background:#FEF3DC;border:2px solid #D4920A;border-radius:12px;padding:12px;margin-bottom:8px"><div style="font-size:30px">{ic}</div><div style="font-weight:700;font-size:11px;color:#0B1F4A;margin-top:4px">{name}</div></div>’, unsafe_allow_html=True)
else: st.markdown(f’<div style="text-align:center;background:#F1F5F9;border:1px dashed #CBD5E1;border-radius:12px;padding:12px;margin-bottom:8px;opacity:0.5"><div style="font-size:30px">🔒</div><div style="font-weight:600;font-size:10px;color:#94A3B8;margin-top:4px">{name}</div></div>’, unsafe_allow_html=True)
with tab3:
df=pd.DataFrame({“Week”:[f”Wk{i+1}” for i in range(8)],“Lessons”:[1,2,1,2,2,1,2,2],“Words”:[5,12,8,18,15,10,20,22]})
c1,c2=st.columns(2)
with c1:
fig=px.bar(df,x=“Week”,y=“Lessons”,title=“Lessons Per Week”,color_discrete_sequence=[”#0F9B58”]); fig.update_layout(plot_bgcolor=“white”,paper_bgcolor=“white”); st.plotly_chart(fig,use_container_width=True)
with c2:
fig2=px.line(df,x=“Week”,y=“Words”,title=“Vocabulary Growth”,color_discrete_sequence=[”#D4920A”],markers=True); fig2.update_layout(plot_bgcolor=“white”,paper_bgcolor=“white”); st.plotly_chart(fig2,use_container_width=True)

# ── PRICING ───────────────────────────────────────────────────────────────────

def page_pricing():
st.markdown(’<div class="hero"><h1>💳 Simple, Transparent Pricing</h1><p>Start free. Upgrade when you're ready. No hidden fees. First lesson free on any plan.</p></div>’, unsafe_allow_html=True)
billing=st.radio(“Billing”,[“Monthly”,“Annual (Save 20%)”],horizontal=True); annual=“Annual” in billing
if annual: st.success(“🎉 You’re saving 20% with annual billing!”)
with st.expander(“🏷️ Have a promo code?”):
pc1,pc2=st.columns([2,1])
with pc1: promo=st.text_input(“Promo code”,placeholder=“e.g. SOMALI10”).upper()
with pc2:
if st.button(“Apply”,type=“primary”):
codes={“SOMALI10”:0.9,“FIRST20”:0.8,“DIASPORA”:0.85}
if promo in codes: st.session_state.promo_discount=codes[promo]; st.success(f”✅ {int((1-codes[promo])*100)}% off!”)
else: st.error(“Invalid code. Try SOMALI10 or FIRST20”)
disc=st.session_state.promo_discount; st.markdown(”—”)
cols=st.columns(4)
for col,plan in zip(cols,PLANS):
with col:
raw=plan[“pa”] if annual else plan[“pm”]
pd_str=“Custom” if raw is None else “Free” if raw==0 else f”${int(raw*disc)}/mo”
pop=plan.get(“popular”,False); border=“2px solid #0F9B58” if pop else “1px solid #E4E9F2”; bg=”#E6F9F0” if pop else “white”
fh=””.join(f’<div style="font-size:12px;color:#0B1429;margin-bottom:8px;display:flex;gap:8px"><span style="color:#0F9B58;font-weight:900">✓</span>{f}</div>’ for f in plan[“features”])
pb=’<div style="background:linear-gradient(90deg,#0F9B58,#13C46E);color:white;text-align:center;font-size:11px;font-weight:700;padding:5px;border-radius:8px 8px 0 0;margin:-1px -1px 12px">⭐ MOST POPULAR</div>’ if pop else “”
st.markdown(f’<div style="background:{bg};border:{border};border-radius:16px;padding:24px 20px;min-height:380px">{pb}<div style="font-size:32px;margin-bottom:6px">{plan[“emoji”]}</div><div style="font-weight:800;font-size:18px;color:#0B1F4A;margin-bottom:6px">{plan[“name”]}</div><div style=“font-size:2rem;font-weight:900;color:{”#0F9B58” if pop else “#0B1F4A”};margin:10px 0”>{pd_str}</div><hr style="border-color:#E4E9F2;margin:12px 0">{fh}</div>’, unsafe_allow_html=True)
ctas={“starter”:“Start Free”,“family”:“Start Free Trial”,“premium”:“Get Premium”,“school”:“Contact Sales”}
if st.button(ctas[plan[“id”]],key=f”p_{plan[‘id’]}”,use_container_width=True,type=“primary” if pop else “secondary”):
if plan[“id”]==“starter”: st.success(“✅ You’re on the Starter plan!”)
elif plan[“id”]==“school”: st.info(“📧 Email sales@somalitutor.com for school pricing”)
else: st.balloons(); st.success(f”🎉 Welcome to {plan[‘name’]} plan!”)
st.markdown(”—”)
g1,g2,g3=st.columns(3)
with g1: st.info(“🛡️ **30-day money-back guarantee**\nNot satisfied? Full refund.”)
with g2: st.info(“🔄 **Free teacher switch**\nNot happy? We’ll find a new teacher for free.”)
with g3: st.info(“❌ **Cancel anytime**\nNo contracts. Cancel in one click.”)

# ── LOGIN ─────────────────────────────────────────────────────────────────────

def page_login():
st.title(“🔐 Log In to SomaliTutor”)
c1,c2=st.columns([1,1])
with c1:
with st.form(“login_form”):
email=st.text_input(“Email”,placeholder=“parent@demo.com”)
password=st.text_input(“Password”,type=“password”,placeholder=“demo1234”)
if st.form_submit_button(“Log In →”,type=“primary”,use_container_width=True):
u=DEMO_USERS.get(email.strip().lower())
if not u: st.error(“No account found with that email.”)
elif u[“password”]!=password: st.error(“Incorrect password.”)
else:
st.session_state.user={k:v for k,v in u.items() if k!=“password”}; st.session_state.nav=“🏠  Home”
st.success(f”Welcome back, {u[‘name’]}! 👋”); st.rerun()
if st.button(“Create Account →”,use_container_width=True): st.session_state.nav=“✍️  Sign Up”; st.rerun()
with c2:
st.markdown(’<div class="nv"><h3 style="color:white;font-size:1rem;margin-bottom:12px">🎭 Demo Accounts</h3><div style="font-size:13px;color:rgba(255,255,255,.7);line-height:2.2"><div><b style="color:white">👩 Parent:</b> parent@demo.com</div><div><b style="color:white">👩‍🏫 Teacher:</b> teacher@demo.com</div><div><b style="color:white">⚙️ Admin:</b> admin@demo.com</div><div style="margin-top:6px"><b style="color:white">Password:</b> demo1234 (admin: admin1234)</div></div></div>’, unsafe_allow_html=True)

def page_signup():
st.title(“🎉 Create Your Account”)
c1,c2=st.columns([1,1])
with c1:
with st.form(“signup_form”):
role=st.radio(“I am a:”,[“Parent / Guardian”,“Teacher”],horizontal=True)
name=st.text_input(“Full name”,placeholder=“Faadumo Hassan”)
email=st.text_input(“Email address”)
password=st.text_input(“Password (min 8 chars)”,type=“password”)
confirm=st.text_input(“Confirm password”,type=“password”)
agree=st.checkbox(“I agree to the Terms of Service”)
if st.form_submit_button(“Create Account →”,type=“primary”,use_container_width=True):
if not agree: st.error(“Please agree to the terms.”)
elif password!=confirm: st.error(“Passwords do not match.”)
elif len(password)<8: st.error(“Password must be at least 8 characters.”)
elif not name or not email: st.error(“Please fill in all fields.”)
else:
st.session_state.user={“id”:“new”,“name”:name.strip(),“email”:email.lower(),“role”:“parent” if “Parent” in role else “teacher”,“children”:[],“plan”:“starter”,“avatar”:“👤”}
st.session_state.nav=“🏠  Home”; st.balloons(); st.success(f”Welcome to SomaliTutor, {name}! 🎉”); st.rerun()
with c2:
st.markdown(’<div class="sc"><h3 style="color:#0B1F4A;font-weight:800;margin-bottom:12px">Why SomaliTutor?</h3><ul style="color:#64748B;font-size:13px;line-height:2.1;padding-left:18px"><li>✅ First lesson completely free</li><li>🛡️ All teachers background-checked</li><li>🤖 AI-matched to your child's needs</li><li>📊 Real-time progress tracking</li><li>🌍 Teachers in 24+ countries</li></ul></div>’, unsafe_allow_html=True)

# ── ACCOUNT ───────────────────────────────────────────────────────────────────

def page_account():
if not rl(): return
user=gu(); st.title(f”👤 My Account — {user[‘name’]}”)
tab1,tab2,tab3=st.tabs([“Profile”,“Subscription”,“Notifications”])
with tab1:
with st.form(“pf”):
st.text_input(“Full name”,value=user[“name”]); st.text_input(“Email”,value=user[“email”])
st.text_input(“Phone”,placeholder=”+44 7700 900000”)
st.selectbox(“Country”,[“United Kingdom”,“United States”,“Canada”,“Sweden”,“UAE”,“Australia”,“Somalia”,“Other”])
st.text_area(“Bio”,placeholder=“Tell teachers about your family…”)
if st.form_submit_button(“Save Changes”,type=“primary”): st.success(“✅ Profile updated!”)
with tab2:
plan=user.get(“plan”,“starter”)
st.markdown(f’<div class="nv"><div style="font-size:13px;color:rgba(255,255,255,.6);margin-bottom:4px">Current Plan</div><div style="font-size:2rem;font-weight:900;color:white">{plan.title()} {“👨‍👩‍👧” if plan==“family” else “💎” if plan==“premium” else “🌱”}</div><div style="color:rgba(255,255,255,.6);font-size:13px;margin-top:4px">Next billing: June 1, 2025</div></div>’, unsafe_allow_html=True)
c1,c2=st.columns(2)
with c1:
if st.button(“⬆️ Upgrade Plan”,type=“primary”,use_container_width=True): st.session_state.nav=“💳  Pricing”; st.rerun()
with c2:
if st.button(“❌ Cancel Subscription”,use_container_width=True): st.warning(“Subscription will end at billing period.”)
with tab3:
with st.form(“nf”):
st.checkbox(“📧 Email: Lesson reminders”,value=True); st.checkbox(“📧 Email: Weekly summary”,value=True)
st.checkbox(“📱 WhatsApp: Reminders”,value=False); st.checkbox(“🔔 Push: Booking confirmations”,value=True)
if st.form_submit_button(“Save Preferences”,type=“primary”): st.success(“✅ Preferences saved!”)
st.divider()
if st.button(“🚪 Log Out”,use_container_width=True): st.session_state.user=None; st.session_state.nav=“🏠  Home”; st.rerun()

# ── TEACHER HUB ───────────────────────────────────────────────────────────────

def page_teacher_hub():
if not rl(): return
user=gu(); t=next((x for x in TEACHERS if x[“id”]==user.get(“teacher_id”,1)),TEACHERS[0])
st.markdown(f’<div style="display:flex;align-items:center;gap:16px;margin-bottom:24px"><span style="font-size:56px">{t[“emoji”]}</span><div><h2 style="color:#0B1F4A;margin:0;font-weight:900">{t[“name”]}</h2><p style="color:#64748B;margin:4px 0">{t[“headline”]}</p><span style="background:#FEF3DC;color:#D4920A;border-radius:20px;padding:3px 14px;font-size:12px;font-weight:700">{t[“badge”].title()} · 85% commission</span></div></div>’, unsafe_allow_html=True)
tab1,tab2,tab3,tab4=st.tabs([“📊 Overview”,“💰 Earnings”,“👥 Students”,“🛠️ Profile”])
with tab1:
k1,k2,k3,k4,k5=st.columns(5)
k1.metric(“📅 Lessons MTD”,“32”,”+8”); k2.metric(“💰 Earnings”,”$384”,”+22%”); k3.metric(“⭐ Rating”,t[“rating”]); k4.metric(“🔁 Rebooking”,f”{t[‘rebooking’]}%”); k5.metric(“✅ Completion”,f”{t[‘completion’]}%”)
st.markdown(”—”); st.subheader(“📅 Upcoming Lessons”)
for l in [{“ch”:“Ayaan”,“s”:“Somali”,“d”:“Today 4:30 PM”},{“ch”:“Lul”,“s”:“Quran”,“d”:“Sat 10:00 AM”},{“ch”:“Hashi”,“s”:“Arabic”,“d”:“Mon 5:00 PM”}]:
c1,c2,c3=st.columns([3,2,1])
with c1: st.write(f”**{l[‘ch’]}** — {l[‘s’]}”)
with c2: st.write(f”📅 {l[‘d’]}”)
with c3:
if st.button(“🎥 Join”,key=f”th_{l[‘ch’]}”,type=“primary”): st.success(“Launching…”)
with tab2:
e1,e2,e3,e4=st.columns(4)
e1.metric(“This Month”,”$384”); e2.metric(“Pending”,”$54”); e3.metric(“Withdrawable”,”$330”); e4.metric(“All Time”,”$5,760”)
with st.expander(“💸 Withdraw Earnings”):
with st.form(“wd”):
amt=st.number_input(“Amount ($)”,20,330,100); meth=st.selectbox(“Method”,[“Bank Transfer”,“PayPal”,“Wise”,“EVC Plus”,“Zaad”])
if st.form_submit_button(“Request Withdrawal”,type=“primary”): st.success(f”✅ Withdrawal of ${amt} via {meth} requested!”)
df=pd.DataFrame([{“Date”:“May 10”,“Student”:“Ayaan”,“Gross”:”$15”,“Net”:”$12.75”,“Status”:“Paid”},{“Date”:“May 10”,“Student”:“Lul”,“Gross”:”$15”,“Net”:”$12.75”,“Status”:“Paid”},{“Date”:“May 9”,“Student”:“Hashi”,“Gross”:”$15”,“Net”:”$12.75”,“Status”:“Pending”}])
st.dataframe(df,use_container_width=True,hide_index=True)
st.download_button(“📥 Export CSV”,df.to_csv(index=False),“earnings.csv”,“text/csv”)
with tab3:
for s in [{“n”:“Ayaan”,“a”:9,“s”:“Somali”,“l”:7,“p”:45},{“n”:“Lul”,“a”:7,“s”:“Quran”,“l”:4,“p”:30},{“n”:“Hashi”,“a”:12,“s”:“Arabic”,“l”:12,“p”:60}]:
with st.expander(f”👤 {s[‘n’]} (Age {s[‘a’]}) — {s[‘s’]}”):
st.write(f”**Lessons:** {s[‘l’]}”); st.progress(s[“p”]/100,text=f”{s[‘p’]}% progress”)
with st.form(f”tn_{s[‘n’]}”):
st.text_area(“Lesson note”,height=70,placeholder=“Today we covered…”)
if st.form_submit_button(“Save Note”): st.success(“Note saved!”)
with tab4:
with st.form(“thp”):
st.text_input(“Display name”,value=t[“name”]); st.text_input(“Headline”,value=t[“headline”])
st.number_input(“Hourly rate ($)”,5,50,t[“price”]); st.text_area(“Bio”,value=t[“bio”],height=100)
st.multiselect(“Subjects”,[“Quran”,“Somali”,“Arabic”,“Math”,“English”,“Islamic Studies”],default=t[“subjects”])
st.checkbox(“Offer free trial lessons”,value=True)
if st.form_submit_button(“Save Profile”,type=“primary”): st.success(“✅ Profile updated!”)

# ── ADMIN ─────────────────────────────────────────────────────────────────────

def page_admin():
if not rl(): return
user=gu()
if user.get(“role”)!=“admin”: st.error(“🔒 Admin access only. Log in as admin@demo.com”); return
st.markdown(’<div style="display:flex;align-items:center;gap:12px;margin-bottom:20px"><span style="background:#DC2626;color:white;border-radius:8px;padding:6px 14px;font-weight:700;font-size:13px">⚙️ ADMIN</span><h2 style="color:#0B1F4A;margin:0;font-weight:900">Control Center</h2></div>’, unsafe_allow_html=True)
tab1,tab2,tab3,tab4,tab5=st.tabs([“📊 KPIs”,“👥 Users”,“🔎 Moderation”,“💰 Finance”,“📈 Analytics”])
with tab1:
k1,k2,k3,k4,k5=st.columns(5)
k1.metric(“👨‍👩‍👧 Families”,“2,041”,”+47”); k2.metric(“🎓 Teachers”,“148”,”+3”); k3.metric(“📅 Bookings Today”,“312”,”+18%”); k4.metric(“💰 Revenue MTD”,”$24,810”,”+22%”); k5.metric(“⭐ Avg Rating”,“4.91”,”+0.01”)
st.markdown(”—”); st.subheader(“🔔 Alerts”)
for ic,lv,msg in [(“🚨”,“High”,“3 teachers not responded >6 hours”),(“⚠️”,“Med”,“Payment failure rate 2.3%”),(“ℹ️”,“Low”,“5 new teacher applications pending”)]:
c1,c2=st.columns([8,1]); bg={“High”:”#FEE2E2”,“Med”:”#FEF3DC”,“Low”:”#E6F9F0”}[lv]
with c1: st.markdown(f’<div style="background:{bg};border-radius:10px;padding:10px 14px;margin-bottom:8px;font-size:13px">{ic} <b>{lv}:</b> {msg}</div>’, unsafe_allow_html=True)
with c2: st.button(“Dismiss”,key=f”al_{msg[:10]}”)
with tab2:
st.dataframe(pd.DataFrame([{“Name”:t[“name”],“Badge”:t[“badge”].title(),“Rating”:t[“rating”],“Lessons”:t[“lessons”],“Status”:“Active”} for t in TEACHERS]),use_container_width=True,hide_index=True)
c1,c2=st.columns(2)
with c1: sus=st.selectbox(“Suspend teacher”,[t[“name”] for t in TEACHERS])
with c2:
if st.button(“⚠️ Suspend”,type=“primary”): st.warning(f”⚠️ {sus} suspended.”)
st.subheader(“📋 New Applications”)
for app in [{“n”:“Yasmin Abdi”,“s”:“Quran, Arabic”,“f”:“Netherlands”},{“n”:“Omar Salah”,“s”:“Somali, History”,“f”:“USA”}]:
with st.expander(f”📄 {app[‘n’]} — {app[‘s’]} — {app[‘f’]}”):
a1,a2,a3=st.columns(3)
with a1:
if st.button(“✅ Approve”,key=f”ap_{app[‘n’]}”,type=“primary”): st.success(“Approved!”)
with a2:
if st.button(“📞 Interview”,key=f”in_{app[‘n’]}”): st.info(“Scheduled.”)
with a3:
if st.button(“❌ Reject”,key=f”re_{app[‘n’]}”): st.error(“Rejected.”)
with tab3:
sf=st.radio(“Filter”,[“All”,“Open”,“Resolved”],horizontal=True)
disputes=[{“id”:“D-001”,“f”:“A. Osman”,“t”:“K. Hassan”,“amt”:”$15”,“r”:“Teacher was 20 min late”,“u”:“High”,“s”:“Open”},{“id”:“D-002”,“f”:“H. Ahmed”,“t”:“A. Farah”,“amt”:”$12”,“r”:“Lesson quality issue”,“u”:“Med”,“s”:“Open”},{“id”:“D-003”,“f”:“M. Warsame”,“t”:“H. Warsame”,“amt”:”$18”,“r”:“Technical difficulties”,“u”:“Low”,“s”:“Resolved”}]
for d in [x for x in disputes if sf==“All” or x[“s”]==sf]:
bg={“High”:”#FEE2E2”,“Med”:”#FEF3DC”,“Low”:”#DBEAFE”}[d[“u”]]
with st.expander(f”{d[‘id’]} — {d[‘f’]} vs {d[‘t’]} — {d[‘s’]}”):
st.markdown(f’<div style="background:{bg};border-radius:8px;padding:10px;font-size:13px;margin-bottom:8px">{d[“r”]}</div>’, unsafe_allow_html=True)
d1,d2,d3=st.columns(3)
with d1:
if st.button(f”💸 Refund”,key=f”rf_{d[‘id’]}”): st.success(“Refund issued!”)
with d2:
if st.button(“💬 Chat”,key=f”ch_{d[‘id’]}”): st.info(“Loading chat log…”)
with d3:
if st.button(“✅ Resolve”,key=f”rs_{d[‘id’]}”): st.success(“Resolved.”)
with tab4:
f1,f2,f3,f4=st.columns(4)
f1.metric(“💰 Gross”,”$24,810”,”+22%”); f2.metric(“📊 Commission”,”$4,962”); f3.metric(“💸 Payouts”,”$19,848”); f4.metric(“📈 Net”,”$4,962”)
df=pd.DataFrame([{“Date”:“May 10”,“Family”:“A. Osman”,“Teacher”:“K. Hassan”,“Gross”:”$15”,“Net”:”$12.00”,“Status”:“Paid”},{“Date”:“May 9”,“Family”:“M. Hassan”,“Teacher”:“H. Warsame”,“Gross”:”$18”,“Net”:”$15.30”,“Status”:“Pending”}])
st.dataframe(df,use_container_width=True,hide_index=True)
st.download_button(“📥 Export CSV”,df.to_csv(index=False),“transactions.csv”,“text/csv”)
with tab5:
c1,c2=st.columns(2)
with c1:
fig=px.pie(pd.DataFrame({“Subject”:[“Quran”,“Somali”,“Arabic”,“Math”,“English”],“Bookings”:[412,287,198,145,89]}),names=“Subject”,values=“Bookings”,title=“Bookings by Subject”,color_discrete_sequence=[”#0F9B58”,”#0B1F4A”,”#D4920A”,”#6D28D9”,”#0891B2”])
st.plotly_chart(fig,use_container_width=True)
with c2:
fig2=px.bar(pd.DataFrame({“Country”:[“UK”,“USA”,“Canada”,“Sweden”,“UAE”,“Australia”],“Families”:[520,480,310,220,190,155]}),x=“Families”,y=“Country”,orientation=“h”,title=“Top Countries”,color_discrete_sequence=[”#0B1F4A”])
fig2.update_layout(plot_bgcolor=“white”,paper_bgcolor=“white”); st.plotly_chart(fig2,use_container_width=True)
lb=pd.DataFrame([{“Rank”:i+1,“Teacher”:t[“name”],“Lessons”:t[“lessons”],“Rating”:t[“rating”],“Revenue”:f”${t[‘lessons’]*t[‘price’]:,}”} for i,t in enumerate(sorted(TEACHERS,key=lambda x:-x[“lessons”])[:5])])
st.dataframe(lb,use_container_width=True,hide_index=True)

# ── ROUTER ────────────────────────────────────────────────────────────────────

n=st.session_state.nav
if   “Home”        in n: page_home()
elif “Find”        in n: page_find()
elif “AI Matching” in n: page_ai()
elif “Bookings”    in n: page_bookings()
elif “Progress”    in n: page_progress()
elif “Pricing”     in n: page_pricing()
elif “Login”       in n: page_login()
elif “Sign Up”     in n: page_signup()
elif “Account”     in n: page_account()
elif “Teacher Hub” in n: page_teacher_hub()
elif “Admin”       in n: page_admin()
