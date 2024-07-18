from pathlib import Path

import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
import streamlit.components.v1 as components


# ------------ PATH SETTINGS ----------
current_dir = Path(__file__).parent.parent
css_file = current_dir / "styles" / "main.css"

# SAP_CERTIFICATION_PIC_PATH = current_dir / "assets" / "certifications" / "SF_EC.png"  # Add the new image path

# ------------ CONSTANTS ----------
PAGE_TITLE = "Certifications | CJ Chew"
PAGE_ICON = "📜"

#-------- Certifications CONTENT----------
SAP_CERTIFICATION_TITLE1 = "SAP Certified Associate - Implementation Consultant - SAP SuccessFactors Employee Central Core"
# SAP_CERTIFICATION_PIC = Image.open(SAP_CERTIFICATION_PIC_PATH)
SAP_CERTIFICATION_LINK1 = "https://www.credly.com/badges/a2464039-6ef2-4d9e-8421-7041b1580736/public_url"
SAP_CERTIFICATION_DESCRIPTION1 = """
- ✔ This certification validates that the candidate has the knowledge and skills to support and implment an <span style="color:#f50057; font-size: 15;">**SAP SuccessFactors Employee Central Core.**</span>
- ✔ It demonstrates the candidate's ability to perform administrative tasks for SAP SuccessFactors Employee Central, including implmentation, and system administration.
    """ 
SAP_CERTIFICATION_TITLE2 = "SAP Certified Associate - Implementation Consultant - SAP SuccessFactors Onboarding"
SAP_CERTIFICATION_LINK2 = "https://www.credly.com/badges/79c59b87-4b63-41ac-bd2b-a55c60b4224c/public_url"
SAP_CERTIFICATION_DESCRIPTION2 = """
- ✔ This certification validates that the candidate has the knowledge and skills to support and implment an <span style="color:#f50057; font-size: 15;">**SAP SuccessFactors Onboarding.**</span>
- ✔ It demonstrates the candidate's ability to perform administrative tasks for <span style="color:#f50057; font-size: 15;">**SAP SuccessFactors Onboarding**</span>, including implmentation, and system administration.
    """ 
    
SAP_CERTIFICATION_TITLE3 = "SAP Certified Associate - SAP SuccessFactors Recruiting: Candidate Experience"
SAP_CERTIFICATION_LINK3 = "https://www.credly.com/badges/412b8770-812e-4abd-8834-f2be3abe2806/public_url"
SAP_CERTIFICATION_DESCRIPTION3 = """
- ✔ This certification validates that the candidate has the knowledge and skills to support and implment an <span style="color:#f50057; font-size: 15;">**SAP SuccessFactors Recruiting: Candidate Experience.**</span>
- ✔ It demonstrates the candidate's ability to perform administrative tasks for <span style="color:#f50057; font-size: 15;">**SAP SuccessFactors Recruiting: Candidate Experience**</span>, including implmentation, and system administration.
    """ 
    
SAP_CERTIFICATION_TITLE4 = "SAP Certified Associate - SAP SuccessFactors Recruiting: Recruiter Experience"
SAP_CERTIFICATION_LINK4 = "https://www.credly.com/badges/203d02b1-33f9-4040-9011-b143663941f6/public_url"
SAP_CERTIFICATION_DESCRIPTION4 = """
- ✔ This certification validates that the candidate has the knowledge and skills to support and implment an <span style="color:#f50057; font-size: 15;">**SAP SuccessFactors Recruiting: Recruiter Experience.**</span>
- ✔ It demonstrates the candidate's ability to perform administrative tasks for <span style="color:#f50057; font-size: 15;">**SAP SuccessFactors Recruiting: Recruiter Experience**</span>, including implmentation, and system administration.
    """ 
    
SAP_CERTIFICATION_TITLE5 = "SAP Certified Associate - SAP SuccessFactors Learning Management"
SAP_CERTIFICATION_LINK5 = "https://www.credly.com/badges/919a2dd8-f54c-4f05-a9e1-07f15a1eba7f/public_url"
SAP_CERTIFICATION_DESCRIPTION5 = """
- ✔ This certification validates that the candidate has the knowledge and skills to support and implment an <span style="color:#f50057; font-size: 15;">**SAP SuccessFactors Learning Management.**</span>
- ✔ It demonstrates the candidate's ability to perform administrative tasks for <span style="color:#f50057; font-size: 15;">**SAP SuccessFactors Learning Management**</span>, including implmentation, and system administration.
    """ 
# --------------------------------------
# st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON,layout="wide")

st.title("📜 Certifications")
# --------------- HELPER FUNCTIONS -----------------------

# def certification_section(CERTIFICATION_TITLE,CERTIFICATION_LINK,CERTIFICATION_DESCRIPTION,CERTIFICATION_PIC):

#     st.subheader(f"[{CERTIFICATION_TITLE}]({CERTIFICATION_LINK})")
#     st.write(CERTIFICATION_DESCRIPTION, unsafe_allow_html=True)
#     with st.expander("Check Certification"):
#         st.image(CERTIFICATION_PIC,width=800)
#     st.write('----')
def certification_section(CERTIFICATION_TITLE,CERTIFICATION_LINK,CERTIFICATION_DESCRIPTION,CERTIFICATION_PIC=None, embed_code=None):
    st.subheader(f"[{CERTIFICATION_TITLE}]({CERTIFICATION_LINK})")
    st.write(CERTIFICATION_DESCRIPTION, unsafe_allow_html=True)
    with st.expander("Check Certification"):
        if CERTIFICATION_PIC:
            st.image(CERTIFICATION_PIC, width=800)
        if embed_code:
            components.html(embed_code)
    st.write('----')
# ----------- CSS, PDF & Profile Pic SETTINGS --------------

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


# ------ HERO SECTION -----------
credly_embed_code1 = '''
<div data-iframe-width="200" data-iframe-height="300" data-share-badge-id="a2464039-6ef2-4d9e-8421-7041b1580736" data-share-badge-host="https://www.credly.com"></div><script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>
'''
credly_embed_code2 = '''
<div data-iframe-width="200" data-iframe-height="300" data-share-badge-id="79c59b87-4b63-41ac-bd2b-a55c60b4224c" data-share-badge-host="https://www.credly.com"></div><script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>
'''
credly_embed_code3 = '''
<div data-iframe-width="200" data-iframe-height="300" data-share-badge-id="412b8770-812e-4abd-8834-f2be3abe2806" data-share-badge-host="https://www.credly.com"></div><script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>
'''
credly_embed_code4 = '''
<div data-iframe-width="200" data-iframe-height="300" data-share-badge-id="203d02b1-33f9-4040-9011-b143663941f6" data-share-badge-host="https://www.credly.com"></div><script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>
'''
credly_embed_code5 = '''
<div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="919a2dd8-f54c-4f05-a9e1-07f15a1eba7f" data-share-badge-host="https://www.credly.com"></div><script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>
'''

certification_section(SAP_CERTIFICATION_TITLE1, SAP_CERTIFICATION_LINK1, SAP_CERTIFICATION_DESCRIPTION1, embed_code=credly_embed_code1)

certification_section(SAP_CERTIFICATION_TITLE2, SAP_CERTIFICATION_LINK2, SAP_CERTIFICATION_DESCRIPTION2, embed_code=credly_embed_code2)

certification_section(SAP_CERTIFICATION_TITLE3, SAP_CERTIFICATION_LINK3, SAP_CERTIFICATION_DESCRIPTION3, embed_code=credly_embed_code3)

certification_section(SAP_CERTIFICATION_TITLE4, SAP_CERTIFICATION_LINK4, SAP_CERTIFICATION_DESCRIPTION4, embed_code=credly_embed_code4)

certification_section(SAP_CERTIFICATION_TITLE5, SAP_CERTIFICATION_LINK5, SAP_CERTIFICATION_DESCRIPTION5, embed_code=credly_embed_code5)