import json
import os

USERS_FILE = os.path.join(os.path.dirname(__file__), 'users.json')

def get_user_credentials():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, 'r') as f:
        return json.load(f)
