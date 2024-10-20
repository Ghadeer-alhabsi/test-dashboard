import streamlit as st

# Example data; this would be passed in from the main file
dots_by_depth = {
    1: [],
    3: [{'position': 37, 'id': 2}],
    5: [{'position': 40, 'id': 2}],
    8: [],
    10: [{'position': 55, 'id': 2}],
}

# Initialize session state for selected depth if not already set
if "selected_depth" not in st.session_state:
    st.session_state.selected_depth = None

# Custom CSS for buttons
st.markdown("""
    <style>
    .depth-button {
        background-color: gray;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        margin: 5px;
        font-size: 16px;
        display: inline-block;
    }
    .depth-button.selected {
        background-color: red;
    }
    </style>
    """, unsafe_allow_html=True)

# Display function for crack positions at selected depth
def display_dots(selected_depth):
    dots = dots_by_depth.get(selected_depth, [])
    if dots:
        st.write(f"Cracks at Depth {selected_depth} meters:")
        for dot in dots:
            st.write(f"- Dot ID: {dot['id']} at Position: {dot['position']}%")
    else:
        st.write(f"No cracks at Depth {selected_depth} meters.")

# JavaScript function to update selected depth
js = """
    <script>
    function setDepth(depth) {
        document.querySelectorAll('.depth-button').forEach(button => {
            button.classList.remove('selected');
        });
        document.getElementById(`depth-${depth}`).classList.add('selected');
        window.parent.postMessage({depth: depth}, '*');
    }
    </script>
"""

st.markdown(js, unsafe_allow_html=True)



# Check if a depth is selected and update session state accordingly
selected_depth = st.session_state.get('depth')

if selected_depth is not None:
    st.session_state.selected_depth = selected_depth

# Display dots for the selected depth
if st.session_state.selected_depth is not None:
    display_dots(st.session_state.selected_depth)
