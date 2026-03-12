“”“SomaliTutor — Dashboard matching reference design”””
import streamlit as st
import pandas as pd
import plotly.express as px
import time, datetime, random

st.set_page_config(page_title=“SomaliTutor”,page_icon=“🛡️”,layout=“wide”,initial_sidebar_state=“expanded”)

st.markdown(”””

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
html,body,[data-testid="stAppViewContainer"],[data-testid="stHeader"],.main{background:#F4F6F9!important;font-family:'Inter',sans-serif!important;}
*{font-family:'Inter',sans-serif!important;box-sizing:border-box;}
#MainMenu,footer,.stDeployButton,[data-testid="stToolbar"]{display:none!important;}
.main .block-container{padding:0!important;max-width:100%!important;}
[data-testid="stSidebar"]{background:#FFFFFF!important;border-right:1px solid #E5E7EB!important;}
[data-testid="stSidebar"] *{color:inherit!important;}
[data-testid="stSidebar"] .stRadio>div{gap:2px!important;padding:0 12px!important;}
[data-testid="stSidebar"] .stRadio label{font-size:14px!important;font-weight:500!important;color:#6B7280!important;background:transparent!important;border-radius:10px!important;padding:10px 14px!important;margin:1px 0!important;white-space:nowrap!important;width:100%!important;}
[data-testid="stSidebar"] .stRadio label:hover{background:#EFF6FF!important;color:#1D4ED8!important;}
[data-testid="stSidebar"] [data-baseweb="radio"]>div:first-child{display:none!important;}
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p{color:#9CA3AF!important;font-size:11px!important;}
.stButton>button{font-family:'Inter',sans-serif!important;font-weight:600!important;font-size:14px!important;border-radius:10px!important;padding:10px 20px!important;transition:all .2s!important;border:1.5px solid #D1D5DB!important;color:#374151!important;background:#FFFFFF!important;}
.stButton>button[kind="primary"]{background:#1E3A6E!important;border:none!important;color:#FFFFFF!important;box-shadow:0 2px 8px rgba(30,58,110,.3)!important;}
.stButton>button[kind="primary"]:hover{background:#162d57!important;transform:translateY(-1px)!important;color:#FFFFFF!important;}
.stButton>button[kind="primary"] p,.stButton>button[kind="primary"] *{color:#FFFFFF!important;}
.stButton>button:hover{border-color:#1E3A6E!important;color:#1E3A6E!important;}
[data-testid="stMetric"]{background:#FFFFFF!important;border:1px solid #E5E7EB!important;border-radius:14px!important;padding:18px 20px!important;box-shadow:0 1px 6px rgba(0,0,0,.06)!important;}
[data-testid="stMetricLabel"] p{font-size:11px!important;font-weight:700!important;color:#6B7280!important;text-transform:uppercase!important;letter-spacing:.05em!important;}
[data-testid="stMetricValue"] div{font-size:1.9rem!important;font-weight:800!important;color:#111827!important;}
.stTabs [data-baseweb="tab-list"]{background:#F9FAFB!important;border-radius:10px!important;padding:4px!important;gap:4px!important;border:1px solid #E5E7EB!important;}
.stTabs [data-baseweb="tab"]{border-radius:7px!important;font-weight:600!important;font-size:13px!important;color:#6B7280!important;padding:8px 16px!important;background:transparent!important;border:none!important;}
.stTabs [data-baseweb="tab"] *{color:inherit!important;}
.stTabs [aria-selected="true"]{background:#FFFFFF!important;color:#1E3A6E!important;box-shadow:0 1px 6px rgba(0,0,0,.08)!important;}
.stTabs [aria-selected="true"] *{color:#1E3A6E!important;}
.stTextInput>div>div>input,.stTextArea textarea,.stNumberInput input{border-radius:10px!important;border:1.5px solid #D1D5DB!important;font-size:14px!important;color:#111827!important;background:#FFFFFF!important;padding:10px 14px!important;}
.stSelectbox>div>div{border-radius:10px!important;border:1.5px solid #D1D5DB!important;background:#FFFFFF!important;}
label{font-weight:600!important;font-size:13px!important;color:#374151!important;}
[data-testid="stAlert"]{border-radius:10px!important;}
.stSuccess>div{background:#F0FDF4!important;color:#166534!important;border:1px solid #86EFAC!important;border-radius:10px!important;}
.stInfo>div{background:#EFF6FF!important;color:#1E40AF!important;border:1px solid #93C5FD!important;border-radius:10px!important;}
.stWarning>div{background:#FFFBEB!important;color:#92400E!important;border:1px solid #FCD34D!important;border-radius:10px!important;}
.stError>div{background:#FEF2F2!important;color:#991B1B!important;border:1px solid #FCA5A5!important;border-radius:10px!important;}
details{background:#FFFFFF!important;border:1px solid #E5E7EB!important;border-radius:12px!important;margin-bottom:8px!important;}
summary{font-weight:600!important;font-size:14px!important;color:#111827!important;padding:14px 16px!important;}
.stProgress>div>div>div{background:linear-gradient(90deg,#1E3A6E,#16A34A)!important;border-radius:99px!important;}
.stProgress>div>div{background:#E5E7EB!important;border-radius:99px!important;}
h1{font-size:2rem!important;font-weight:800!important;color:#111827!important;}
h2{font-size:1.35rem!important;font-weight:700!important;color:#111827!important;}
h3{font-size:1.1rem!important;font-weight:700!important;color:#111827!important;}
p{color:#374151!important;line-height:1.65!important;font-size:14px!important;}
hr{border:none!important;border-top:1px solid #E5E7EB!important;margin:20px 0!important;}
.stCheckbox label{font-size:14px!important;color:#374151!important;font-weight:500!important;}
.stRadio label{font-size:14px!important;color:#374151!important;}
[data-testid="stDataFrame"]{border-radius:12px!important;border:1px solid #E5E7EB!important;overflow:hidden!important;}
/* Custom cards */
.card{background:#FFFFFF;border:1px solid #E5E7EB;border-radius:16px;padding:22px;box-shadow:0 1px 6px rgba(0,0,0,.05);margin-bottom:16px;}
.trow{background:#FFFFFF;border:1px solid #E5E7EB;border-radius:14px;padding:16px 20px;margin-bottom:10px;display:flex;align-items:center;gap:16px;box-shadow:0 1px 4px rgba(0,0,0,.05);}
.av{width:56px;height:56px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:30px;flex-shrink:0;}
.topbar{background:#FFFFFF;border-bottom:1px solid #E5E7EB;padding:14px 28px;display:flex;align-items:center;justify-content:space-between;margin-bottom:24px;}
.searchbar{background:#F9FAFB;border:1.5px solid #E5E7EB;border-radius:10px;padding:9px 16px;font-size:14px;color:#6B7280;display:flex;align-items:center;gap:10px;min-width:280px;}
.topicon{width:36px;height:36px;border-radius:50%;background:#F3F4F6;display:flex;align-items:center;justify-content:center;font-size:16px;}
.bkcard{background:#FFFFFF;border:1px solid #E5E7EB;border-radius:16px;padding:22px;box-shadow:0 1px 6px rgba(0,0,0,.06);}
.payrow{background:#FFFFFF;border:1.5px solid #E5E7EB;border-radius:10px;padding:13px 16px;margin-bottom:8px;display:flex;align-items:center;gap:12px;}
.livecard{background:linear-gradient(145deg,#0F1F4A,#1E3A6E);border-radius:16px;overflow:hidden;position:relative;}
.sbitem{background:#F9FAFB;border:1px solid #E5E7EB;border-radius:12px;padding:12px;margin-bottom:8px;display:flex;align-items:center;gap:10px;}
.chip{background:#F3F4F6;border:1px solid #E5E7EB;border-radius:8px;padding:5px 14px;font-size:13px;font-weight:500;color:#374151;display:inline-block;margin-right:6px;}
.welcome{background:#FFFFFF;border:1px solid #E5E7EB;border-radius:16px;padding:22px 26px;margin-bottom:18px;box-shadow:0 1px 6px rgba(0,0,0,.05);}
</style>

“””,unsafe_allow_html=True)

TEACHERS=[
{“id”:1,“name”:“Teacher Khadra”,“emoji”:“👩🏽‍🏫”,“abg”:”#DBEAFE”,“headline”:“Quran & Somali Expert”,“subjects”:[“Quran”,“Somali”,“Arabic”],“rating”:4.9,“reviews”:127,“lessons”:380,“price”:15,“verify_level”:5,“online”:True,“badge”:“Diamond”,“rebooking”:92,“completion”:99,“response_time”:”<30 min”,“bio”:“Hafidha with Ijaazah. 10+ years teaching diaspora children Quran with beautiful Tajweed.”,“gender”:“female”,“next_slot”:“Today 4:30 PM”},
{“id”:2,“name”:“Teacher Ahmed”,“emoji”:“👨🏽‍🏫”,“abg”:”#D1FAE5”,“headline”:“Somali & English Tutor”,“subjects”:[“Somali”,“English”,“Math”],“rating”:4.8,“reviews”:89,“lessons”:215,“price”:12,“verify_level”:4,“online”:False,“badge”:“Gold”,“rebooking”:78,“completion”:97,“response_time”:”<1 hr”,“bio”:“8 years experience. Fun structured lessons for diaspora kids aged 7-14.”,“gender”:“male”,“next_slot”:“Tomorrow 10 AM”},
{“id”:3,“name”:“Teacher Hodan”,“emoji”:“👩🏾‍🏫”,“abg”:”#FCE7F3”,“headline”:“Quran Memorisation Specialist”,“subjects”:[“Quran”,“Arabic”,“Islamic Studies”],“rating”:4.9,“reviews”:204,“lessons”:501,“price”:18,“verify_level”:5,“online”:True,“badge”:“Diamond”,“rebooking”:95,“completion”:99,“response_time”:”<30 min”,“bio”:“Hafidha helping 50+ children complete their full Quran journey.”,“gender”:“female”,“next_slot”:“Today 6 PM”},
{“id”:4,“name”:“Teacher Abdi”,“emoji”:“👨🏾‍🎓”,“abg”:”#FEF3C7”,“headline”:“Math & Somali for Teens”,“subjects”:[“Math”,“Somali”],“rating”:4.6,“reviews”:34,“lessons”:48,“price”:10,“verify_level”:3,“online”:True,“badge”:“Rising”,“rebooking”:65,“completion”:94,“response_time”:”<3 hr”,“bio”:“Education student. Energetic and relatable for teens.”,“gender”:“male”,“next_slot”:“Fri 3 PM”},
{“id”:5,“name”:“Teacher Safia”,“emoji”:“👩🏽‍💼”,“abg”:”#EDE9FE”,“headline”:“Arabic & Islamic Studies”,“subjects”:[“Arabic”,“Quran”,“Islamic Studies”],“rating”:4.7,“reviews”:67,“lessons”:142,“price”:14,“verify_level”:4,“online”:False,“badge”:“Trusted”,“rebooking”:80,“completion”:96,“response_time”:”<1 hr”,“bio”:“Classical Arabic teacher trained in Cairo.”,“gender”:“female”,“next_slot”:“Sat 11 AM”},
{“id”:6,“name”:“Teacher Faarax”,“emoji”:“👨🏾‍🏫”,“abg”:”#FFE4E6”,“headline”:“Somali Culture & Language”,“subjects”:[“Somali”,“History”],“rating”:4.5,“reviews”:22,“lessons”:31,“price”:8,“verify_level”:2,“online”:False,“badge”:“New”,“rebooking”:55,“completion”:90,“response_time”:”<6 hr”,“bio”:“Native speaker sharing Somali heritage through oral storytelling.”,“gender”:“male”,“next_slot”:“Mon 5 PM”},
]
PLANS=[
{“id”:“starter”,“name”:“Starter”,“emoji”:“🌱”,“pm”:0,“pa”:0,“popular”:False,“features”:[“1 free trial lesson”,“Browse all tutors”,“Basic progress tracking”,“Email support”]},
{“id”:“family”,“name”:“Family”,“emoji”:“👨‍👩‍👧”,“pm”:49,“pa”:39,“popular”:True,“features”:[“Up to 3 children”,“8 lessons/month”,“AI teacher matching”,“Recordings 30 days”,“Priority booking”,“Cancel anytime”]},
{“id”:“premium”,“name”:“Premium”,“emoji”:“💎”,“pm”:89,“pa”:71,“popular”:False,“features”:[“Unlimited children”,“Unlimited lessons”,“AI matching + scheduling”,“Recordings forever”,“Weekly parent call”,“Dedicated account manager”,“24/7 support”]},
{“id”:“school”,“name”:“School”,“emoji”:“🏫”,“pm”:None,“pa”:None,“popular”:False,“features”:[“Bulk student accounts”,“Admin dashboard”,“Custom reporting”,“API access”,“Invoice billing”,“SLA guarantee”]},
]
AI_QS=[
{“id”:“age”,“q”:“How old is your child?”,“opts”:[“3-6 years”,“7-10 years”,“11-14 years”,“15+ years”]},
{“id”:“subject”,“q”:“What subject are you looking for?”,“opts”:[“Quran & Tajweed”,“Somali Language”,“Arabic”,“Math”,“Multiple subjects”]},
{“id”:“level”,“q”:“What is your child current level?”,“opts”:[“Complete beginner”,“Some exposure”,“Intermediate”,“Advanced”]},
{“id”:“style”,“q”:“How does your child learn best?”,“opts”:[“Visual (pictures, videos)”,“Auditory (listening, repetition)”,“Reading & writing”,“Hands-on activities”]},
{“id”:“gender”,“q”:“Do you prefer a specific teacher gender?”,“opts”:[“Female teacher”,“Male teacher”,“No preference”]},
{“id”:“budget”,“q”:“What is your budget per lesson?”,“opts”:[“Under $10”,”$10-$15”,”$15-$20”,”$20+”]},
]
DEMO_USERS={
“parent@demo.com”:{“id”:“u1”,“name”:“Faadumo Hassan”,“email”:“parent@demo.com”,“role”:“parent”,“password”:“demo1234”,“children”:[{“name”:“Ayaan”,“age”:9,“goal”:“Quran”,“streak”:5,“lessons”:7},{“name”:“Lul”,“age”:7,“goal”:“Somali”,“streak”:3,“lessons”:4}],“plan”:“family”,“avatar”:“👩🏽”},
“teacher@demo.com”:{“id”:“u2”,“name”:“Khadra Hassan”,“email”:“teacher@demo.com”,“role”:“teacher”,“password”:“demo1234”,“teacher_id”:1,“plan”:None,“avatar”:“👩🏽‍🏫”},
“admin@demo.com”:{“id”:“u3”,“name”:“Admin User”,“email”:“admin@demo.com”,“role”:“admin”,“password”:“admin1234”,“plan”:None,“avatar”:“⚙️”},
}
for k,v in {“user”:None,“nav”:“🏠 Dashboard”,“ai_step”:0,“ai_answers”:{},“ai_matches”:[],“wishlist”:[],“promo_discount”:1.0,“bt”:TEACHERS[0]}.items():
if k not in st.session_state: st.session_state[k]=v

def gu(): return st.session_state.get(“user”)
def rl():
if gu(): return True
st.markdown(’<div class="card" style="text-align:center;padding:40px"><div style="font-size:48px">🔐</div><h2>Please log in</h2><p style="color:#6B7280">You need an account to access this page</p></div>’,unsafe_allow_html=True)
c1,c2,_=st.columns([1,1,3])
with c1:
if st.button(“Log In”,type=“primary”): st.session_state.nav=“🔐 Login”; st.rerun()
with c2:
if st.button(“Sign Up”): st.session_state.nav=“✍️ Sign Up”; st.rerun()
return False
def ms(t,ans):
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
elif “$10” in b and t[“price”]<=15: s+=8
elif “$15” in b and t[“price”]<=20: s+=5
s+=(t[“rating”]-4.0)*5+t[“rebooking”]*0.05+random.uniform(-3,3)
return min(99,max(50,int(s)))

# SIDEBAR

with st.sidebar:
st.markdown(”””<div style='display:flex;align-items:center;gap:12px;padding:20px 20px 16px;border-bottom:1px solid #E5E7EB;'>
<div style='background:#1E3A6E;border-radius:10px;width:38px;height:38px;display:flex;align-items:center;justify-content:center;font-size:20px;'>🛡️</div>
<div><div style='font-size:16px;font-weight:800;color:#111827;'>SomaliTutor</div>
<div style='font-size:10px;color:#9CA3AF;font-weight:500;'>Verified Teachers</div></div></div>”””,unsafe_allow_html=True)
st.markdown(”<div style='height:10px'></div>”,unsafe_allow_html=True)
NAVS=[“🏠 Dashboard”,“🔍 Find Tutors”,“📅 My Lessons”,“💬 Messages”,“💳 Payments”,“📊 Progress”,“💎 Pricing”,“🔐 Login”,“✍️ Sign Up”,“👤 My Account”,“🎓 Teacher Hub”,“⚙️ Admin”]
idx=NAVS.index(st.session_state.nav) if st.session_state.nav in NAVS else 0
nav=st.radio(””,NAVS,index=idx,label_visibility=“collapsed”)
st.session_state.nav=nav
st.divider()
user=gu()
if user:
st.markdown(”<div style='padding:0 12px;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:#9CA3AF;margin-bottom:8px;'>Upcoming Lessons</div>”,unsafe_allow_html=True)
for t in TEACHERS[:2]:
st.markdown(f”””<div class="sbitem"><div style="font-size:26px;">{t[‘emoji’]}</div>
<div style="flex:1;min-width:0;"><div style="font-size:13px;font-weight:700;color:#111827;">{t[‘name’]}</div>
<div style="font-size:11px;color:#6B7280;">★{t[‘rating’]} · {t[‘subjects’][0]} · ${t[‘price’]}/hr</div></div></div>”””,unsafe_allow_html=True)
if st.button(“🎥 Join Now”,type=“primary”,use_container_width=True): st.success(“Launching lesson room…”)
st.divider()
st.markdown(f”””<div style='display:flex;align-items:center;gap:10px;padding:8px 12px;'><div style='font-size:26px;'>{user[‘avatar’]}</div>
<div><div style='font-size:13px;font-weight:700;color:#111827;'>{user[‘name’]}</div>
<div style='font-size:11px;color:#6B7280;'>{user[‘role’].title()}</div></div></div>”””,unsafe_allow_html=True)
if st.button(“🚪 Log Out”,use_container_width=True): st.session_state.user=None; st.session_state.nav=“🏠 Dashboard”; st.rerun()
else:
c1,c2=st.columns(2)
with c1:
if st.button(“Log In”,use_container_width=True): st.session_state.nav=“🔐 Login”; st.rerun()
with c2:
if st.button(“Sign Up”,type=“primary”,use_container_width=True): st.session_state.nav=“✍️ Sign Up”; st.rerun()
st.markdown(”<div style='padding:12px;font-size:12px;color:#9CA3AF;'>📞 support@somalitutor.com</div>”,unsafe_allow_html=True)

def page_home():
user=gu(); name=user[“name”] if user else “Guest”; child=user[“children”][0][“name”] if user and user.get(“children”) else “Ayaan”
st.markdown(f”””<div class="topbar">
<div class="searchbar">🔍   Search Tutors…</div>
<div style="display:flex;align-items:center;gap:12px;">
<div class="topicon">🔍</div><div class="topicon">✉️</div><div class="topicon">🔔</div>
<div style="background:#1E3A6E;color:white;border-radius:50%;width:36px;height:36px;display:flex;align-items:center;justify-content:center;font-size:16px;">{user[‘avatar’] if user else ‘👤’}</div>
</div></div>”””,unsafe_allow_html=True)
col_main,col_right=st.columns([1.5,1],gap=“medium”)
with col_main:
st.markdown(f”””<div class="welcome">
<div style="font-size:1.4rem;font-weight:800;color:#111827;margin-bottom:4px;">Welcome back, {child}! 👋</div>
<div style="color:#6B7280;font-size:14px;">You have 2 upcoming lessons this week. Keep up the great work!</div></div>”””,unsafe_allow_html=True)
st.markdown(”””<div style="background:#FFFFFF;border:1.5px solid #E5E7EB;border-radius:12px;padding:10px 16px;display:flex;align-items:center;gap:12px;margin-bottom:16px;box-shadow:0 1px 4px rgba(0,0,0,.04);">
<span style="color:#9CA3AF;">🔍</span>
<span style="color:#9CA3AF;font-size:14px;flex:1;">Search tutors…</span>
<span class="chip">Availability ▾</span><span class="chip">Price ▾</span>
</div>”””,unsafe_allow_html=True)
st.markdown(”””<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
<span style="font-size:15px;font-weight:700;color:#111827;">Featured Tutors</span>
<span style="font-size:13px;font-weight:600;color:#1D4ED8;cursor:pointer;">View all →</span></div>”””,unsafe_allow_html=True)
for t in TEACHERS[:3]:
ol=’<span style="background:#10B981;color:white;border-radius:99px;padding:2px 8px;font-size:11px;font-weight:700;margin-left:6px;">● Online</span>’ if t[“online”] else “”
st.markdown(f”””<div class="trow">
<div class="av" style="background:{t['abg']};">{t[‘emoji’]}</div>
<div style="flex:1;min-width:0;">
<div style="font-size:15px;font-weight:700;color:#111827;">{t[‘name’]}{ol}</div>
<div style="color:#F59E0B;font-size:13px;">{“★”*int(t[‘rating’])}{“☆”*(5-int(t[‘rating’]))} <span style="color:#6B7280;font-size:12px;">{t[‘rating’]} · {t[‘subjects’][0]}</span></div>
<div style="font-size:12px;color:#6B7280;">${t[‘price’]}/hr · 🎓 {t[‘subjects’][1] if len(t[‘subjects’])>1 else t[‘subjects’][0]}</div>
</div>
<div style="text-align:right;flex-shrink:0;">
<div style="font-size:15px;font-weight:800;color:#F59E0B;">★ ${t[‘price’]}/hr</div>
<div style="font-size:11px;color:#9CA3AF;">{t[‘next_slot’]}</div>
</div>
<span style="font-size:18px;color:#D1D5DB;margin-left:8px;">›</span></div>”””,unsafe_allow_html=True)
c1,c2=st.columns(2)
with c1:
if st.button(“📅 Book a Lesson”,type=“primary”,use_container_width=True): st.session_state.nav=“📅 My Lessons”; st.rerun()
with c2:
if st.button(“🎁 Free Trial Lesson →”,use_container_width=True): st.session_state.nav=“🔍 Find Tutors”; st.rerun()
st.markdown(”<div style='height:16px'></div>”,unsafe_allow_html=True)
st.markdown(’<div style="font-size:15px;font-weight:700;color:#111827;margin-bottom:12px;">Upcoming Lesson</div>’,unsafe_allow_html=True)
st.markdown(f”””<div style="background:#F8FAFF;border:1px solid #DBEAFE;border-radius:12px;padding:16px;display:flex;align-items:flex-start;gap:14px;">
<div style="font-size:38px;">{TEACHERS[0][‘emoji’]}</div>
<div><div style="font-size:15px;font-weight:700;color:#111827;">{TEACHERS[0][‘name’]}</div>
<div style="font-size:13px;color:#4B5563;margin-top:4px;line-height:1.6;">
“Great teacher. My {child.lower()} loves her classes. She explains everything so clearly and sessions are always engaging.”</div>
<div style="color:#F59E0B;margin-top:8px;font-size:15px;">★★★★★</div></div></div>”””,unsafe_allow_html=True)
with col_right:
bt=st.session_state.bt
st.markdown(f”””<div class="bkcard">
<div style="font-size:16px;font-weight:700;color:#111827;margin-bottom:16px;">Book Your Lesson</div>
<div style="font-size:13px;color:#6B7280;margin-bottom:14px;"><b style="color:#111827;">Book with</b> {bt[‘name’]}</div>
<div style="font-size:12px;color:#6B7280;margin-bottom:6px;">Friday, May 12</div>
<div style="background:#FFFFFF;border:1.5px solid #D1D5DB;border-radius:10px;padding:12px 16px;display:flex;justify-content:space-between;margin-bottom:18px;">
<span style="font-size:14px;font-weight:700;color:#111827;">4:30 PM – 5:00 PM</span>
<span style="color:#9CA3AF;">▾</span>
</div>
<div style="font-size:13px;font-weight:700;color:#374151;margin-bottom:10px;">Payment Method</div>
<div class="payrow"><span style="font-size:18px;">💳</span><span style="font-size:14px;font-weight:500;color:#111827;">Credit / Debit Card</span><span style="margin-left:auto;color:#9CA3AF;">›</span></div>
<div class="payrow"><span style="font-size:18px;">🅿️</span><span style="font-size:14px;font-weight:500;color:#111827;">PayPal</span><span style="margin-left:auto;color:#9CA3AF;">›</span></div>
<div class="payrow"><span style="font-size:18px;">📱</span><span style="font-size:14px;font-weight:500;color:#111827;">Mobile Money</span><span style="margin-left:auto;color:#9CA3AF;">›</span></div>
</div>”””,unsafe_allow_html=True)
if st.button(f”✅ Confirm & Pay ${bt[‘price’]}”,type=“primary”,use_container_width=True): st.balloons(); st.success(f”Booking confirmed with {bt[‘name’]}!”)
st.markdown(”<div style='height:14px'></div>”,unsafe_allow_html=True)
st.markdown(f”””<div class="livecard">
<div style="display:flex;justify-content:space-between;align-items:center;padding:16px 18px 0;">
<div style="color:white;font-size:15px;font-weight:700;">Live Lesson</div>
<div style="background:#EF4444;color:white;border-radius:99px;padding:3px 12px;font-size:11px;font-weight:700;">● LIVE</div>
</div>
<div style="margin:12px;background:rgba(0,0,0,.2);border-radius:12px;padding:28px 16px;text-align:center;">
<div style="font-size:36px;margin-bottom:10px;">👩🏽‍🏫    👦🏽</div>
<div style="background:white;border-radius:8px;padding:10px;font-size:24px;font-weight:700;color:#1E3A6E;letter-spacing:6px;">ب   ث</div>
</div>
<div style="display:flex;gap:8px;padding:0 14px 14px;flex-wrap:wrap;">
<div style="background:rgba(255,255,255,.15);border:1px solid rgba(255,255,255,.2);border-radius:8px;padding:7px 12px;color:white;font-size:12px;font-weight:600;flex:1;text-align:center;">🎙️ Mute</div>
<div style="background:rgba(255,255,255,.15);border:1px solid rgba(255,255,255,.2);border-radius:8px;padding:7px 12px;color:white;font-size:12px;font-weight:600;flex:1;text-align:center;">📹 Video</div>
<div style="background:#EF4444;border-radius:8px;padding:7px 12px;color:white;font-size:12px;font-weight:700;flex:1;text-align:center;">End</div>
</div></div>”””,unsafe_allow_html=True)
st.markdown(”<div style='height:12px'></div>”,unsafe_allow_html=True)
s1,s2,s3=st.columns(3)
s1.metric(“📚 Lessons”,“11”,”+2”); s2.metric(“🔥 Streak”,“5 days”,”+1”); s3.metric(“⭐ Rating”,“4.9”,“↑”)

def page_find():
st.markdown(”<div style='padding:24px 28px 0'><h2 style='margin:0 0 4px'>🔍 Find a Tutor</h2><p style='color:#6B7280;margin:0 0 20px'>Browse verified teachers and book your perfect match</p></div>”,unsafe_allow_html=True)
with st.expander(“🎛️ Filter Teachers”,expanded=True):
c1,c2,c3,c4=st.columns(4)
with c1: subj=st.selectbox(“Subject”,[“All”,“Quran”,“Somali”,“Arabic”,“Math”,“English”,“Islamic Studies”])
with c2: maxp=st.slider(“Max price/hr ($)”,5,50,50)
with c3: minr=st.select_slider(“Min rating”,[0.0,4.0,4.5,4.8,4.9],0.0,format_func=lambda x:“Any” if x==0 else f”★{x}+”)
with c4: gend=st.selectbox(“Gender”,[“Any”,“Female”,“Male”])
c5,c6=st.columns(2);
with c5: only_on=st.checkbox(“Online now only”)
with c6: sortby=st.selectbox(“Sort by”,[“Top Rated”,“Price: Low to High”,“Most Lessons”])
ts=[t for t in TEACHERS if(subj==“All” or subj in t[“subjects”]) and t[“price”]<=maxp and t[“rating”]>=(minr or 0) and(gend==“Any” or t[“gender”]==gend.lower()) and(not only_on or t[“online”])]
ts=sorted(ts,key={“Top Rated”:lambda x:-x[“rating”],“Price: Low to High”:lambda x:x[“price”],“Most Lessons”:lambda x:-x[“lessons”]}[sortby])
st.markdown(f”<div style='margin-bottom:12px;font-size:14px;color:#6B7280;font-weight:600;'>{len(ts)} teachers found</div>”,unsafe_allow_html=True)
if not ts: st.info(“No teachers match. Try widening your filters.”); return
for t in ts:
ol=’<span style="background:#10B981;color:white;border-radius:99px;padding:2px 8px;font-size:11px;font-weight:700;margin-left:8px;">● Online</span>’ if t[“online”] else “”
stags=””.join(f’<span style="background:#EFF6FF;color:#1D4ED8;border-radius:6px;padding:2px 10px;font-size:11px;font-weight:600;margin-right:6px;">{s}</span>’ for s in t[“subjects”])
st.markdown(f”””<div class="trow" style="padding:18px 22px;">
<div class="av" style="background:{t['abg']};width:62px;height:62px;font-size:32px;">{t[‘emoji’]}</div>
<div style="flex:1;min-width:0;">
<div style="font-size:16px;font-weight:700;color:#111827;">{t[‘name’]}{ol}</div>
<div style="color:#6B7280;font-size:13px;margin:2px 0 6px;">{t[‘headline’]}</div>
<div style="color:#F59E0B;font-size:13px;">{“★”*int(t[‘rating’])}{“☆”*(5-int(t[‘rating’]))} <span style="color:#6B7280;font-size:12px;">{t[‘rating’]} ({t[‘reviews’]} reviews)</span></div>
<div style="margin-top:8px;">{stags}</div>
</div>
<div style="text-align:right;flex-shrink:0;min-width:110px;">
<div style="font-size:20px;font-weight:800;color:#1E3A6E;">${t[‘price’]}<span style="font-size:12px;color:#9CA3AF;">/hr</span></div>
<div style="font-size:11px;color:#9CA3AF;">🗓 {t[‘next_slot’]}</div>
<div style="font-size:11px;color:#10B981;margin-top:2px;">✅ {t[‘completion’]}%</div>
</div></div>”””,unsafe_allow_html=True)
b1,b2,b3=st.columns(3)
with b1:
if st.button(“📅 Book Lesson”,key=f”fb_{t[‘id’]}”,use_container_width=True,type=“primary”):
st.session_state.bt=t; st.session_state.nav=“🏠 Dashboard”; st.rerun()
with b2:
wl=st.session_state.wishlist
if st.button(“❤️ Saved” if t[“id”] in wl else “🤍 Wishlist”,key=f”fw_{t[‘id’]}”,use_container_width=True):
if t[“id”] in wl: wl.remove(t[“id”])
else: wl.append(t[“id”])
st.rerun()
with b3:
if st.button(“💬 Message”,key=f”fm_{t[‘id’]}”,use_container_width=True): st.info(f”Chat with {t[‘name’]}…”)

def page_ai():
st.markdown(”<div style='padding:24px 28px 0'><h2 style='margin:0 0 4px'>🤖 AI Teacher Matching</h2><p style='color:#6B7280;margin:0 0 20px'>Answer 6 questions. Our AI finds your perfect teacher instantly.</p></div>”,unsafe_allow_html=True)
step=st.session_state.ai_step; ans=st.session_state.ai_answers; matches=st.session_state.ai_matches
if step==0:
c1,c2=st.columns([2,1])
with c1:
st.markdown(”””<div class="card"><div style="font-weight:700;font-size:15px;color:#111827;margin-bottom:14px;">How the Algorithm Works</div>
<div style="display:grid;gap:14px;">
<div style="display:flex;gap:14px;"><div style="background:#EFF6FF;border-radius:10px;padding:10px;font-size:22px;flex-shrink:0;">🎯</div><div><div style="font-weight:700;color:#111827;">Subject + age matching</div><div style="font-size:13px;color:#6B7280;margin-top:2px;">Finds teachers with the best track record for your child’s age</div></div></div>
<div style="display:flex;gap:14px;"><div style="background:#F0FDF4;border-radius:10px;padding:10px;font-size:22px;flex-shrink:0;">💡</div><div><div style="font-weight:700;color:#111827;">Learning style fit</div><div style="font-size:13px;color:#6B7280;margin-top:2px;">Matches your child’s style with each teacher’s teaching method</div></div></div>
<div style="display:flex;gap:14px;"><div style="background:#FFF7ED;border-radius:10px;padding:10px;font-size:22px;flex-shrink:0;">💰</div><div><div style="font-weight:700;color:#111827;">Budget alignment</div><div style="font-size:13px;color:#6B7280;margin-top:2px;">Only shows teachers within your preferred price range</div></div></div>
<div style="display:flex;gap:14px;"><div style="background:#FDF4FF;border-radius:10px;padding:10px;font-size:22px;flex-shrink:0;">⭐</div><div><div style="font-weight:700;color:#111827;">Performance metrics</div><div style="font-size:13px;color:#6B7280;margin-top:2px;">Rating, rebooking rate, completion rate, and response time</div></div></div>
</div></div>”””,unsafe_allow_html=True)
with c2:
st.markdown(”””<div class="card" style="text-align:center;padding:36px 20px;">
<div style="font-size:56px;margin-bottom:14px;">🤖</div>
<div style="font-weight:800;font-size:17px;color:#111827;margin-bottom:8px;">AI Matchmaker</div>
<div style="color:#6B7280;font-size:13px;line-height:1.6;">14 factors<br>analysed instantly</div>
</div>”””,unsafe_allow_html=True)
if st.button(“🚀 Start AI Matching”,type=“primary”,use_container_width=True): st.session_state.ai_step=1; st.session_state.ai_answers={}; st.session_state.ai_matches=[]; st.rerun()
return
if 1<=step<=len(AI_QS):
q=AI_QS[step-1]; pct=int((step/len(AI_QS))*100)
st.markdown(f”<div style='margin-bottom:6px;display:flex;justify-content:space-between;'><span style='font-weight:700;color:#1E3A6E;'>Question {step} of {len(AI_QS)}</span><span style='color:#6B7280;font-size:13px;'>{pct}% complete</span></div>”,unsafe_allow_html=True)
st.progress(pct/100)
st.markdown(f”<div style='font-size:19px;font-weight:700;color:#111827;margin:16px 0 12px;'>{q[‘q’]}</div>”,unsafe_allow_html=True)
di=q[“opts”].index(ans.get(q[“id”])) if ans.get(q[“id”]) in q[“opts”] else 0
chosen=st.radio(””,q[“opts”],index=di,key=f”aiq{step}”,label_visibility=“collapsed”)
c1,c2,c3=st.columns([1,1,3])
with c1:
if step>1 and st.button(“← Back”,use_container_width=True): st.session_state.ai_step-=1; st.rerun()
with c2:
if st.button(“Next →”,type=“primary”,use_container_width=True):
ans[q[“id”]]=chosen; st.session_state.ai_answers=ans
if step==len(AI_QS):
with st.spinner(“Analysing teachers…”): time.sleep(1.5)
scored=sorted([{**t,“match”:ms(t,ans)} for t in TEACHERS],key=lambda x:-x[“match”])[:3]
st.session_state.ai_matches=scored; st.session_state.ai_step=99
else: st.session_state.ai_step+=1
st.rerun()
with c3:
if st.button(“Start Over”,use_container_width=True): st.session_state.ai_step=0; st.session_state.ai_answers={}; st.session_state.ai_matches=[]; st.rerun()
return
if step==99:
st.success(“🎯 AI matching complete! Here are your top 3 matches.”)
for i,t in enumerate(matches):
lbl=“🏆 Best Match” if i==0 else f”#{i+1} Match”; clr=”#1E3A6E” if i==0 else “#6B7280”
with st.expander(f”{lbl} — {t[‘name’]} · {t[‘match’]}% match”,expanded=(i==0)):
c1,c2=st.columns([3,1])
with c1:
st.markdown(f”<div style='display:flex;align-items:center;gap:14px;margin-bottom:12px;'><div style=‘background:{t[‘abg’]};border-radius:12px;padding:12px;font-size:36px;’>{t[‘emoji’]}</div><div><div style='font-size:18px;font-weight:800;color:#111827;'>{t[‘name’]}</div><div style='color:#6B7280;font-size:13px;'>{t[‘headline’]}</div></div></div>”,unsafe_allow_html=True)
st.write(t[“bio”])
m1,m2,m3,m4=st.columns(4); m1.metric(“⭐ Rating”,t[“rating”]); m2.metric(“✅ Done”,f”{t[‘completion’]}%”); m3.metric(“🔁 Rebook”,f”{t[‘rebooking’]}%”); m4.metric(“⚡ Reply”,t[“response_time”])
with c2:
st.markdown(f”<div style='text-align:center;background:#F8FAFF;border:2px solid {clr};border-radius:16px;padding:22px 14px;'><div style='font-size:2.4rem;font-weight:900;color:{clr};'>{t[‘match’]}%</div><div style='font-size:11px;color:#6B7280;font-weight:700;margin-bottom:10px;'>MATCH</div><div style='font-size:24px;font-weight:800;color:#111827;'>${t[‘price’]}</div><div style='font-size:11px;color:#9CA3AF;'>/hour</div></div>”,unsafe_allow_html=True)
if st.button(“📅 Book”,key=f”mb_{t[‘id’]}”,use_container_width=True,type=“primary”): st.session_state.bt=t; st.session_state.nav=“🏠 Dashboard”; st.rerun()
if st.button(“🔄 Retake Quiz”,use_container_width=True): st.session_state.ai_step=0; st.session_state.ai_answers={}; st.session_state.ai_matches=[]; st.rerun()

def page_lessons():
if not rl(): return
st.markdown(”<div style='padding:24px 28px 0'><h2 style='margin:0 0 20px'>📅 My Lessons</h2></div>”,unsafe_allow_html=True)
tab1,tab2,tab3=st.tabs([“📅 Upcoming”,“✅ Past”,“➕ Book New”])
with tab1:
for b in [{“t”:TEACHERS[0],“date”:“Fri May 12”,“time”:“4:30 PM”,“child”:“Ayaan”,“subj”:“Somali”},{“t”:TEACHERS[2],“date”:“Sat May 13”,“time”:“10:00 AM”,“child”:“Lul”,“subj”:“Quran”}]:
t=b[“t”]
st.markdown(f”””<div class="trow" style="padding:18px 22px;">
<div class="av" style="background:{t['abg']};width:52px;height:52px;font-size:28px;">{t[‘emoji’]}</div>
<div style="flex:1;"><div style="font-size:15px;font-weight:700;color:#111827;">{t[‘name’]}</div>
<div style="font-size:13px;color:#6B7280;">{b[‘subj’]} · {b[‘child’]} · {b[‘date’]} at {b[‘time’]}</div></div>
<div style="background:#F0FDF4;color:#166534;border-radius:99px;padding:4px 14px;font-size:12px;font-weight:700;">Confirmed</div>
<div style="font-size:18px;font-weight:800;color:#1E3A6E;margin-left:12px;">${t[‘price’]}</div></div>”””,unsafe_allow_html=True)
b1,b2,b3=st.columns(3)
with b1:
if st.button(“🎥 Join Lesson”,key=f”jl_{b[‘date’]}”,type=“primary”,use_container_width=True): st.success(“Launching…”)
with b2:
if st.button(“✏️ Reschedule”,key=f”rs_{b[‘date’]}”,use_container_width=True): st.info(“Rescheduling…”)
with b3:
if st.button(“❌ Cancel”,key=f”cl_{b[‘date’]}”,use_container_width=True): st.warning(“Cancelled.”)
with tab2:
for b in [{“t”:TEACHERS[0],“s”:“Somali”,“d”:“May 5”},{“t”:TEACHERS[2],“s”:“Quran”,“d”:“May 3”}]:
with st.expander(f”{b[‘t’][‘name’]} — {b[‘s’]} — {b[‘d’]}”):
r=st.slider(“Rate ⭐”,1,5,5,key=f”rate_{b[‘d’]}”); st.text_area(“Review”,placeholder=“Share your experience…”,key=f”rev_{b[‘d’]}”)
c1,c2=st.columns(2)
with c1:
if st.button(“Submit”,key=f”sr_{b[‘d’]}”,type=“primary”): st.success(f”Rated {r}⭐!”)
with c2:
if st.button(“🔄 Book Again”,key=f”ba_{b[‘d’]}”): st.success(“Re-booking…”)
with tab3:
c1,c2=st.columns(2)
with c1: tc=st.selectbox(“Teacher”,[t[“name”] for t in TEACHERS]); cc=st.selectbox(“Child”,[“Ayaan”,“Lul”]); sc=st.selectbox(“Subject”,[“Quran”,“Somali”,“Arabic”,“Math”])
with c2: ld=st.date_input(“Date”,min_value=datetime.date.today()); lt=st.selectbox(“Time”,[“9:00 AM”,“10:00 AM”,“2:00 PM”,“3:30 PM”,“4:30 PM”,“6:00 PM”]); ltype=st.selectbox(“Type”,[“Regular (60 min)”,“Extended (90 min)”,“Trial (30 min — Free)”])
if st.button(“✅ Confirm Booking”,type=“primary”,use_container_width=True): st.balloons(); st.success(f”Booked with {tc} on {ld} at {lt}!”)

def page_messages():
if not rl(): return
st.markdown(”<div style='padding:24px 28px 0'><h2 style='margin:0 0 20px'>💬 Messages</h2></div>”,unsafe_allow_html=True)
c1,c2=st.columns([1,2.5])
with c1:
st.markdown(”<div class='card' style='padding:0;overflow:hidden;'>”,unsafe_allow_html=True)
for t in TEACHERS[:5]:
st.markdown(f”<div style='display:flex;align-items:center;gap:12px;padding:13px 14px;border-bottom:1px solid #F3F4F6;cursor:pointer;'><div style='font-size:26px;'>{t[‘emoji’]}</div><div><div style='font-size:13px;font-weight:700;color:#111827;'>{t[‘name’]}</div><div style='font-size:11px;color:#9CA3AF;'>Last message 2h ago</div></div></div>”,unsafe_allow_html=True)
st.markdown(”</div>”,unsafe_allow_html=True)
with c2:
st.markdown(f”<div class='card'><div style='border-bottom:1px solid #E5E7EB;padding-bottom:14px;margin-bottom:16px;display:flex;align-items:center;gap:12px;'><div style='font-size:30px;'>{TEACHERS[0][‘emoji’]}</div><div><div style='font-weight:700;color:#111827;'>{TEACHERS[0][‘name’]}</div><div style='font-size:12px;color:#10B981;'>● Online now</div></div></div>”,unsafe_allow_html=True)
for msg,role in [(“Assalamu alaykum! I look forward to our lesson today.”,“teacher”),(“Wa alaykum assalam! Me too, see you at 4:30 PM!”,“parent”),(“Great! I have prepared new Somali vocabulary for Ayaan 📚”,“teacher”)]:
align=“flex-end” if role==“parent” else “flex-start”; bg=”#1E3A6E” if role==“parent” else “#F3F4F6”; clr=“white” if role==“parent” else “#111827”
st.markdown(f”<div style='display:flex;justify-content:{align};margin-bottom:10px;'><div style='background:{bg};color:{clr};border-radius:12px;padding:10px 14px;font-size:13px;max-width:70%;'>{msg}</div></div>”,unsafe_allow_html=True)
st.markdown(”</div>”,unsafe_allow_html=True)
c_msg,c_btn=st.columns([4,1])
with c_msg: st.text_input(””,placeholder=“Type a message…”,label_visibility=“collapsed”)
with c_btn:
if st.button(“Send →”,type=“primary”,use_container_width=True): st.success(“Sent!”)

def page_progress():
if not rl(): return
user=gu()
st.markdown(”<div style='padding:24px 28px 0'><h2 style='margin:0 0 20px'>📊 Progress Tracker</h2></div>”,unsafe_allow_html=True)
children=user.get(“children”,[])
if not children: st.info(“No children added yet.”); return
sel=st.selectbox(“Select child”,[c[“name”] for c in children]); child=next(c for c in children if c[“name”]==sel)
k1,k2,k3,k4=st.columns(4); k1.metric(“📚 Lessons”,child.get(“lessons”,7),”+2 this week”); k2.metric(“🔥 Streak”,f”{child.get(‘streak’,5)} days”,”+1”); k3.metric(“🏅 Badges”,“8”,”+1 this week”); k4.metric(“📈 Progress”,“45%”,”+5%”)
st.markdown(”—”)
tab1,tab2,tab3=st.tabs([“🌳 Skill Tree”,“🏅 Badges”,“📈 Charts”])
with tab1:
subj=st.radio(“Subject”,[“Somali Language”,“Quran Journey”,“Arabic”],horizontal=True)
sm={“Somali Language”:[(“Greetings”,“done”),(“Family & Numbers”,“done”),(“Colours”,“done”),(“Daily Routines”,“current”),(“Food & Market”,“locked”),(“Storytelling”,“locked”)],“Quran Journey”:[(“Al-Fatiha”,“done”),(“Al-Ikhlas”,“done”),(“Al-Falaq”,“current”),(“An-Nas”,“locked”),(“Al-Kawthar”,“locked”),(“Tajweed”,“locked”)],“Arabic”:[(“Alphabet A-M”,“done”),(“Alphabet N-Y”,“current”),(“Basic Vocab”,“locked”),(“Sentences”,“locked”),(“Reading”,“locked”),(“Writing”,“locked”)]}
skills=sm[subj]; cols=st.columns(len(skills))
for col,(name,status) in zip(cols,skills):
with col:
if status==“done”: st.success(f”✅\n{name}”)
elif status==“current”: st.warning(f”▶️\n{name}”)
else: st.markdown(f”<div style='background:#F9FAFB;border:1px dashed #D1D5DB;border-radius:10px;padding:10px;font-size:11px;color:#9CA3AF;text-align:center;'>🔒<br>{name}</div>”,unsafe_allow_html=True)
done=sum(1 for _,s in skills if s==“done”); st.progress(done/len(skills),text=f”{done}/{len(skills)} complete”)
with tab2:
badges=[(“🌟”,“1st Lesson”,True),(“📖”,“5 Lessons”,True),(“🗣️”,“10 Words”,True),(“✅”,“10 Lessons”,True),(“🔥”,“7-Day Streak”,True),(“📿”,“1st Surah”,True),(“🌙”,“Ramadan”,True),(“⭐”,“Top Student”,True),(“🏆”,“25 Lessons”,False),(“💎”,“Hafidh”,False)]
cols=st.columns(5)
for i,(ic,name,earned) in enumerate(badges):
with cols[i%5]:
if earned: st.markdown(f”<div style='text-align:center;background:#FFFBEB;border:2px solid #FCD34D;border-radius:12px;padding:14px;margin-bottom:8px;'><div style='font-size:28px;'>{ic}</div><div style='font-weight:700;font-size:11px;color:#111827;margin-top:6px;'>{name}</div></div>”,unsafe_allow_html=True)
else: st.markdown(f”<div style='text-align:center;background:#F9FAFB;border:1px dashed #D1D5DB;border-radius:12px;padding:14px;margin-bottom:8px;opacity:0.5;'><div style='font-size:28px;'>🔒</div><div style='font-size:10px;color:#9CA3AF;margin-top:6px;'>{name}</div></div>”,unsafe_allow_html=True)
with tab3:
df=pd.DataFrame({“Week”:[f”Wk{i+1}” for i in range(8)],“Lessons”:[1,2,1,2,2,1,2,2],“Words”:[5,12,8,18,15,10,20,22]})
c1,c2=st.columns(2)
with c1: fig=px.bar(df,x=“Week”,y=“Lessons”,title=“Lessons Per Week”,color_discrete_sequence=[”#1E3A6E”]); fig.update_layout(plot_bgcolor=“white”,paper_bgcolor=“white”); st.plotly_chart(fig,use_container_width=True)
with c2: fig2=px.line(df,x=“Week”,y=“Words”,title=“Vocabulary Growth”,color_discrete_sequence=[”#16A34A”],markers=True); fig2.update_layout(plot_bgcolor=“white”,paper_bgcolor=“white”); st.plotly_chart(fig2,use_container_width=True)

def page_pricing():
st.markdown(”<div style='padding:24px 28px 0'><h2 style='margin:0 0 4px'>💳 Simple Pricing</h2><p style='color:#6B7280;margin:0 0 20px'>Start free. No hidden fees.</p></div>”,unsafe_allow_html=True)
billing=st.radio(“Billing”,[“Monthly”,“Annual (Save 20%)”],horizontal=True); annual=“Annual” in billing
if annual: st.success(“🎉 Saving 20% with annual billing!”)
with st.expander(“🏷️ Promo code”):
pc1,pc2=st.columns([2,1])
with pc1: promo=st.text_input(“Code”,placeholder=“SOMALI10”).upper()
with pc2:
if st.button(“Apply”,type=“primary”):
codes={“SOMALI10”:0.9,“FIRST20”:0.8,“DIASPORA”:0.85}
if promo in codes: st.session_state.promo_discount=codes[promo]; st.success(f”✅ {int((1-codes[promo])*100)}% off!”)
else: st.error(“Invalid. Try SOMALI10 or FIRST20”)
disc=st.session_state.promo_discount; st.markdown(”—”)
cols=st.columns(4)
for col,plan in zip(cols,PLANS):
with col:
raw=plan[“pa”] if annual else plan[“pm”]
pd_str=“Custom” if raw is None else “Free” if raw==0 else f”${int(raw*disc)}/mo”
pop=plan.get(“popular”,False); border=“2px solid #1E3A6E” if pop else “1px solid #E5E7EB”; bg=”#EFF6FF” if pop else “white”
fh=””.join(f’<div style="font-size:13px;color:#374151;margin-bottom:8px;display:flex;gap:8px;"><span style="color:#16A34A;font-weight:700;">✓</span>{f}</div>’ for f in plan[“features”])
pb=’<div style="background:#1E3A6E;color:white;text-align:center;font-size:11px;font-weight:700;padding:6px;border-radius:8px 8px 0 0;margin:-24px -24px 16px;">⭐ MOST POPULAR</div>’ if pop else “”
st.markdown(f”<div style='background:{bg};border:{border};border-radius:16px;padding:24px;min-height:380px;'>{pb}<div style='font-size:28px;margin-bottom:8px;'>{plan[‘emoji’]}</div><div style='font-weight:800;font-size:17px;color:#111827;margin-bottom:6px;'>{plan[‘name’]}</div><div style=‘font-size:2rem;font-weight:900;color:{’#1E3A6E’ if pop else ‘#111827’};margin:10px 0;’>{pd_str}</div><hr style='border:none;border-top:1px solid #E5E7EB;margin:14px 0;'>{fh}</div>”,unsafe_allow_html=True)
ctas={“starter”:“Start Free”,“family”:“Start Trial”,“premium”:“Get Premium”,“school”:“Contact Sales”}
if st.button(ctas[plan[“id”]],key=f”p_{plan[‘id’]}”,use_container_width=True,type=“primary” if pop else “secondary”):
if plan[“id”]==“school”: st.info(“📧 sales@somalitutor.com”)
else: st.balloons(); st.success(f”🎉 Welcome to {plan[‘name’]}!”)

def page_login():
*,c,*=st.columns([1,1.5,1])
with c:
st.markdown(’<div class="card"><div style="text-align:center;margin-bottom:24px;"><div style="font-size:44px;">🛡️</div><h2 style="margin:8px 0 4px;">Welcome back</h2><p style="color:#6B7280;">Log in to SomaliTutor</p></div>’,unsafe_allow_html=True)
with st.form(“lf”):
email=st.text_input(“Email”,placeholder=“parent@demo.com”); password=st.text_input(“Password”,type=“password”,placeholder=“demo1234”)
if st.form_submit_button(“Log In →”,type=“primary”,use_container_width=True):
u=DEMO_USERS.get(email.strip().lower())
if not u: st.error(“No account found.”)
elif u[“password”]!=password: st.error(“Wrong password.”)
else: st.session_state.user={k:v for k,v in u.items() if k!=“password”}; st.session_state.nav=“🏠 Dashboard”; st.rerun()
st.markdown(”</div>”,unsafe_allow_html=True)
st.markdown(’<div class="card" style="margin-top:12px;"><div style="font-weight:700;color:#374151;margin-bottom:10px;">🎭 Demo Accounts</div><div style="font-size:13px;color:#6B7280;line-height:2.1;"><div>👩 parent@demo.com / demo1234</div><div>👩‍🏫 teacher@demo.com / demo1234</div><div>⚙️ admin@demo.com / admin1234</div></div></div>’,unsafe_allow_html=True)
if st.button(“Create Account →”,use_container_width=True): st.session_state.nav=“✍️ Sign Up”; st.rerun()

def page_signup():
*,c,*=st.columns([1,1.5,1])
with c:
st.markdown(’<div class="card"><div style="text-align:center;margin-bottom:24px;"><div style="font-size:44px;">🎉</div><h2 style="margin:8px 0 4px;">Create Account</h2><p style="color:#6B7280;">Join 2,000+ diaspora families</p></div>’,unsafe_allow_html=True)
with st.form(“sf”):
role=st.radio(“I am a:”,[“Parent / Guardian”,“Teacher”],horizontal=True)
name=st.text_input(“Full name”); email=st.text_input(“Email”); password=st.text_input(“Password (min 8 chars)”,type=“password”); confirm=st.text_input(“Confirm password”,type=“password”); agree=st.checkbox(“I agree to Terms of Service”)
if st.form_submit_button(“Create Account →”,type=“primary”,use_container_width=True):
if not agree: st.error(“Please agree to terms.”)
elif password!=confirm: st.error(“Passwords do not match.”)
elif len(password)<8: st.error(“Min 8 characters.”)
elif not name or not email: st.error(“Fill in all fields.”)
else: st.session_state.user={“id”:“new”,“name”:name.strip(),“email”:email.lower(),“role”:“parent” if “Parent” in role else “teacher”,“children”:[],“plan”:“starter”,“avatar”:“👤”}; st.session_state.nav=“🏠 Dashboard”; st.balloons(); st.rerun()
st.markdown(”</div>”,unsafe_allow_html=True)

def page_account():
if not rl(): return
user=gu()
st.markdown(f”<div style='padding:24px 28px 0'><h2 style='margin:0 0 20px'>👤 My Account</h2></div>”,unsafe_allow_html=True)
tab1,tab2,tab3=st.tabs([“Profile”,“Subscription”,“Notifications”])
with tab1:
with st.form(“pf”):
c1,c2=st.columns(2)
with c1: st.text_input(“Full name”,value=user[“name”]); st.text_input(“Email”,value=user[“email”])
with c2: st.text_input(“Phone”,placeholder=”+44 7700 900000”); st.selectbox(“Country”,[“United Kingdom”,“United States”,“Canada”,“Sweden”,“UAE”,“Australia”,“Somalia”,“Other”])
st.text_area(“Bio”,placeholder=“Tell teachers about your family…”,height=80)
if st.form_submit_button(“Save Changes”,type=“primary”): st.success(“✅ Profile updated!”)
with tab2:
plan=user.get(“plan”,“starter”)
st.markdown(f”<div class='card' style='background:#1E3A6E;'><div style='font-size:13px;color:rgba(255,255,255,.6);margin-bottom:4px;'>Current Plan</div><div style='font-size:2rem;font-weight:900;color:white;'>{plan.title()}</div><div style='color:rgba(255,255,255,.6);font-size:13px;margin-top:4px;'>Next billing: June 1, 2025</div></div>”,unsafe_allow_html=True)
c1,c2=st.columns(2)
with c1:
if st.button(“⬆️ Upgrade”,type=“primary”,use_container_width=True): st.session_state.nav=“💎 Pricing”; st.rerun()
with c2:
if st.button(“❌ Cancel”,use_container_width=True): st.warning(“Will end at billing period.”)
with tab3:
with st.form(“nf”):
st.checkbox(“📧 Lesson reminders”,value=True); st.checkbox(“📧 Weekly summary”,value=True); st.checkbox(“📱 WhatsApp reminders”,value=False); st.checkbox(“🔔 Booking confirmations”,value=True)
if st.form_submit_button(“Save”,type=“primary”): st.success(“✅ Saved!”)
st.divider()
if st.button(“🚪 Log Out”,use_container_width=True): st.session_state.user=None; st.session_state.nav=“🏠 Dashboard”; st.rerun()

def page_teacher_hub():
if not rl(): return
user=gu(); t=next((x for x in TEACHERS if x[“id”]==user.get(“teacher_id”,1)),TEACHERS[0])
st.markdown(f”<div style='padding:24px 28px 0;display:flex;align-items:center;gap:14px;margin-bottom:18px;'><div style=‘background:{t[‘abg’]};border-radius:14px;padding:10px;font-size:44px;’>{t[‘emoji’]}</div><div><h2 style='margin:0;'>{t[‘name’]}</h2><p style='color:#6B7280;margin:4px 0;'>{t[‘headline’]}</p><span style='background:#FFFBEB;color:#92400E;border-radius:99px;padding:3px 14px;font-size:12px;font-weight:700;'>{t[‘badge’]} · 85% commission</span></div></div>”,unsafe_allow_html=True)
tab1,tab2,tab3,tab4=st.tabs([“📊 Overview”,“💰 Earnings”,“👥 Students”,“🛠️ Profile”])
with tab1:
k1,k2,k3,k4,k5=st.columns(5); k1.metric(“📅 Lessons”,“32”,”+8”); k2.metric(“💰 Earnings”,”$384”,”+22%”); k3.metric(“⭐ Rating”,t[“rating”]); k4.metric(“🔁 Rebooking”,f”{t[‘rebooking’]}%”); k5.metric(“✅ Completion”,f”{t[‘completion’]}%”)
st.markdown(”—”)
for l in [{“ch”:“Ayaan”,“s”:“Somali”,“d”:“Today 4:30 PM”},{“ch”:“Lul”,“s”:“Quran”,“d”:“Sat 10:00 AM”},{“ch”:“Hashi”,“s”:“Arabic”,“d”:“Mon 5:00 PM”}]:
c1,c2,c3=st.columns([3,2,1])
with c1: st.write(f”**{l[‘ch’]}** — {l[‘s’]}”)
with c2: st.write(f”📅 {l[‘d’]}”)
with c3:
if st.button(“🎥 Join”,key=f”th_{l[‘ch’]}”,type=“primary”): st.success(“Launching…”)
with tab2:
e1,e2,e3,e4=st.columns(4); e1.metric(“Month”,”$384”); e2.metric(“Pending”,”$54”); e3.metric(“Available”,”$330”); e4.metric(“All Time”,”$5,760”)
with st.expander(“💸 Withdraw”):
with st.form(“wd”):
amt=st.number_input(“Amount ($)”,20,330,100); meth=st.selectbox(“Method”,[“Bank Transfer”,“PayPal”,“Wise”,“EVC Plus”,“Zaad”])
if st.form_submit_button(“Request”,type=“primary”): st.success(f”✅ ${amt} via {meth} requested!”)
df=pd.DataFrame([{“Date”:“May 10”,“Student”:“Ayaan”,“Gross”:”$15”,“Net”:”$12.75”,“Status”:“Paid”},{“Date”:“May 10”,“Student”:“Lul”,“Gross”:”$15”,“Net”:”$12.75”,“Status”:“Paid”},{“Date”:“May 9”,“Student”:“Hashi”,“Gross”:”$15”,“Net”:”$12.75”,“Status”:“Pending”}])
st.dataframe(df,use_container_width=True,hide_index=True); st.download_button(“📥 Export CSV”,df.to_csv(index=False),“earnings.csv”,“text/csv”)
with tab3:
for s in [{“n”:“Ayaan”,“a”:9,“s”:“Somali”,“l”:7,“p”:45},{“n”:“Lul”,“a”:7,“s”:“Quran”,“l”:4,“p”:30},{“n”:“Hashi”,“a”:12,“s”:“Arabic”,“l”:12,“p”:60}]:
with st.expander(f”👤 {s[‘n’]} (Age {s[‘a’]}) — {s[‘s’]}”):
st.write(f”Lessons: {s[‘l’]}”); st.progress(s[“p”]/100,text=f”{s[‘p’]}%”)
with st.form(f”tn_{s[‘n’]}”):
st.text_area(“Note”,height=60,placeholder=“Today we covered…”)
if st.form_submit_button(“Save”): st.success(“Saved!”)
with tab4:
with st.form(“thp”):
c1,c2=st.columns(2)
with c1: st.text_input(“Name”,value=t[“name”]); st.number_input(“Rate ($)”,5,50,t[“price”])
with c2: st.text_input(“Headline”,value=t[“headline”]); st.multiselect(“Subjects”,[“Quran”,“Somali”,“Arabic”,“Math”,“English”,“Islamic Studies”],default=t[“subjects”])
st.text_area(“Bio”,value=t[“bio”],height=80); st.checkbox(“Offer free trial”,value=True)
if st.form_submit_button(“Save Profile”,type=“primary”): st.success(“✅ Updated!”)

def page_admin():
if not rl(): return
user=gu()
if user.get(“role”)!=“admin”: st.error(“🔒 Admin only. Log in as admin@demo.com”); return
st.markdown(”<div style='padding:24px 28px 0;display:flex;align-items:center;gap:12px;margin-bottom:18px;'><span style='background:#DC2626;color:white;border-radius:8px;padding:6px 14px;font-weight:700;font-size:13px;'>⚙️ ADMIN</span><h2 style='margin:0;'>Control Center</h2></div>”,unsafe_allow_html=True)
tab1,tab2,tab3,tab4,tab5=st.tabs([“📊 KPIs”,“👥 Users”,“🔎 Disputes”,“💰 Finance”,“📈 Analytics”])
with tab1:
k1,k2,k3,k4,k5=st.columns(5); k1.metric(“👨‍👩‍👧 Families”,“2,041”,”+47”); k2.metric(“🎓 Teachers”,“148”,”+3”); k3.metric(“📅 Today”,“312”,”+18%”); k4.metric(“💰 MTD”,”$24,810”,”+22%”); k5.metric(“⭐ Rating”,“4.91”,”+0.01”)
st.markdown(”—”)
for ic,lv,msg in [(“🚨”,“High”,“3 teachers not responded >6 hours”),(“⚠️”,“Med”,“Payment failure rate 2.3%”),(“ℹ️”,“Low”,“5 new applications pending”)]:
bg={“High”:”#FEF2F2”,“Med”:”#FFFBEB”,“Low”:”#F0FDF4”}[lv]; tc={“High”:”#991B1B”,“Med”:”#92400E”,“Low”:”#166534”}[lv]
c1,c2=st.columns([8,1])
with c1: st.markdown(f”<div style='background:{bg};color:{tc};border-radius:10px;padding:10px 14px;margin-bottom:8px;font-size:13px;font-weight:500;'>{ic} <b>{lv}:</b> {msg}</div>”,unsafe_allow_html=True)
with c2: st.button(“✕”,key=f”al_{msg[:8]}”)
with tab2:
st.dataframe(pd.DataFrame([{“Name”:t[“name”],“Badge”:t[“badge”],“Rating”:t[“rating”],“Lessons”:t[“lessons”],“Status”:“Active”} for t in TEACHERS]),use_container_width=True,hide_index=True)
c1,c2=st.columns(2)
with c1: sus=st.selectbox(“Suspend”,[t[“name”] for t in TEACHERS])
with c2:
if st.button(“⚠️ Suspend”,type=“primary”): st.warning(f”{sus} suspended.”)
with tab3:
for d in [{“id”:“D-001”,“f”:“A. Osman”,“t”:“K. Hassan”,“amt”:”$15”,“r”:“Teacher was 20 min late”,“u”:“High”},{“id”:“D-002”,“f”:“H. Ahmed”,“t”:“A. Farah”,“amt”:”$12”,“r”:“Lesson quality issue”,“u”:“Med”}]:
with st.expander(f”{d[‘id’]} — {d[‘f’]} vs {d[‘t’]}”):
st.write(f”**Reason:** {d[‘r’]}”); d1,d2,d3=st.columns(3)
with d1:
if st.button(f”💸 Refund”,key=f”rf_{d[‘id’]}”): st.success(“Refund issued!”)
with d2:
if st.button(“💬 Chat”,key=f”ch_{d[‘id’]}”): st.info(“Loading…”)
with d3:
if st.button(“✅ Resolve”,key=f”rs_{d[‘id’]}”): st.success(“Resolved.”)
with tab4:
f1,f2,f3,f4=st.columns(4); f1.metric(“💰 Gross”,”$24,810”); f2.metric(“📊 Commission”,”$4,962”); f3.metric(“💸 Payouts”,”$19,848”); f4.metric(“📈 Net”,”$4,962”)
df=pd.DataFrame([{“Date”:“May 10”,“Family”:“A. Osman”,“Teacher”:“K. Hassan”,“Gross”:”$15”,“Status”:“Paid”},{“Date”:“May 9”,“Family”:“M. Hassan”,“Teacher”:“H. Warsame”,“Gross”:”$18”,“Status”:“Pending”}])
st.dataframe(df,use_container_width=True,hide_index=True); st.download_button(“📥 Export”,df.to_csv(index=False),“transactions.csv”,“text/csv”)
with tab5:
c1,c2=st.columns(2)
with c1:
fig=px.pie(pd.DataFrame({“Subject”:[“Quran”,“Somali”,“Arabic”,“Math”,“English”],“Bookings”:[412,287,198,145,89]}),names=“Subject”,values=“Bookings”,title=“Bookings by Subject”,color_discrete_sequence=[”#1E3A6E”,”#16A34A”,”#F59E0B”,”#8B5CF6”,”#06B6D4”]); st.plotly_chart(fig,use_container_width=True)
with c2:
fig2=px.bar(pd.DataFrame({“Country”:[“UK”,“USA”,“Canada”,“Sweden”,“UAE”,“Australia”],“Families”:[520,480,310,220,190,155]}),x=“Families”,y=“Country”,orientation=“h”,title=“Top Countries”,color_discrete_sequence=[”#1E3A6E”]); fig2.update_layout(plot_bgcolor=“white”,paper_bgcolor=“white”); st.plotly_chart(fig2,use_container_width=True)

n=st.session_state.nav
if   “Dashboard” in n: page_home()
elif “Find”      in n: page_find()
elif “AI”        in n: page_ai()
elif “Lessons”   in n: page_lessons()
elif “Messages”  in n: page_messages()
elif “Progress”  in n: page_progress()
elif “Pricing”   in n or “Payment” in n: page_pricing()
elif “Login”     in n: page_login()
elif “Sign Up”   in n: page_signup()
elif “Account”   in n: page_account()
elif “Teacher”   in n: page_teacher_hub()
elif “Admin”     in n: page_admin()
else: page_home()
