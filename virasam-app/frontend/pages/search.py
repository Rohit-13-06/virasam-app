# frontend/pages/2_Search.py

import streamlit as st
from frontend.utils.swecha_search import categorize_query, fetch_content
from frontend.utils.ai_fallback import get_ai_response

def show():
    st.title("Discover")
    st.write("Ask about culture, folk tales, recipes, music, skills, festivals, or anything from the Swecha corpus. If there is no match, the AI assistant will help!")

    user_query = st.text_input("What would you like to discover?")

    if st.button("Search") and user_query.strip():
        found = False

        # Try to find an answer in the curated Swecha corpus
        category = categorize_query(user_query)
        results = fetch_content(category) if category else []
        for result in results:
            # Simple substring match; customize as needed.
            if user_query.lower() in result.get("title", "").lower() or user_query.lower() in result.get("description", "").lower():
                st.success("Result from Swecha Corpus:")
                st.markdown(f"**{result['title']}**")
                st.write(result['description'])
                found = True
                break

        # Use Llama 3 (Ollama) fallback if no corpus match found
        if not found:
            st.info("No curated corpus result found. Asking the local AI assistant...")
            ai_answer = get_ai_response(user_query)
            st.markdown(f"**AI Answer:**\n{ai_answer}")
