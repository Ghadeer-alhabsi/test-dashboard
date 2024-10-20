import streamlit as st
from location_template import display_location_details

# Define location data as dictionaries
location_data = {
    "Location 1": {
        "name": "Location 1",
        "description": "Description for Location 1.",
        "date": "Date: January 2024",
        "depths_mapping": {
            1: "PLe0-g4IQhPY5-mZj_1RDxXdlHUwcGzsP3",
            2: "PLe0-g4IQhPY5VlnEmI9N-EFQlQMX6mxqR",
            3: "PLe0-g4IQhPY5VlnEmI9N-EFQlQMX6mxqR",
            4: "PLe0-g4IQhPY5VlnEmI9N-EFQlQMX6mxqR",
        }
    },
    "Location 2": {
        "name": "Location 2",
        "description": "Description for Location 2.",
        "date": "Date: February 2024",
        "depths_mapping": {
            1: "PLe0-g4IQhPY5-mZj_1RDxXdlHUwcGzsP3",
            5: "PLe0-g4IQhPY4toWjE59UolzfXNs7qbsNM",
            4: "PLe0-g4IQhPY4toWjE59UolzfXNs7qbsNM",
            3: "PLe0-g4IQhPY4toWjE59UolzfXNs7qbsNM",
            6: "PLe0-g4IQhPY4toWjE59UolzfXNs7qbsNM",
        }
    }
}

# Custom CSS
st.markdown("""
    <style>
    body {
        background-color: #ffffff; /* Set background color to white */
    }
    .location-details {
        background-color: #f0f8ff; /* Adjust as needed */
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .location-name {
        font-size: 26px;
        font-weight: bold;
        color: #004466;
    }
    .location-description, .location-date {
        font-size: 18px;
        color: #333;
    }
    .video-container iframe {
        border-radius: 10px;
        width: 100%;
        height: 400px; /* Adjust height as needed */
    }
    </style>
    """, unsafe_allow_html=True)

# Main page logic
def show():
    # Your main logic here
    selected_location = st.selectbox("Select a location", list(location_data.keys()))
    location = location_data[selected_location]
    display_location_details(location["name"], location["description"], location["date"], location["depths_mapping"])

# Run the show function to display the page
if __name__ == "__main__":
    show()
