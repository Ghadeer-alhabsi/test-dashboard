import streamlit as st

def display_controls(playlist_items):
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Previous Video"):
            st.session_state.video_index = max(st.session_state.get('video_index', 0) - 1, 0)
    with col2:
        st.button("Play", on_click=lambda: st.session_state.update(is_playing=True))
    with col3:
        if st.button("Next Video"):
            st.session_state.video_index = (st.session_state.get('video_index', 0) + 1) % len(playlist_items)
    
