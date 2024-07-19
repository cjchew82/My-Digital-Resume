from pathlib import Path

import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image


# ------------ PATH SETTINGS ----------
current_dir = Path(__file__).parent.parent
css_file = current_dir / "styles" / "main.css"

DCV_PIC_PATH = current_dir / "assets" / "personal_projects" / "personaldigitalcv.png"

# ------------ CONSTANTS ----------
PAGE_TITLE = "Personal Projects | CJ Chew"
PAGE_ICON = "🔬"

#-------- PERSONAL PROJECTS CONTENT----------
DCV_PIC  = Image.open(DCV_PIC_PATH)
DCV_PROJECT_TITLE = "Streamlit Personal Digital Resume"
DCV_PROJECT_LINK = "https://github.com/cjchew82/streamlit_resume.git"
DCV_PROJECT_KEYWORDS = "Python, CSS, Streamlit, Github, Visual Studio Code IDE"
DCV_PROJECT_DESCRIPTION = """
    - 📍 To build a personal digital resume using a Streamlit application.
    - 📍 Learning to connect Streamlit to a GitHub repository.
    - 📍 Improving skillsets in Python coding, Streamlit tools, etc.
    - 💡 In this mini project, the goal is to gain a lot of experience in Python coding. While I may not build the entire resume by writing all the code myself, completing and launching my own Digital Resume application in Streamlit is a significant achievement.
    """ 
# --------------------------------------
# st.set_page_config(page_title="Digital Resume | CJ Chew", page_icon="💼", layout="wide")

st.title("🔬 Personal Projects")
# --------------- HELPER FUNCTIONS -----------------------

def personal_project_section(PROJECT_TITLE,PROJECT_LINK,PROJECT_KEYWORDS,PROJECT_DESCRIPTION):

    st.subheader(f"[{PROJECT_TITLE}]({PROJECT_LINK})")
    st.write('---')
    st.write(f'''<span style="color:#f50057; font-size: 15;">**Keywords :**</span> {PROJECT_KEYWORDS}''', unsafe_allow_html=True)
    
    st.write(PROJECT_DESCRIPTION, unsafe_allow_html=True)
    st.write('\n')
# ----------- CSS, PDF & Profile Pic SETTINGS --------------

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# ------ HERO SECTION -----------

#------ Project 1 SECTION
personal_project_section(DCV_PROJECT_TITLE,DCV_PROJECT_LINK,DCV_PROJECT_KEYWORDS,DCV_PROJECT_DESCRIPTION)
with st.expander("**Preview :** "):
    st.image(DCV_PIC,width=1000)
st.write('----')

# #------ Project 4 SECTION
# personal_project_section(THREE_MODELS_PROJECT_TITLE,THREE_MODELS_PROJECT_LINK,THREE_MODELS_PROJECT_KEYWORDS,THREE_MODELS_PROJECT_STACK,THREE_MODELS_PROJECT_DESCRIPTION)
# with st.expander("**Preview of deliverables :** "):
#     st.image(THREE_MODELS_PIC,width=1000)
# st.write('----')

# Add footer
st.write('---')
st.write('© Chew Chuan Juen  |  Last updated: July 2024')

# Add sidebar text
st.sidebar.text("Created by 💕 CJ Chew")