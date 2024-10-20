import streamlit as st
from video_player import display_video
from dots_display import display_dots
from controls import display_controls

# State management
st.session_state.playlist_items = ["PLe0-g4IQhPY5-mZj_1RDxXdlHUwcGzsP3", "PLe0-g4IQhPY5VlnEmI9N-EFQlQMX6mxqR"]

# Select depth
selected_depth = st.sidebar.selectbox("Select Depth (meters)", [1, 3, 5])

# Display the video player
playlist_id = st.session_state.playlist_items[0]  # Select based on the depth if needed
display_video(playlist_id)

# Display dots based on the selected depth
display_dots(selected_depth)

# Display the control buttons
display_controls()
