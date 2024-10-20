import streamlit as st
from video_player import display_video
from dots_display import display_dots
from controls import display_controls

# Define the content for the Locations page
def show():
    st.title("Locations Page")

    # Static location information (common for all depths)
    location_name = "Example Location"
    location_description = "This is a common description for the location."
    location_date = "Date: January 2024"
    #location_image = "path_to_common_location_image.jpg"  # Replace with the actual image path

    # Display location information
    st.write(f"## {location_name}")
    st.write("**Description:**", location_description)
    st.write("**Date:**", location_date)

    # Display location image (if available)
    #st.image(location_image, caption=location_name, use_column_width=True)

    # Initialize session state if not already done
    if 'selected_depth' not in st.session_state:
        st.session_state.selected_depth = 1
    if 'playlist_items' not in st.session_state:
        st.session_state.playlist_items = [
            "PLe0-g4IQhPY5-mZj_1RDxXdlHUwcGzsP3",
            "PLe0-g4IQhPY5VlnEmI9N-EFQlQMX6mxqR",
        ]
    if 'current_video_index' not in st.session_state:
        st.session_state.current_video_index = 0
    if 'is_playing' not in st.session_state:
        st.session_state.is_playing = False

    # Mapping depths to playlist IDs
    depth_to_playlist = {
        1: "PLe0-g4IQhPY5-mZj_1RDxXdlHUwcGzsP3",
        3: "PLe0-g4IQhPY5VlnEmI9N-EFQlQMX6mxqR",
        5: "PLe0-g4IQhPY4toWjE59UolzfXNs7qbsNM",
        8: "PLe0-g4IQhPY4aQYn_LJW93XAvCHhKVTHo",
        10: "PLe0-g4IQhPY6Zv6TCf-w1DVjR7BNatCs6"
    }

    # Get the playlist ID based on the selected depth
    playlist_id = depth_to_playlist.get(st.session_state.selected_depth, st.session_state.playlist_items[0])

    # Example function to retrieve playlist items from a playlist ID
    def get_playlist_items(playlist_id):
        if playlist_id == "PLe0-g4IQhPY5-mZj_1RDxXdlHUwcGzsP3":
            return [
                "https://www.youtube.com/watch?v=your_video_id_1",
                "https://www.youtube.com/watch?v=your_video_id_2"
            ]
        elif playlist_id == "PLe0-g4IQhPY5VlnEmI9N-EFQlQMX6mxqR":
            return [
                "https://www.youtube.com/watch?v=your_video_id_3",
                "https://www.youtube.com/watch?v=your_video_id_4"
            ]
        else:
            return []

    # Update the session state with the videos for the selected playlist
    st.session_state.playlist_items = get_playlist_items(playlist_id)

    # Display the video player
    display_video(playlist_id)

    # Depth selection buttons
    st.write("### Select Depth to View")
    depth_options = [1, 3, 5, 8, 10]
    cols = st.columns(len(depth_options))
    for i, depth in enumerate(depth_options):
        with cols[i]:
            if st.button(f"Depth {depth}"):
                st.session_state.selected_depth = depth

    # Display dots based on the selected depth
    display_dots(st.session_state.selected_depth)

    # Display the control buttons with the playlist items
    display_controls(st.session_state.playlist_items)
