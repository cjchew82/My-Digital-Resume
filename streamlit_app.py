import streamlit as st

# --- PAGE SETUP ---
about_page = st.Page(
    "views/1_About_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
education_page = st.Page(
    "views/2_Education_Background.py",
    title="Education Background",
    icon=":material/school:",
)
working_page = st.Page(
    "views/3_Working_Experiences.py",
    title="Working Experiences",
    icon=":material/business_center:",
)
project_page = st.Page(
    "views/4_Personal_Projects.py",
    title="Personal Projects",
    icon=":material/exoeriment:",
)
certification_page = st.Page(
    "views/5_Certifications.py",
    title="Certifications",
    icon=":material/license:",
)

# --- NEVIGATION SETUP ---
pg = st.navigation(pages=[about_page, education_page, working_page, 
                          project_page, certification_page])

st.logo("assets/icons8-menu-240.png")
st.sidebar.text("Created by 💕 CJ Chew")

pg.run