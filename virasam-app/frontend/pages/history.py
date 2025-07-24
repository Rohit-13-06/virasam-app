import sys
import os
# Add project root to path to enable backend imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import streamlit as st
from backend.database import (
    query_history_data,
    save_history_question,
    save_history_ai_answer,
    save_history_contribution
)
from frontend.utils.ai_fallback import get_ai_response, get_fast_ai_response, get_comprehensive_ai_response, get_smart_ai_response
from frontend.utils.translation import translate_to_telugu

def _(txt):
    return translate_to_telugu(txt) if st.session_state.get("is_telugu", False) else txt

def show():
    st.header(_("Local History"))

    action = st.radio(
        _("Choose an option:"),
        [_("Ask / Search"), _("Contribute")],
        horizontal=True,
        key="history_action"
    )

    user_id = st.session_state.get("user_id", None)

    if action == _("Ask / Search"):
        st.subheader(_("Ask a Question About Local History"))
        
        question = st.text_input(_("Ask a question about Local History:"))
        
        # Add model selection option
        col1, col2 = st.columns([3, 1])
        with col2:
            model_choice = st.selectbox(
                _("Response Type:"),
                ["Smart", "Fast", "Detailed"],
                key="history_model_choice"
            )
        
        if st.button(_("Submit"), key="history_ask_submit") and question.strip():
            # 1. FIRST: Save question to history_questions table
            question_id = None
            with st.spinner(_("Saving your question...")):
                try:
                    question_records = save_history_question(user_id, question)
                    if question_records and len(question_records) > 0:
                        question_id = question_records[0].get("id")
                        st.success(f"✅ Question saved.")
                        
                        # Debug info
                        with st.expander("🔍 Question Details", expanded=False):
                            st.json(question_records[0])
                except Exception as e:
                    st.error(f"❌ Failed to save question: {e}")
                    print(f"Error saving question: {e}")

            # 2. SECOND: Search existing content in history_content table
            with st.spinner(_("Searching local history database...")):
                results = query_history_data(question)
            
            if results:
                st.write(_("📚 Results from local history database:"))
                for r in results:
                    title = r.get('title', 'No Title')
                    description = r.get('description', 'No Description')
                    
                    with st.container():
                        st.markdown(f"**{title}**")
                        st.write(description)
                        st.markdown("---")
            else:
                # 3. THIRD: Generate AI response if no database results
                st.info(_("📖 No database results found. Generating AI response..."))
                
                with st.spinner(_("Generating AI response...")):
                    try:
                        if model_choice == "Fast":
                            ai_answer = get_fast_ai_response(f"Local History context: {question}")
                        elif model_choice == "Detailed":
                            ai_answer = get_comprehensive_ai_response(f"Local History context: {question}")
                        else:  # Smart
                            ai_answer = get_smart_ai_response(f"Local History context: {question}")
                        
                        if ai_answer and not ai_answer.startswith("AI Error"):
                            st.success(_("🤖 AI Assistant response:"))
                            st.write(ai_answer)
                            
                            # 4. FOURTH: Save AI answer linked to the question
                            if question_id and ai_answer:
                                try:
                                    answer_records = save_history_ai_answer(question_id, ai_answer)
                                    if answer_records and len(answer_records) > 0:
                                        st.success("✅ AI answer saved.")
                                        
                                        # Debug info
                                        with st.expander("🔍 Answer Details", expanded=False):
                                            st.json(answer_records[0])
                                    else:
                                        st.warning("⚠️ AI answer may not have been saved properly")
                                except Exception as e:
                                    st.error(f"❌ Failed to save AI answer: {e}")
                                    print(f"Error saving AI answer: {e}")
                            else:
                                st.warning("⚠️ Cannot save AI answer - missing question ID or answer content")
                        else:
                            st.error(_("❌ Failed to generate AI response. Please try again."))
                            
                    except Exception as e:
                        st.error(f"❌ Error generating AI response: {e}")

    else:  # Contribute section
        st.subheader(_("Share Your Local History Knowledge"))
        
        # Show user info for contributions
        effective_user_id = user_id or st.session_state.get("username") or "anonymous"
        st.info(f"📝 Contributing as: **{effective_user_id}**")
        
        with st.form("history_contrib_form"):
            contrib_title = st.text_input(
                _("Title (optional):"),
                placeholder=_("Enter a title for your contribution...")
            )
            contrib_text = st.text_area(
                _("Share your local history knowledge:"),
                placeholder=_("Share historical events, landmarks, stories, or any local history knowledge..."),
                height=150
            )
            contrib_file = st.file_uploader(
                _("Upload media (optional):"), 
                type=["mp3", "wav", "jpg", "png", "mp4"],
                help=_("Upload images, audio, or video related to your history contribution")
            )
            submitted = st.form_submit_button(_("📤 Submit Contribution"))
            
            if submitted and contrib_text.strip():
                with st.spinner(_("💾 Saving your contribution...")):
                    try:
                        result = save_history_contribution(
                            user_id=effective_user_id,
                            title=contrib_title.strip() if contrib_title else "History Contribution",
                            description=contrib_text.strip(),
                            media_url=None  # TODO: Implement file upload to Supabase Storage
                        )
                        
                        if result and len(result) > 0:
                            st.success(_("✅ Thank you! Your contribution has been saved !"))
                            st.balloons()
                            
                            # Show saved contribution details
                            saved_record = result[0] if isinstance(result, list) else result
                            
                            with st.expander("📄 Your Saved Contribution", expanded=True):
                                st.write(f"**ID:** {saved_record.get('id', 'N/A')}")
                                st.write(f"**Title:** {saved_record.get('title', 'N/A')}")
                                st.write(f"**Description:** {saved_record.get('description', 'N/A')[:100]}...")
                                st.write(f"**Saved at:** {saved_record.get('created_at', 'N/A')}")
                            
                            # Show success metrics
                            st.info("🎉 Your contribution will help preserve local history for future generations!")
                            
                        else:
                            st.error(_("❌ Failed to save your contribution. Please try again."))
                            st.write("**Possible issues:**")
                            st.write("- Database connection problem")
                            st.write("- Permission/authentication issue")
                            st.write("- Data validation error")
                            
                    except Exception as e:
                        st.error(_("❌ Error saving your contribution. Please try again."))
                        st.error(f"**Error Details:** {str(e)}")
                        
                        # Show technical details for debugging
                        with st.expander("🔧 Technical Details", expanded=False):
                            import traceback
                            st.code(traceback.format_exc())
                            
            elif submitted:
                st.warning(_("⚠️ Please enter some content before submitting your contribution."))
        
        # Additional help section
        with st.expander("💡 Contribution Tips", expanded=False):
            st.write("**What to share:**")
            st.write("- Historical landmarks and monuments")
            st.write("- Founding stories and early settlements")
            st.write("- Significant local events and dates")
            st.write("- Local heroes and important figures")
            st.write("- Migration and settlement patterns")
            st.write("- Historical photographs and documents")
            
            st.write("**Tips for better contributions:**")
            st.write("- Include specific dates and locations")
            st.write("- Mention sources when possible")
            st.write("- Provide historical context")
            st.write("- Be respectful of all communities")

    # Database status section
    st.markdown("---")
    with st.expander("🔧 Database Information", expanded=False):
        st.write("**Database Tables Used:**")
        st.write("- `history_questions` - Stores user questions")
        st.write("- `history_content` - Pre-populated history content for search")
        st.write("- `history_answers` - AI-generated answers linked to questions")
        st.write("- `history_contributions` - User-submitted history knowledge")
        
        # Test database connection
        if st.button("Test Database Connection", key="test_history_db"):
            try:
                from backend.database import supabase
                
                # Test query
                test_response = supabase.from_("history_content").select("*").limit(3).execute()
                
                if test_response.data:
                    st.success("✅ Database connection successful!")
                    st.write(f"Found {len(test_response.data)} records.")
                else:
                    st.info("Database connected but history_content table is empty")
                    
            except Exception as e:
                st.error(f"❌ Database connection failed: {e}")

# This allows the file to be run standalone for testing
if __name__ == "__main__":
    show()
