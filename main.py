import streamlit as st
from pages import profile, locations, home

# Load the CSS file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles.css")

# Sidebar Menu for Navigation (this should only be in `main.py`)
st.sidebar.title("Navigation")
menu_options = ["Home", "Profile", "Locations"]
selected_page = st.sidebar.selectbox("Select a page", menu_options)

# Page Navigation Logic
if selected_page == "Home":
    home.show()

elif selected_page == "Profile":
    profile.show()

elif selected_page == "Locations":
    locations.show()
