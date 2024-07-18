from pathlib import Path
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
import streamlit.components.v1 as components

# ------------ PATH SETTINGS ----------
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
# css_file = current_dir / "styles" / "main.css"
# resume_file = current_dir / "assets" / "CJCHEW-Resume_2023_v1.pdf"
# profile_pic = current_dir / "assets" / "home" /"profile-pic.png"
# my_zone_pic = current_dir / "assets" / "home" / "my_zone.png"
css_file = ("./styles/main.css")
resume_file = ("./assets/CJCHEW-Resume_2023_v1.pdf")
profile_pic = ("./assets/home/profile-pic.png")

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
PROJECTS = {
    "📋 Digital resume streamlit ": "https://github.com/MouadEttali/streamlit_resume",
    "📊 Quantatitive Backtest App streamlit ": "",
    "📈 Crypto Algorithm Trading Bot (Bybit)": ""
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Function to generate social media icons
def social_media_icon(link, icon_url, name):
    return f'''
    <a href="{link}" target="_blank" style="text-decoration:none;">
        <img src="{icon_url}" alt="{name}" width="40" height="40" style="display:block;margin-left:auto;margin-right:auto;">
    </a>
    <p style="text-align:center;font-size:16px;margin-top:10px;">{name}</p>
    '''

# Sidebar content
def sidebar_item(icon, name, key=None):
    st.sidebar.markdown(f"""
        <div class="icon-item">
            <a href="#" onclick="toggleSidebar('{key}')">
                <i class="fa {icon}" style="font-size:24px;"></i>
            </a>
            <span class="tooltip">{name}</span>
        </div>
    """, unsafe_allow_html=True)
    if st.session_state.get(key, False):
        st.session_state['sidebar_expanded'] = not st.session_state.get('sidebar_expanded', True)

st.sidebar.markdown("""
    <script>
        function toggleSidebar(key) {
            var expanded = localStorage.getItem(key);
            if (expanded === "true") {
                localStorage.setItem(key, "false");
                document.body.classList.remove("sidebar-expanded");
            } else {
                localStorage.setItem(key, "true");
                document.body.classList.add("sidebar-expanded");
            }
        }
    </script>
""", unsafe_allow_html=True)

# Check sidebar expanded state
if 'sidebar_expanded' not in st.session_state:
    st.session_state['sidebar_expanded'] = False

# Add the expanded class to the body if sidebar is expanded
if st.session_state['sidebar_expanded']:
    st.markdown('<style>body{overflow: hidden;}body.sidebar-expanded .sidebar-content { width: 60px; }</style>', unsafe_allow_html=True)

# Sidebar items with Font Awesome icons
sidebar_item("fa-home", "Home", key="home")
sidebar_item("fa-graduation-cap", "Academic Background", key="academic")
sidebar_item("fa-briefcase", "Professional Experiences", key="professional")
sidebar_item("fa-flask", "Personal Projects", key="projects")
sidebar_item("fa-certificate", "Certifications", key="certifications")

# Main content
if st.session_state.get('home', False):
    st.title("🏡 Home")
    st.write("This is the home page of the resume.")

if st.session_state.get('academic', False):
    st.title("🎓 Academic Background")
    st.write("This is the academic background section of the resume.")

if st.session_state.get('professional', False):
    st.title("💼 Professional Experiences")
    st.write("This is the professional experiences section of the resume.")

if st.session_state.get('projects', False):
    st.title("🔬 Personal Projects")
    st.write("This is the personal projects section of the resume.")

if st.session_state.get('certifications', False):
    st.title("📜 Certifications")
    st.write("This is the certifications section of the resume.")


st.title("Hi / 您好 / Apa Kahbar")

# --------------- HELPER FUNCTIONS -----------------------
def V_SPACE(lines):
    for _ in range(lines):
        st.write('&nbsp;')

def go_to_full_page(label,page):
    personal_project = st.button(label)
    if personal_project:
        switch_page(page)


# ----------- CSS, PDF & Profile Pic SETTINGS --------------

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

profile_pic = Image.open(profile_pic)

my_zone_pic = Image.open(my_zone_pic)
# ------ HERO SECTION -----------

cols = st.columns(2, gap='small')

with cols[0]:
    st.image(profile_pic)
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
# st.write(
#     """
#     - ✔️ **8 years of experience** in SAP SuccessFactors consulting firms for clients like <span style="color:#f50057; font-size: 15;">Total Energies , ONCF , Nexans, Allegro Musique </span> (Details in Professional Experiences)
#     - ✔️ Built multiple ML based web applications (Python, Javascript, D3js, Streamlit) with deployment in AWS **(Sagemaker, API Gateway, Lambda).**
#     - ✔️ Expertise in statistical principles and classical ML models
#     - ✔️ Product and value oriented mindset ( my dream is to build valuable ML tools, my nightmare is models dying in notebooks )
#     - ✔️ Work feels best when it's **challenging enough to push me and not easy enough to make me bored**
#     """
# ,unsafe_allow_html=True)

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
st.write('\n')
st.subheader("Hard Skills 🛠️")
st.write(
    """
- 👩‍💻 Programming: Python, SQL, Microsoft Office, HTML
- 🧪 Data science : Machine Learning, Deep Learning, Optimisation
- 🗄️ Databases: Microsoft SQL Server
- 🚀 Deployment : Github, Steamlit
"""
)
go_to_full_page("See my certifications and trainings" , "Certifications")

# --------- work history ---------
V_SPACE(1)
st.subheader("Recent Job Experience 🏢")
st.write('---')

st.write('\n')
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

go_to_full_page("Check out all my experiences" , "Professional Experiences")


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Personal Projects 🧠")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

go_to_full_page("More Personal Projects" , "Personal Projects")

# Add footer
st.write('---')
st.write('© Chew Chuan Juen  |  Last updated: July 2024')