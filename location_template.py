import streamlit as st
from video_player import display_video
from dots_display import display_dots

def display_location_details(location_name, location_description, location_date, depths_mapping):
    st.markdown(f"""
    <div class="location-details">
        <h3 class="location-name">{location_name}</h3>
        <p class="location-description"><strong>Description:</strong> {location_description}</p>
        <p class="location-date"><strong>Date:</strong> {location_date}</p>
         <p class="location-date"><strong>Date:</strong> {location_date}</p>
          <p class="location-date"><strong>Date:</strong> {location_date}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
    .depth-buttons {
        margin-top: 20px;
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
    }
    .depth-buttons button {
        background-color: #004466;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
        margin: 5px;
        transition: background-color 0.3s, transform 0.3s;
    }
    .depth-buttons button:hover {
        background-color: #006699;
        transform: scale(1.05);
    }
    .depth-buttons button:active {
        background-color: #003d5c;
    }
    </style>
    """, unsafe_allow_html=True)

    # Initialize session state if not already done
    if 'selected_depth' not in st.session_state:
        st.session_state.selected_depth = 1

    # Depth selection buttons with styling
    st.markdown('<div class="depth-buttons" >', unsafe_allow_html=True)
    depth_options = list(depths_mapping.keys())
    cols = st.columns(len(depth_options))
    for i, depth in enumerate(depth_options):
        with cols[i]:
            if st.button(f"Depth {depth}", key=f"depth_{depth}"):
                st.session_state.selected_depth = depth
    st.markdown('</div>', unsafe_allow_html=True)

    # Get the playlist ID for the selected depth
    playlist_id = depths_mapping.get(st.session_state.selected_depth)
    st.write(f"Displaying video for Depth {st.session_state.selected_depth}")

    # Display video and other details
    display_video(playlist_id)
    display_dots(st.session_state.selected_depth)
