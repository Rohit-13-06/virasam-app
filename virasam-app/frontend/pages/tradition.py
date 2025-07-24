import sys
import os
# Add project root to path to enable backend imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import streamlit as st
from backend.database import (
    query_tradition_data,
    save_tradition_question,
    save_tradition_ai_answer,
    save_tradition_contribution
)
from frontend.utils.ai_fallback import get_ai_response, get_fast_ai_response, get_comprehensive_ai_response, get_smart_ai_response
from frontend.utils.translation import translate_to_telugu

def _(txt):
    return translate_to_telugu(txt) if st.session_state.get("is_telugu", False) else txt

def show():
    st.header(_("Our Traditions"))

    action = st.radio(
        _("Choose an option:"),
        [_("Ask / Search"), _("Contribute")],
        horizontal=True,
        key="tradition_action"
    )

    user_id = st.session_state.get("user_id", None)

    if action == _("Ask / Search"):
        st.subheader(_("Ask a Question About Traditions"))
        
        question = st.text_input(_("Ask a question about Traditions:"))
        
        # Add model selection option
        col1, col2 = st.columns([3, 1])
        with col2:
            model_choice = st.selectbox(
                _("Response Type:"),
                ["Smart", "Fast", "Detailed"],
                key="tradition_model_choice"
            )
        
        if st.button(_("Submit"), key="tradition_ask_submit") and question.strip():
            # 1. FIRST: Save question to traditions_questions table
            question_id = None
            with st.spinner(_("Saving your question...")):
                try:
                    question_records = save_tradition_question(user_id, question)
                    if question_records and len(question_records) > 0:
                        question_id = question_records[0].get("id")
                        st.success(f"✅ Question saved.")
                        
                        # Debug info
                        with st.expander("🔍 Question Details", expanded=False):
                            st.json(question_records[0])
                except Exception as e:
                    st.error(f"❌ Failed to save question: {e}")
                    print(f"Error saving question: {e}")

            # 2. SECOND: Search existing content in traditions_content table
            with st.spinner(_("Searching traditions...")):
                results = query_tradition_data(question)
            
            if results:
                st.write(_("📚 Results :"))
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
                            ai_answer = get_fast_ai_response(f"Traditions context: {question}")
                        elif model_choice == "Detailed":
                            ai_answer = get_comprehensive_ai_response(f"Traditions context: {question}")
                        else:  # Smart
                            ai_answer = get_smart_ai_response(f"Traditions context: {question}")
                        
                        if ai_answer and not ai_answer.startswith("AI Error"):
                            st.success(_("🤖 AI Assistant response:"))
                            st.write(ai_answer)
                            
                            # 4. FOURTH: Save AI answer linked to the question
                            if question_id and ai_answer:
                                try:
                                    answer_records = save_tradition_ai_answer(question_id, ai_answer)
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
        st.subheader(_("Share Your Traditions Knowledge"))
        
        # Show user info for contributions
        effective_user_id = user_id or st.session_state.get("username") or "anonymous"
        st.info(f"📝 Contributing as: **{effective_user_id}**")
        
        with st.form("tradition_contrib_form"):
            contrib_title = st.text_input(
                _("Title (optional):"),
                placeholder=_("Enter a title for your contribution...")
            )
            contrib_text = st.text_area(
                _("Share your traditions knowledge:"),
                placeholder=_("Share traditional practices, customs, ceremonies, or any traditions knowledge..."),
                height=150
            )
            contrib_file = st.file_uploader(
                _("Upload media (optional):"), 
                type=["mp3", "wav", "jpg", "png", "mp4"],
                help=_("Upload images, audio, or video related to your traditions contribution")
            )
            submitted = st.form_submit_button(_("📤 Submit Contribution"))
            
            if submitted and contrib_text.strip():
                with st.spinner(_("💾 Saving your contribution...")):
                    try:
                        result = save_tradition_contribution(
                            user_id=effective_user_id,
                            title=contrib_title.strip() if contrib_title else "Traditions Contribution",
                            description=contrib_text.strip(),
                            media_url=None  # TODO: Implement file upload to Supabase Storage
                        )
                        
                        if result and len(result) > 0:
                            st.success(_("✅ Thank you! Your contribution has been saved!"))
                            st.balloons()
                            
                            # Show saved contribution details
                            saved_record = result[0] if isinstance(result, list) else result
                            
                            with st.expander("📄 Your Saved Contribution", expanded=True):
                                st.write(f"**ID:** {saved_record.get('id', 'N/A')}")
                                st.write(f"**Title:** {saved_record.get('title', 'N/A')}")
                                st.write(f"**Description:** {saved_record.get('description', 'N/A')[:100]}...")
                                st.write(f"**Saved at:** {saved_record.get('created_at', 'N/A')}")
                            
                            # Show success metrics
                            st.info("🎉 Your contribution will help preserve traditions for future generations!")
                            
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
            st.write("- Wedding ceremonies and customs")
            st.write("- Religious celebrations and rituals")
            st.write("- Seasonal festivals and traditions")
            st.write("- Coming of age ceremonies")
            st.write("- Family traditions and customs")
            st.write("- Traditional clothing and attire")
            
            st.write("**Tips for better contributions:**")
            st.write("- Be specific about the region or community")
            st.write("- Include context and background information")
            st.write("- Mention any variations you know")
            st.write("- Respect cultural sensitivity")

    # Database status section
    st.markdown("---")
    with st.expander("🔧 Database Information", expanded=False):
        st.write("**Database Tables Used:**")
        st.write("- `traditions_questions` - Stores user questions")
        st.write("- `traditions_content` - Pre-populated traditions content for search")
        st.write("- `traditions_answers` - AI-generated answers linked to questions")
        st.write("- `traditions_contributions` - User-submitted traditions knowledge")
        
        # Test database connection
        if st.button("Test Database Connection", key="test_tradition_db"):
            try:
                from backend.database import supabase
                
                # Test query
                test_response = supabase.from_("traditions_content").select("*").limit(3).execute()
                
                if test_response.data:
                    st.success("✅ Database connection successful!")
                    st.write(f"Found {len(test_response.data)} records in tradition")
                else:
                    st.info("Database connected but traditions_content table is empty")
                    
            except Exception as e:
                st.error(f"❌ Database connection failed: {e}")

# This allows the file to be run standalone for testing
if __name__ == "__main__":
    show()
