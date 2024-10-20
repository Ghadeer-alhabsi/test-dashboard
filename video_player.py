import streamlit as st

def display_video(playlist_id):
    st.markdown(f"""
    <div class="video-container">
        <iframe src="https://www.youtube.com/embed/{playlist_id}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
    """, unsafe_allow_html=True)