# frontend/utils/swecha_search.py

import os
import json
import re

# ---- Dummy example categories & corpus (replace with your real data-loading as needed) ----
CATEGORIES = {
    "folk tales": ["rabbit", "tortoise", "panchatantra", "story", "tale", "king", "animal"],
    "music": ["song", "singer", "folk music", "instrument"],
    "recipes": ["cook", "recipe", "cooking", "food", "dish"],
    "skills": ["weaving", "pottery", "farming", "craft"],
    "festivals": ["festival", "deepavali", "sankranti", "celebration", "harvest"],
    # add more as needed
}

# Simulate corpus (replace with DB or file loading if available)
# Each key = category, value = list of dicts with real content
SAMPLE_CORPUS = {
    "folk tales": [
        {"title": "The Clever Rabbit", "description": "A classic animal story."},
        {"title": "Panchatantra Tale: The Lion and the Rabbit", "description": "A story from the Panchatantra."},
    ],
    "music": [
        {"title": "Folk Song of Telangana", "description": "A beautiful local melody."},
    ],
    "recipes": [
        {"title": "How to Make Pulihora", "description": "Recipe for a tangy South Indian rice dish."},
    ],
    # add your real records here
}

def categorize_query(query):
    """Return the best-matched category for the query."""
    query_lower = query.lower()
    for category, keywords in CATEGORIES.items():
        for kw in keywords:
            if re.search(r"\b" + re.escape(kw) + r"\b", query_lower):
                return category
    return None

def fetch_content(category):
    """Return list of content dicts for the category."""
    if not category:
        return []
    # You can later load content from a DB or file here
    return SAMPLE_CORPUS.get(category, [])

# ---------- Optional: Direct fulltext search across all categories ----------
def search_fulltext(query):
    """Return labeled matches across all categories if no direct category found."""
    query_lower = query.lower()
    matches = []
    for cat, items in SAMPLE_CORPUS.items():
        for item in items:
            text = (item.get("title","") + " " + item.get("description","")).lower()
            if query_lower in text:
                matches.append((cat, item))
    return matches

# ------- Usage Example -------
if __name__ == "__main__":
    q = "Tell me a rabbit story"
    cat = categorize_query(q)
    print("Category:", cat)
    if cat:
        print("Results:", fetch_content(cat))
    else:
        print("No direct category; Fulltext:", search_fulltext(q))
