from pathlib import Path
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image


# ------------ PATH SETTINGS ----------
current_dir = Path(__file__).parent.parent
css_file = current_dir / "styles" / "main.css"
tenthpin_PIC_PATH = current_dir / "assets" / "work" / "tenthpin" /"tenthpin.png"
deloitte_PIC_PATH = current_dir / "assets" / "work" /  "deloitte" / "deloitte.png"
epiuse_PIC_PATH = current_dir / "assets" / "work" /  "epiuse" / "epiuse.png"
vs_PIC_PATH = current_dir / "assets" / "work" /  "vs" / "flex.png"
preview_tenthpin = [f"""{current_dir}/assets/work/tenthpin/{example}""" for example in ['NDpaper.png','fapon.png','virogin.png','mindray.png','logo.png']]
preview_deloitte = [f"""{current_dir}/assets/work/deloitte/{example}""" for example in ['Top_Glove.png','deloitte.png','unicharm.png','prefchem.png']]
preview_epiuse = [f"""{current_dir}/assets/work/epiuse/{example}""" for example in ['Sunway.png','nestle.png','mas.png']]
preview_vs = [f"""{current_dir}/assets/work/vs/{example}""" for example in ['mcd.png','pmm.png','lgb.png','berjaya.png']]

# ------------ CONSTANTS ----------
PAGE_TITLE = "Work Experiences | CJ Chew"
PAGE_ICON = "💼"

#-------- WORK EXPERIENCE CONTENT----------
COMMUN_ROLE1  = "SAP SuccessFactors Senior Consultant"
tenthpin_PIC  = Image.open(tenthpin_PIC_PATH)
tenthpin_COMPANY = "Tenthpin Management Consultants Sdn Bhd"
tenthpin_PERIOD = "12/2021 - Present"
tenthpin_DESCRIPTION = """
    - ►  <span style="color:#f50057; font-size: 15;">Responsibilities : </span>
        - 🟪 During the kick-off meeting, I prepare proposals and demonstrate the system to the client. 
        - 🟪 Additionally, I guide and collaborate closely with team members to ensure successful project delivery. 
        - 🟪 My experience in the full project implementation cycle includes facilitating workshops to gather requirements. 
        - 🟪 Conducting system reviews and iterations, performing configuration testing, delivering train-the-trainer sessions, conducting user acceptance tests, and providing go-live project support.
    - ►  <span style="color:#f50057; font-size: 15;">Client Support : </span>
        - 🟩 Project: Clover Biopharmaceuticals (EC, RCM, and ONB 2.0 Oversea UK and US implementation)
        - 🟩 Project: Mindray (EC Integration and SF full suite system support)
        - 🟩 Project: Clover Biopharmaceuticals (Compensation new worksheet implementation)
        - 🟩 Project: SAP HCM Malaysia Payroll (Project Manager role)
    """
    
COMMUN_ROLE2  = "SAP SuccessFactors Consultant"    
deloitte_PIC  = Image.open(deloitte_PIC_PATH)
deloitte_COMPANY = "DC Technology Sdn Bhd"
deloitte_PERIOD = "10/2018 - 11/2021"
deloitte_DESCRIPTION = """
    - ►  <span style="color:#f50057; font-size: 15;">Responsibilities : </span>
        - 🟪 As a functional consultant, I participate in proposal preparation and deliver system demonstrations to clients during the kick-off meeting. 
        - 🟪 My experience in the full project implementation cycle includes facilitating workshops to gather requirements.
        - 🟪 Conducting system reviews and iterations, performing configuration testing, delivering train-the-trainer sessions, conducting user acceptance tests, and providing go-live project support.
    - ►  <span style="color:#f50057; font-size: 15;">Client Support : </span>
        - 🟩 Project: Malaysia’s largest glove production manufacturing. (LMS, Recruiting, On-boarding)
        - 🟩 Project: Deloitte SEA (Recruiting)
        - 🟩 Project: Japan collaboration Baby Care production Taiwan and Australia (EC, LMS, PMGM and SP) 
        - 🟩 Project: Petrochemical, Refinery and Cracker Company (LMS, Onboarding 2.0)
    """ 

COMMUN_ROLE3  = "SAP HCM & SuccessFactors Consultant"
epiuse_PIC  = Image.open(epiuse_PIC_PATH)
epiuse_COMPANY = "EPI-USE Malaysia Sdn Bhd"
epiuse_PERIOD = "07/2017 - 09/2018"
epiuse_DESCRIPTION = """
        EPI-USE, the world’s largest and most experienced independent SAP HCM specialist, has emerged as a leader in designing, building, integrating, and implementing Cloud-based, hybrid, and on-premises SAP-based solutions for large, complex multinational corporations. 
        My responsibilities as a consultant are to provide a solution, support service in any project been assigned by management. I was worked on a few projects during EPI-USE which is SuccessFactors LMS implementation in Sunway Berhad, SuccessFactors Employee Center testing release for Corning (US company). Last year just implemented SAP LSO for one of the Dubai customers.
        Besides project implementation tasks. I also handled SF LMS customer support for MAB (Malaysia Airlines Berhad) and SAP HCM support for Nestle worldwide (excluding the US and Europe region).
        """
        
COMMUN_ROLE4  = "Project Analyst"
vs_PIC  = Image.open(vs_PIC_PATH)
vs_COMPANY = "Visual Solutions Sdn Bhd"
vs_PERIOD = "08/2012 - 07/2017"
vs_DESCRIPTION = """
    - ►  Visual Solutions is a leading human resources software company that is dedicated and focused entirely on developing and implementing its Human Resources System software called flexHR® which meets the growing demands of human resources practitioners.
    - ►  My responsibilities are Implementing the Human Resource Management System (HRMS), Employee Self Service (ESS) & Human Resource Strategy System (HRSS) Module implementation. To Ensure project delivery as per gap analysis, conduct module training & user acceptance test (UAT). Coordinates preparation internal and external reports through gathering, analyzing and summarizing data and information from the departments and plan manages and monitors minor projects from concepts through implementation
    - ►  <span style="color:#f50057; font-size: 15;">Client Support : </span>
        - 🟩 TESCO, 
        - 🟩 Berjaya Corp,
        - 🟩 Philip Morris, 
        - 🟩 Watson's, 
        - 🟩 Golden Archer Restaurant (McD), 
        - 🟩 Cycle & Carriage, etc.
    """ 
# --------------------------------------
# st.set_page_config(page_title="Digital Resume | CJ Chew", page_icon="💼", layout="wide")

st.title("💼 Working Experiences")
# --------------- HELPER FUNCTIONS -----------------------

def work_experience_section(PIC,ROLE,COMPANY,PERIOD,WORK_DESCRIPTION):

    st.image(PIC,width=150)
    st.write(f"**{ROLE} | {COMPANY}**")
    st.write(f"{PERIOD}")
    st.write(WORK_DESCRIPTION, unsafe_allow_html=True)
    

# ----------- CSS, PDF & Profile Pic SETTINGS --------------

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


# ------ HERO SECTION -----------

# ------ tenthpin SECTION ---------
work_experience_section(tenthpin_PIC,COMMUN_ROLE1,tenthpin_COMPANY,tenthpin_PERIOD,tenthpin_DESCRIPTION)
images = [Image.open(image) for image in preview_tenthpin]
image_captions = ['ND Paper Malaysia','Fapon Biotech','Virogin','Mindray','Clover']
with st.expander("**Successful Client Project :** "):
    cols = st.columns(3,gap="large")
    for i,image in enumerate(images):
        with cols[i%3]:
            st.image(image,caption=image_captions[i],width=200)
st.write('----')

# ------ deloitte SECTION ---------
work_experience_section(deloitte_PIC,COMMUN_ROLE2,deloitte_COMPANY,deloitte_PERIOD,deloitte_DESCRIPTION)
images = [Image.open(image) for image in preview_deloitte]
image_captions = ['Top Glove Berhad' , 'Deloitte Shared Service','Unicharm Group' ,'PRefChem']
with st.expander("**Successful Client Project :** "):
    cols = st.columns(3,gap="large")
    for i,image in enumerate(images):
        with cols[i%3]:
            st.image(image,caption=image_captions[i],width=200)
st.write('----')

#------ epiuse SECTION
work_experience_section(epiuse_PIC,COMMUN_ROLE3,epiuse_COMPANY,epiuse_PERIOD,epiuse_DESCRIPTION)
images = [Image.open(image) for image in preview_epiuse]
image_captions = ['Sunway Berhad','Nestle APAC','Malaysia Airline']
with st.expander("**Successful Client Project :** "):
    cols = st.columns(3,gap="large")
    for i,image in enumerate(images):
        with cols[i%3]:
            st.image(image,caption=image_captions[i],width=200)
st.write('----')

#------ vs SECTION
work_experience_section(vs_PIC,COMMUN_ROLE4,vs_COMPANY,vs_PERIOD,vs_DESCRIPTION)
images = [Image.open(image) for image in preview_vs]
image_captions = ['Golden Archer Restaurant (McD)','Philip Morris Malaysia','LGB Group','Berjay Corp']
with st.expander("**Successful Client Project :** "):
    cols = st.columns(3,gap="large")
    for i,image in enumerate(images):
        with cols[i%3]:
            st.image(image,caption=image_captions[i],width=200)
            
# Add footer
st.write('---')
st.write('© Chew Chuan Juen  |  Last updated: July 2024')

# Add sidebar text
st.sidebar.text("Created by 💕 CJ Chew")