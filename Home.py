from pathlib import Path
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
import streamlit.components.v1 as components

# ------------ PATH SETTINGS ----------
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CJCHEW-Resume_Full.pdf"
profile_pic = current_dir / "assets" / "home" /"profile-pic.png"
OLMPIA_PIC_PATH = current_dir / "assets" / "academic" /"olympia.png"
INFO_PIC_PATH = current_dir / "assets" / "academic" / "informatics.png"
OLMPIA_PICCERT_PATH = current_dir / "assets" / "academic" / "degree.png"
INFO_PICCERT_PATH = current_dir / "assets" / "academic" / "adiploma.png"

# ------------ CONSTANTS ----------
PAGE_TITLE = "Digital Resume | CJ Chew"
PAGE_ICON = "💼"
NAME = "Chuan Juen (CJ) Chew"
GENDER = "MALE 🚹"
DESCRIPTION = """
SAP SuccessFactors Senior Consultant @ Tenthpin Malaysia, specializing in HXM project rollouts, 
passionate about programming and data-driven machine learning.
"""
EMAIL = "ccjuen@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/chuan-juen-cj-chew-99012462/",
    "GitHub": "https://github.com/cjchew82",
    "X": "",
    "Facebook": "",
    "Instagram": ""
}
SOCIAL_MEDIA_ICONS = {
    "LinkedIn": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/600px-LinkedIn_logo_initials.png?20140125013055",
    "GitHub": "https://cdn-icons-png.flaticon.com/512/25/25231.png",
    "X": "https://upload.wikimedia.org/wikipedia/commons/c/ce/X_logo_2023.svg",
    "Facebook": "https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg",
    "Instagram": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png"
}
#----------- Education-------------------
# ---------- OLMPIA ------------------
OLMPIA_PIC  = Image.open(OLMPIA_PIC_PATH)
OLMPIA_TITLE = "**Bachelor's Degree in Computer Science/Information Technology**"
OLMPIA_PERIOD = "03/2006 - 09/2007"
OLMPIA_MAJOR = "Networking"
OLMPIA_GRADE = "Grade C/2nd Class Lower"
OLMPIA_CERT = Image.open(OLMPIA_PICCERT_PATH)
# ---------------------------------

# ---------- INFORMATICS ------------------
INFO_PIC  = Image.open(INFO_PIC_PATH)
INFO_TITLE = "**Bachelor's Degree in Computer Science/Information Technology**"
INFO_PERIOD = "05/2001 - 10/2003"
INFO_MAJOR = "Networking and Communication, Multimedia, and Internet"
INFO_GRADE = "Grade D/3rd Class"
INFO_CERT = Image.open(INFO_PICCERT_PATH)
# --------------------------------------

PROJECTS = {
    "📋 Digital resume streamlit ": "https://github.com/MouadEttali/streamlit_resume",
    "📊 Quantatitive Backtest App streamlit ": "",
    "📈 Crypto Algorithm Trading Bot (Bybit)": ""
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

st.markdown("""
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <style>
        .sidebar .css-1v3fvcr { 
            font-size: 16px; 
            font-family: 'Material Icons';
        }
        .vertical-align-middle {
            display: flex;
            align-items: center;
            height: 20px;
        }
        /* Custom slider style */
        .stSlider > div > div > div {
            height: 10px;
        }
        .stSlider > div > div > div > div[role="slider"] {
            width: 20px;
            height: 20px;
            background-color: #007bff;
        }
    </style>
""", unsafe_allow_html=True)

# Function to generate social media icons
def social_media_icon(link, icon_url, name):
    return f'''
    <a href="{link}" target="_blank" style="text-decoration:none;">
        <img src="{icon_url}" alt="{name}" width="40" height="40" style="display:block;margin-left:auto;margin-right:auto;">
    </a>
    <p style="text-align:center;font-size:16px;margin-top:10px;">{name}</p>
    '''

st.title("Hi / 您好 / Apa Kahbar")

# --------------- HELPER FUNCTIONS -----------------------
def V_SPACE(lines):
    for _ in range(lines):
        st.write('&nbsp;')

def go_to_full_page(label,page):
    personal_project = st.button(label)
    if personal_project:
        switch_page(page)
        
# go_to_full_page("See my certifications and trainings" , "Certifications")
# def go_switch_page(label,page):
#     click = st.button(page)
#     if click == "Working Experiences":
#         st.switch_page("pages/3_Working_Experiences.py")
#     if click == "Certifications":
#         st.switch_page("pages/4_Certifications.py")
#     if click == "Personal Projects":
#         st.switch_page("pages/5_Personal_Projects.py")

# ----------- CSS, PDF & Profile Pic SETTINGS --------------

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

profile_pic = Image.open(profile_pic)

# my_zone_pic = Image.open(my_zone_pic)
# ------ HERO SECTION -----------

cols = st.columns(2, gap='small')

with cols[0]:
    st.image(profile_pic, width=400)
    # st.image(profile_pic, width=230)
    # st.image(profile_pic, use_column_width=False, width=230, output_format="PNG", caption="Profile Picture", clamp=True, class_="profile-pic")

with cols[1]:
    st.title(NAME)
    st.write("Gender:",GENDER)
    st.write(DESCRIPTION)
    st.download_button(
        label="⏳ Download Resume",
        data= PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write("📤",EMAIL)

# -------- SOCIALS ---------

V_SPACE(1)

# cols = st.columns(len(SOCIAL_MEDIA))
# for index, (platform,link) in enumerate(SOCIAL_MEDIA.items()):
#     cols[index].write(f"[{platform}]({link})")

# Social media icons display
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    with cols[index]:
        st.markdown(social_media_icon(link, SOCIAL_MEDIA_ICONS[platform], platform), unsafe_allow_html=True)

# ------- EXPERIENCE AND QUALIFS --------

V_SPACE(1)
st.subheader('About me 🧑‍🦱')
st.write('---')
st.write(
    """
    - ✔️ **8 years of experience** in SAP SuccessFactors Consulting across various industries, including <span style="color:#f50057; font-size: 15;">manufacturing, shared services, pharmaceutical, refinery & cracker, Life Science, </span> with involvement in multi-country implementations.
    - ✔️ Certified Associate Consultant in **Employee Central, Recruiting (Candidate & Recruiter), Learning Management, and Onboarding.**
    - ✔️ Project lead with comprehensive experience in the full HXM implementation project cycle and system maintenance, covering requirement workshops, iteration reviews, configuration, end-user training, user acceptance testing, and Go-Live hypercare support.
    - ✔️ Solution Architect providing end-to-end HXM architecture flow and workaround solutions.
    - ✔️ Expertise in the SuccessFactors platform, including Reporting Canvas, Integration Center, Job Profile Builder, and API endpoint scripting. Strong knowledge of HR data analysis.
    - ✔️ **2 years of experience** in Python programming, with a passion for exploring data statistics and machine learning.
    """
,unsafe_allow_html=True)

# st.image(my_zone_pic)
# st.write(""" ⚠️ Warning : if you hand me a boring task <span style="color:#f50057; font-size: 15;">I will try to automate it.</span>""",unsafe_allow_html=True)
# --- SKILLS ---
V_SPACE(1)
st.subheader("Hard Skills 🛠️")
st.write('---')
st.write(
    """
- 👩‍💻 Programming: Python, SQL, Microsoft Office, HTML
- 🧪 Data science : Machine Learning, Deep Learning, Optimisation
- 🗄️ Databases: Microsoft SQL Server
- 🚀 Deployment : Github, Steamlit
"""
)
go_to_full_page("See my certifications and trainings" , "Certifications")
# go_switch_page("See my certifications and trainings" , "Certifications")

# --------- Education Background ---------
V_SPACE(1)
st.subheader("Education Background 🎓")
st.write('---')

def education_section(PIC,TITLE,PERIOD,MAJOR,GRADE,CERT=None):
    st.image(PIC, width=200)
    st.write(f"**{TITLE}**")
    st.write(f"MAJOR: "f"***{MAJOR}***")
    st.write(f"GRADE: "f"***{GRADE}***")
    st.write(f"PERIOD: "f"***{PERIOD}***")
    with st.expander("Check Certification"):
        if CERT:
            st.image(CERT, width=300)
    st.write('---')
    
education_section(OLMPIA_PIC, OLMPIA_TITLE, OLMPIA_PERIOD, OLMPIA_MAJOR, OLMPIA_GRADE, OLMPIA_CERT)
education_section(INFO_PIC, INFO_TITLE, INFO_PERIOD, INFO_MAJOR, INFO_GRADE, INFO_CERT )

# --------- Language Skills ---------
V_SPACE(1)
st.subheader("Language Skills 🌐")
st.write('---')

# Define the language skills data
languages = [
    {"language": "English", "writing": 5, "speaking": 5},
    {"language": "Chinese", "writing": 4, "speaking": 5},
    {"language": "Bahasa", "writing": 3, "speaking": 3},
]

# Display the table header
cols = st.columns(3)
cols[0].write("**Language**")
cols[1].markdown("**<div style='text-align: center;'>Writing</div>**", unsafe_allow_html=True)
cols[2].markdown("**<div style='text-align: center;'>Speaking</div>**", unsafe_allow_html=True)

# Display the language skills
for i, lang in enumerate(languages):
    cols = st.columns(3)
    cols[0].markdown(f"<div class='vertical-align-middle'>{lang['language']}</div>", unsafe_allow_html=True)
    cols[1].slider("", 1, 5, lang["writing"], disabled=True, key=f"writing_{i}")
    cols[2].slider("", 1, 5, lang["speaking"], disabled=True, key=f"speaking_{i}")
    
# --------- work history ---------
V_SPACE(1)
st.subheader("Recent Job Experience 🏢")
st.write('---')
st.write("💻", "**SAP SuccessFactors Senior Consultant | Tenthpin Management Consultants Sdn Bhd**")
st.write("12/2021 - Present")

col1, col2, col3 = st.columns(3)

with st.expander("***Project Implementation***"):
    st.write(
        """
        My experience in the full project implementation cycle:
        <ul>
            <li>• Facilitating workshops to gather requirements</li>
            <li>• Conducting system reviews and iterations, performing configuration testing</li>
            <li>• Delivering train-the-trainer sessions, conducting user acceptance tests</li>
            <li>• Providing go-live project support</li>
            <li>• Partially involved in Project Managing such as kick-off meeting</li>
            <li>• Additionally, I guide and collaborate closely with team members to ensure successful project delivery</li>
        </ul>
        """, unsafe_allow_html=True
    )

with st.expander("***Business Development***"):
    st.write(
        """
        <ul>
            <li>• Work closely with the Business Development on any opportunity pipeline bidding presentation</li>
            <li>• Pre-sales demo to client, and discussion with client on project architecture framework</li>
            <li>• Workout on the project timeline and propose the project methodology to client during the bidding presentation</li>
        </ul>
        """, unsafe_allow_html=True
    )

with st.expander("***Client Support***"):
    st.write(
        """
        <ul>
            <li>✅ Project: Clover Biopharmaceuticals (EC, RCM, and ONB 2.0 Oversea UK and US implementation)</li>
            <li>✅ Project: Mindray (EC Integration and SF full suite system support)</li>
            <li>✅ Project: Clover Biopharmaceuticals (Compensation new worksheet implementation)</li>
            <li>✅ Project Fapon Biotech EC and Onboarding Rollout and support</li>
            <li>✅ Project: ND Paper SAP HCM Malaysia Payroll (Project Manager)</li>
        </ul>
        """, unsafe_allow_html=True
    )

go_to_full_page("Check out all my experiences" , "Working Experiences")

V_SPACE(1)
# --- Projects & Accomplishments ---
st.subheader("Personal Projects 🧠")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

go_to_full_page("More Personal Projects" , "Personal Projects")

# Add footer
st.write('---')
st.write('© Chew Chuan Juen  |  Last updated: July 2024')

# Add sidebar text
st.sidebar.text("Created by 💕 CJ Chew")