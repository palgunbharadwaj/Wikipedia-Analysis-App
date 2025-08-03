import sys
import requests
import re
import os
import json
from collections import Counter

# Minimal English stopwords list
STOPWORDS = set('''a about above after again against all am an and any are aren't as at be because been before being below between both but by can't cannot could couldn't did didn't do does doesn't doing don't down during each few for from further had hadn't has hasn't have haven't having he he'd he'll he's her here here's hers herself him himself his how how's i i'd i'll i'm i've if in into is isn't it it's its itself let's me more most mustn't my myself no nor not of off on once only or other ought our ours ourselves out over own same shan't she she'd she'll she's should shouldn't so some such than that that's the their theirs them themselves then there there's these they they'd they'll they're they've this those through to too under until up very was wasn't we we'd we'll we're we've were weren't what what's when when's where where's which while who who's whom why why's with won't would wouldn't you you'd you'll you're you've your yours yourself yourselves'''.split())

def get_cache_path(category, cache_dir="cache"):
    os.makedirs(cache_dir, exist_ok=True)
    safe_category = category.replace("/", "_").replace(" ", "_")
    return os.path.join(cache_dir, f"{safe_category}.json")

def load_cache(category, cache_dir="cache"):
    path = get_cache_path(category, cache_dir)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return None

def save_cache(category, data, cache_dir="cache"):
    path = get_cache_path(category, cache_dir)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# Minimal English stopwords list
STOPWORDS = set('''a about above after again against all am an and any are aren't as at be because been before being below between both but by can't cannot could couldn't did didn't do does doesn't doing don't down during each few for from further had hadn't has hasn't have haven't having he he'd he'll he's her here here's hers herself him himself his how how's i i'd i'll i'm i've if in into is isn't it it's its itself let's me more most mustn't my myself no nor not of off on once only or other ought our ours ourselves out over own same shan't she she'd she'll she's should shouldn't so some such than that that's the their theirs them themselves then there there's these they they'd they'll they're they've this those through to too under until up very was wasn't we we'd we'll we're we've were weren't what what's when when's where where's which while who who's whom why why's with won't would wouldn't you you'd you'll you're you've your yours yourself yourselves'''.split())

def get_category_members(category, max_pages=200):
    # Try cache first
    cached = load_cache(category)
    if cached:
        print(f"Loaded {len(cached)} pages from cache.")
        return cached[:max_pages]
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "categorymembers",
        "cmtitle": f"Category:{category}",
        "cmlimit": str(max_pages),
        "cmtype": "page"
    }
    r = requests.get(url, params=params, timeout=30)
    data = r.json()
    if 'query' in data and 'categorymembers' in data['query']:
        titles = [page['title'] for page in data['query']['categorymembers']]
        if titles:
            save_cache(category, titles)
            return titles[:max_pages]
    # Fallback: try with more pages if no results
    params["cmlimit"] = "500"
    r = requests.get(url, params=params, timeout=30)
    data = r.json()
    if 'query' in data and 'categorymembers' in data['query']:
        titles = [page['title'] for page in data['query']['categorymembers']]
        if titles:
            save_cache(category, titles)
            return titles[:500]
    return []

def get_page_content(title):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "extracts",
        "explaintext": True,
        "exsectionformat": "plain"
    }
    r = requests.get(url, params=params, timeout=30)
    data = r.json()
    page = next(iter(data['query']['pages'].values()))
    return page.get('extract', '')

def process_text(text):
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    return [w for w in words if w not in STOPWORDS]

def main():
    category = sys.argv[1] if len(sys.argv) > 1 else "Large_language_models"
    print(f"Analyzing category: {category}")
    pages = get_category_members(category)
    print(f"Found {len(pages)} pages: {pages}")
    word_counter = Counter()
    for title in pages:
        print(f"Processing: {title}")
        content = get_page_content(title)
        words = process_text(content)
        word_counter.update(words)
    print("\nTop 20 most frequent non-common words:")
    for word, freq in word_counter.most_common(20):
        print(f"{word:20} {freq}")

if __name__ == "__main__":
    main()
