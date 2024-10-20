import streamlit as st

# Define your username and password
USERNAME = "ghadeer@ilabmarine.com"
PASSWORD = "123456"

# Initialize session state for logged-in status
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def show_login():
    # Create a login form
    st.write("# Login to Access Home Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Button to submit the login form
    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True  # Set login status to True
            st.success("Logged in successfully!")
            st.session_state.page = "home"  # Set the page state to home
        else:
            st.error("Incorrect username or password!")

def show_home_page():
    st.write("# Welcome to the Home Page")
    st.write("This is the content of the Home page.")

    # Example content that would be displayed after login
    external_url = 'https://industrial.ubidots.com/app/dashboards/public/dashboard/HZ15EbLdCK_ue-KywYWAQqezjyPGEmCMPdi3Y76Cbkg?nonavbar=true'
    st.components.v1.html(
        f'<iframe src="{external_url}" width="100%" height="600" frameborder="0"></iframe>',
        height=600
    )

# Check login status and page state to display the appropriate page
if st.session_state.logged_in and st.session_state.get("page") == "home":
    show_home_page()  # Show the home page if logged in
else:
    show_login()  # Show the login form if not logged in



