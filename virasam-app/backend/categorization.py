import re

CATEGORIES = [
    "Folk Tales", "Music", "Recipes", "Skills",
    "Places", "Festivals", "Architecture", "Local History"
]

def categorize_query(query):
    query = query.lower()
    if re.search(r'song|music', query): return "Music"
    if re.search(r'recipe|cooking|food', query): return "Recipes"
    if re.search(r'folktale|story|legend', query): return "Folk Tales"
    if re.search(r'skill|craft|art', query): return "Skills"
    if re.search(r'festival|celebration', query): return "Festivals"
    if re.search(r'architecture|building', query): return "Architecture"
    if re.search(r'place|village|monument', query): return "Places"
    if re.search(r'history|heritage', query): return "Local History"
    return None
