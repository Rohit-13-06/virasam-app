import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import streamlit as st
from frontend.utils.translation import translate_to_telugu
from backend.swecha_api import post_content
from backend.categorization import CATEGORIES

def show():
    is_telugu = st.session_state.get('is_telugu', False)

    header = "Contribute Content"
    if is_telugu:
        header = translate_to_telugu(header)
    st.header(header)

    # Form labels
    title_label = "Title"
    cat_label = "Category"
    desc_label = "Description"
    text_label = "Text Content"
    audio_label = "Audio (mp3/wav)"
    submit_label = "Submit"
    success_msg = "Contribution submitted successfully!"
    error_msg = "Submission failed. Please try again."

    if is_telugu:
        title_label = translate_to_telugu(title_label)
        cat_label = translate_to_telugu(cat_label)
        desc_label = translate_to_telugu(desc_label)
        text_label = translate_to_telugu(text_label)
        audio_label = translate_to_telugu(audio_label)
        submit_label = translate_to_telugu(submit_label)
        success_msg = translate_to_telugu(success_msg)
        error_msg = translate_to_telugu(error_msg)

    with st.form("contribution_form"):
        title = st.text_input(title_label)
        category = st.selectbox(cat_label, CATEGORIES)
        description = st.text_area(desc_label)
        text_content = st.text_area(text_label)
        audio_file = st.file_uploader(audio_label, type=["mp3", "wav"])
        submitted = st.form_submit_button(submit_label)

    if submitted:
        data = {
            "title": title,
            "category": category,
            "description": description,
            "text": text_content,
        }
        if post_content(data):
            st.success(success_msg)
        else:
            st.error(error_msg)
