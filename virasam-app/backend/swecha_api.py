import requests

BASE_URL = "https://api.swecha-corpus.org"  # Update as appropriate

def fetch_content(category, language=None):
    params = {"category": category}
    if language:
        params["language"] = language
    resp = requests.get(f"{BASE_URL}/content", params=params)
    if resp.status_code == 200:
        return resp.json()
    return []

def post_content(data, auth_token=None):
    headers = {"Authorization": f"Bearer {auth_token}"} if auth_token else {}
    resp = requests.post(f"{BASE_URL}/contribute", json=data, headers=headers)
    return resp.status_code == 201
