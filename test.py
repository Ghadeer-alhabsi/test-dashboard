import streamlit as st

# Function to display the content of each page
def home(search_query):
    st.write(f"Welcome to the Home Page! Search query: {search_query}")

def profile(search_query):
    st.write(f"This is the Profile Page. Search query: {search_query}")

def locations(search_query):
    st.write(f"Here are the Locations. Search query: {search_query}")

# Main function to control the app layout
def main():
    st.set_page_config(page_title="Simple Dashboard", layout="wide")
    
    # Add custom CSS to bring the title closer to the top and resize the search box
    st.markdown("""
        <style>
        .title {
            margin-top: -80px;  /* Adjust this value to move the title closer to the top */
            text-align: center;
        }
        .stTextInput>div>div>input {
            width: 50px;  /* Adjust the width of the search box */
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Display the title
    st.markdown("<h1 class='title'>My Dashboard</h1>", unsafe_allow_html=True)
    
    # Display the search box with custom width
    search_query = st.text_input("Search", "")
    
    # Menu for page selection
    page = st.sidebar.selectbox("Select a Page", ["Home", "Profile", "Locations"])
    
    # Page content based on menu selection
    if page == "Home":
        home(search_query)
    elif page == "Profile":
        profile(search_query)
    elif page == "Locations":
        locations(search_query)

if __name__ == "__main__":
    main()
