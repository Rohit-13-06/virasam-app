import streamlit as st
import os
import json
import bcrypt
from supabase import create_client

# Import your feature pages (make sure pages exist accordingly)
from pages.folk import show as show_folk
from pages.tradition import show as show_tradition
from pages.history import show as show_history
from pages.recipes import show as show_recipes

from pages.search import show as show_search
from pages.contribute import show as show_contribute
from pages.community import show as show_community

from frontend.utils.translation import translate_to_telugu
from frontend.utils.ai_fallback import get_ai_response  # Your AI wrapper

# Add fallback for experimental_rerun if not available
if not hasattr(st, "experimental_rerun"):
    def dummy_rerun():
        st.warning("Please refresh the page manually.")
    st.experimental_rerun = dummy_rerun

# --- Session State Initialization ---
if "auth_tab" not in st.session_state:
    st.session_state["auth_tab"] = "Login"
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""
if "name" not in st.session_state:
    st.session_state["name"] = ""
if "reg_email" not in st.session_state:
    st.session_state["reg_email"] = ""
if "user_id" not in st.session_state:
    st.session_state["user_id"] = None
if "is_telugu" not in st.session_state:
    st.session_state["is_telugu"] = False
if "selected_feature" not in st.session_state:
    st.session_state["selected_feature"] = None
if "current_action" not in st.session_state:
    st.session_state["current_action"] = None
if "show_user_info" not in st.session_state:
    st.session_state["show_user_info"] = False

# --- Supabase Client ---
@st.cache_resource
def get_supabase_client():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_ANON_KEY"]
    return create_client(url, key)

supabase = get_supabase_client()

USERS_FILE = os.path.join(os.path.dirname(__file__), 'utils', 'users.json')

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)

# --- Translation helper ---
def _(txt):
    return translate_to_telugu(txt) if st.session_state.get("is_telugu", False) else txt

# --- Authentication UI ---
def render_auth_ui():
    # Hide sidebar during authentication
    st.markdown("""
    <style>
        .css-1d391kg {display: none;}
        .css-1rs6os {display: none;}
        .css-17eq0hr {display: none;}
        [data-testid="stSidebar"] {display: none;}
        section[data-testid="stSidebar"] {display: none !important;}
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    st.markdown('<div class="brand-script">VIRASAM</div>', unsafe_allow_html=True)
    
    if st.session_state["auth_tab"] == "Login":
        st.markdown(f'<div class="form-title">{_("Sign in to your account")}</div>', unsafe_allow_html=True)
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_pw")
        st.markdown(f'<div class="forgot-pw"><a href="#">{_("Forgot password?")}</a></div>', unsafe_allow_html=True)
        login = st.button(_("Sign in"), key="login_btn")
        
        if login:
            users = load_users()
            user = users.get(username.strip())
            if user and bcrypt.checkpw(password.encode(), user["password"].encode()):
                st.session_state["authenticated"] = True
                st.session_state["username"] = username.strip()
                st.session_state["name"] = user["name"]
                st.session_state["reg_email"] = user.get("email", "")
                st.session_state["user_id"] = None  # Update if using real user IDs
                st.success(_("Welcome back!"))
                st.experimental_rerun()
            else:
                st.error(_("Invalid username or password."))
        
        st.markdown('<div class="divider">or</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="google-btn"><a href="#" target="_self">{_("Sign in with Google")}</a></div>', unsafe_allow_html=True)
        
        if st.button(_("Create Account"), key="goto_register"):
            st.session_state["auth_tab"] = "Register"
            st.experimental_rerun()
            
        st.markdown(f'<div class="auth-switch">{_("New to VIRASAM?")} <button class="switch-link" onclick="None">{_("Create Account")}</button></div>', unsafe_allow_html=True)
    
    else:  # Register tab
        st.markdown(f'<div class="form-title">{_("Create your VIRASAM account")}</div>', unsafe_allow_html=True)
        username = st.text_input("Username", key="reg_username", placeholder=_("Choose username"))
        name = st.text_input("Full Name", key="reg_name", placeholder=_("Full Name"))
        email = st.text_input("Email", key="reg_email", placeholder=_("Email Address"))
        pw1 = st.text_input("Password", type="password", key="reg_pw1", placeholder=_("Create password"))
        pw2 = st.text_input("Confirm Password", type="password", key="reg_pw2", placeholder=_("Confirm password"))
        reg = st.button(_("Create Account"), key="register_btn")
        
        if reg:
            users = load_users()
            if username.strip() in users:
                st.error(_("Username already exists."))
            elif pw1 != pw2:
                st.error(_("Passwords do not match."))
            elif not username.strip() or not name.strip() or not email.strip() or not pw1:
                st.error(_("All fields are required."))
            elif len(pw1) < 6:
                st.error(_("Password must be at least 6 characters."))
            else:
                pw_hash = bcrypt.hashpw(pw1.encode(), bcrypt.gensalt()).decode()
                users[username.strip()] = {"name": name.strip(), "email": email.strip(), "password": pw_hash}
                save_users(users)
                st.success(_("Account created successfully! Please log in."))
                st.session_state["auth_tab"] = "Login"
                st.experimental_rerun()
        
        st.markdown('<div class="divider">or</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="google-btn"><a href="#" target="_self">{_("Sign up with Google")}</a></div>', unsafe_allow_html=True)
        
        if st.button(_("Back to Sign In"), key="goto_login"):
            st.session_state["auth_tab"] = "Login"
            st.experimental_rerun()
            
        st.markdown(f'<div class="auth-switch">{_("Already have an account?")} <button class="switch-link" onclick="None">{_("Sign In")}</button></div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Check authentication and show login if not authenticated
if not st.session_state.get("authenticated", False):
    render_auth_ui()
    st.stop()

# --- AUTHENTICATED USER SECTION ---
# Show sidebar and main content only after authentication

# Language toggle in the top right
col1, col2 = st.columns([7, 2])
with col2:
    is_telugu = st.checkbox(
        "తెలుగు", value=st.session_state.get("is_telugu", False), key="language_toggle"
    )
    st.session_state["is_telugu"] = is_telugu

def home_page():
    header = _("VIRASAM: The Living Cultural Archive")
    tagline = _("Preserve, Share, and Discover Cultural Heritage")
    intro = _(
        "Welcome to Virasam, a community-driven platform where cultural traditions, stories, recipes, songs, and skills come alive. "
        "Connect with your heritage, share your knowledge, and explore the rich tapestry of human culture."
    )

    st.markdown(
        f'<h1 style="color:#FFFFFF; font-weight:800; text-shadow: 2px 2px 4px rgba(7,30,34,0.25); margin-bottom: 1rem;">{header}</h1>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<h3 style="color: #FFFFFF; font-weight:600; opacity:0.92; margin-bottom: 1rem;">{tagline}</h3>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<p style="color: #FFFFFF; font-size:1.08rem; opacity:0.8; line-height:1.56; margin-bottom: 2rem;">{intro}</p>',
        unsafe_allow_html=True,
    )

    features = [
        {"key": "folk", "icon": "🛕", "title": _("OUR FOLK")},
        {"key": "tradition", "icon": "📿", "title": _("OUR TRADITIONS")},
        {"key": "history", "icon": "📚", "title": _("LOCAL HISTORY")},
        {"key": "recipes", "icon": "🥗", "title": _("OUR RECIPES")},
    ]

    cols = st.columns(len(features))
    for i, card in enumerate(features):
        with cols[i]:
            st.markdown(
                f'<div style="font-size: 3rem; text-align: center;">{card["icon"]}</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                f'<h3 style="text-align:center;">{card["title"]}</h3>',
                unsafe_allow_html=True,
            )
            if st.button(_("Explore"), key=f'explore_{card["key"]}'):
                st.session_state["selected_feature"] = card["key"]
                st.session_state["current_action"] = None

def show_feature_page(feature_key):
    # Import feature pages locally to avoid unnecessary imports
    if feature_key == "folk":
        import pages.folk as feature
    elif feature_key == "tradition":
        import pages.tradition as feature
    elif feature_key == "history":
        import pages.history as feature
    elif feature_key == "recipes":
        import pages.recipes as feature
    else:
        st.error(_("Unknown feature selected."))
        return

    feature.show()

    if st.button(_("Back to Home")):
        st.session_state["selected_feature"] = None
        st.experimental_rerun()

# Sidebar navigation (only shown when authenticated)
page = st.sidebar.radio(
    _("Navigate"),
    [_("Home"), _("Search"), _("Contribute"), _("Community")]
)

# Main content routing
if page == _("Home"):
    if st.session_state.get("selected_feature") is not None:
        show_feature_page(st.session_state["selected_feature"])
    else:
        home_page()
elif page == _("Search"):
    show_search()
elif page == _("Contribute"):
    show_contribute()
elif page == _("Community"):
    show_community()

# Sidebar user info and logout (only shown when authenticated)
with st.sidebar:
    st.markdown("---")
    if st.session_state.get("show_user_info") is None:
        st.session_state["show_user_info"] = False

    user_clicked = st.button(
        _("Registration info"),
        key="user_info_btn",
        use_container_width=True,
    )

    st.markdown(
        f"""
        <div style='position:fixed;bottom:30px;width:210px;text-align:center;color:#f4c095; background:none; cursor:pointer; z-index:99;'>
            <span style='font-size:2em;'>👤</span><br>
            <strong>{st.session_state.get("name", "")}</strong>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if user_clicked:
        st.session_state["show_user_info"] = not st.session_state["show_user_info"]

    if st.session_state.get("show_user_info", False):
        st.markdown("<div style='height:32px;'></div>", unsafe_allow_html=True)
        with st.expander(_("Your Registration Info"), expanded=True):
            st.markdown(f"#### {_('Registration Details')}")
            st.markdown(f"**{_('Name')}:** {st.session_state.get('name', '-')}")
            st.markdown(f"**{_('Username')}:** {st.session_state.get('username', '-')}")
            st.markdown(f"**{_('Email')}:** {st.session_state.get('reg_email', '-')}")
    
    if st.button(_("Logout"), use_container_width=True):
        for k in ["authenticated", "username", "name", "reg_email", "user_id"]:
            st.session_state.pop(k, None)
        st.session_state["auth_tab"] = "Login"
        st.experimental_rerun()
