import streamlit as st
from frontend.utils.translation import translate_to_telugu

def show():
    is_telugu = st.session_state.get('is_telugu', False)

    header = "Community & Engagement"
    info = "- See top contributors\n- Join a mentorship/story circle (coming soon)\n- Voting and comment area (coming soon)"

    if is_telugu:
        header = translate_to_telugu(header)
        info = translate_to_telugu(info)

    st.header(header)
    st.write(info)
