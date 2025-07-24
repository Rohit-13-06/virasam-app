from supabase import create_client
import os
import streamlit as st
import uuid

# Initialize Supabase client from Streamlit secrets or environment variables
SUPABASE_URL = st.secrets.get("SUPABASE_URL") or os.getenv("SUPABASE_URL")
SUPABASE_KEY = st.secrets.get("SUPABASE_ANON_KEY") or os.getenv("SUPABASE_ANON_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def convert_to_uuid(user_id):
    """
    Convert user_id to proper UUID format or None
    """
    if not user_id or user_id in ["anonymous", "None", None]:
        return None
    
    try:
        # If it's already a valid UUID string, return it
        uuid.UUID(str(user_id))
        return str(user_id)
    except ValueError:
        # If it's not a UUID, generate one based on the string
        # This ensures consistent UUIDs for the same username
        return str(uuid.uuid5(uuid.NAMESPACE_DNS, str(user_id)))

# ---------------- Folk Culture ------------------

def query_folk_data(question: str):
    try:
        response = supabase.from_("folk_content").select("*").ilike("description", f"%{question}%").execute()
        return response.data if response.data else []
    except Exception as e:
        print(f"Error querying folk data: {e}")
        return []

def save_folk_question(user_id, question_text):
    try:
        data = {
            "user_id": convert_to_uuid(user_id),
            "question": question_text
        }
        print(f"🔍 Saving folk question with data: {data}")
        response = supabase.from_("folk_questions").insert(data).execute()
        print(f"🔍 Folk question save response: {response.data}")
        return response.data if response.data else []
    except Exception as e:
        print(f"Error saving folk question: {e}")
        return []

def save_folk_ai_answer(question_id, answer_text):
    try:
        data = {
            "question_id": question_id,
            "answer": answer_text
        }
        print(f"🔍 Saving folk AI answer with data: {data}")
        response = supabase.from_("folk_answers").insert(data).execute()
        print(f"🔍 Folk AI answer save response: {response.data}")
        return response.data if response.data else []
    except Exception as e:
        print(f"Error saving folk AI answer: {e}")
        return []

def save_folk_contribution(user_id, title, description, media_url=None):
    try:
        data = {
            "user_id": convert_to_uuid(user_id),
            "title": title,
            "description": description,
            "media_url": media_url
        }
        print(f"🔍 Saving folk contribution with data: {data}")
        response = supabase.from_("folk_contributions").insert(data).execute()
        print(f"🔍 Folk contribution save response: {response.data}")
        return response.data if response.data else []
    except Exception as e:
        print(f"Error saving folk contribution: {e}")
        import traceback
        traceback.print_exc()
        return []

# ---------------- Traditions ------------------

def query_tradition_data(question: str):
    try:
        response = supabase.from_("traditions_content").select("*").ilike("description", f"%{question}%").execute()
        return response.data if response.data else []
    except Exception as e:
        print(f"Error querying tradition data: {e}")
        return []

def save_tradition_question(user_id, question_text):
    try:
        data = {
            "user_id": convert_to_uuid(user_id),
            "question": question_text
        }
        response = supabase.from_("traditions_questions").insert(data).execute()
        return response.data if response.data else []
    except Exception as e:
        print(f"Error saving tradition question: {e}")
        return []

def save_tradition_ai_answer(question_id, answer_text):
    try:
        data = {
            "question_id": question_id,
            "answer": answer_text
        }
        response = supabase.from_("traditions_answers").insert(data).execute()
        return response.data if response.data else []
    except Exception as e:
        print(f"Error saving tradition AI answer: {e}")
        return []

def save_tradition_contribution(user_id, title, description, media_url=None):
    try:
        data = {
            "user_id": convert_to_uuid(user_id),
            "title": title,
            "description": description,
            "media_url": media_url
        }
        response = supabase.from_("traditions_contributions").insert(data).execute()
        return response.data if response.data else []
    except Exception as e:
        print(f"Error saving tradition contribution: {e}")
        return []

# ---------------- Local History ------------------

def query_history_data(question: str):
    try:
        response = supabase.from_("history_content").select("*").ilike("description", f"%{question}%").execute()
        return response.data if response.data else []
    except Exception as e:
        print(f"Error querying history data: {e}")
        return []

def save_history_question(user_id, question_text):
    try:
        data = {
            "user_id": convert_to_uuid(user_id),
            "question": question_text
        }
        response = supabase.from_("history_questions").insert(data).execute()
        return response.data if response.data else []
    except Exception as e:
        print(f"Error saving history question: {e}")
        return []

def save_history_ai_answer(question_id, answer_text):
    try:
        data = {
            "question_id": question_id,
            "answer": answer_text
        }
        response = supabase.from_("history_answers").insert(data).execute()
        return response.data if response.data else []
    except Exception as e:
        print(f"Error saving history AI answer: {e}")
        return []

def save_history_contribution(user_id, title, description, media_url=None):
    try:
        data = {
            "user_id": convert_to_uuid(user_id),
            "title": title,
            "description": description,
            "media_url": media_url
        }
        response = supabase.from_("history_contributions").insert(data).execute()
        return response.data if response.data else []
    except Exception as e:
        print(f"Error saving history contribution: {e}")
        return []

# ---------------- Recipes ------------------

def query_recipes_data(question: str):
    try:
        response = supabase.from_("recipes_content").select("*").ilike("description", f"%{question}%").execute()
        return response.data if response.data else []
    except Exception as e:
        print(f"Error querying recipes data: {e}")
        return []

def save_recipes_question(user_id, question_text):
    try:
        data = {
            "user_id": convert_to_uuid(user_id),
            "question": question_text
        }
        response = supabase.from_("recipes_questions").insert(data).execute()
        return response.data if response.data else []
    except Exception as e:
        print(f"Error saving recipes question: {e}")
        return []

def save_recipes_ai_answer(question_id, answer_text):
    try:
        data = {
            "question_id": question_id,
            "answer": answer_text
        }
        response = supabase.from_("recipes_answers").insert(data).execute()
        return response.data if response.data else []
    except Exception as e:
        print(f"Error saving recipes AI answer: {e}")
        return []

def save_recipes_contribution(user_id, title, description, media_url=None):
    try:
        data = {
            "user_id": convert_to_uuid(user_id),
            "title": title,
            "description": description,
            "media_url": media_url
        }
        response = supabase.from_("recipes_contributions").insert(data).execute()
        return response.data if response.data else []
    except Exception as e:
        print(f"Error saving recipes contribution: {e}")
        return []
