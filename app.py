import os
import json
from flask import Flask, jsonify, render_template, request, send_file
from collections import Counter
from color_palette import get_all_color_palettes
from min_wikipedia_word_freq import get_category_members, get_page_content, process_text

app = Flask(__name__)

DEFAULT_CATEGORY = "Large_language_models"

@app.route("/")
def index():
    return send_file("index.html")

@app.route("/api/wordfreq")
def wordfreq():
    category = request.args.get("category", DEFAULT_CATEGORY)
    word_freq = load_cache(f"wordfreq_{category}")
    if word_freq is None:
        pages = get_category_members(category)
        counter = Counter()
        for title in pages:
            content = get_page_content(title)
            words = process_text(content)
            counter.update(words)
        word_freq = dict(counter)
        save_cache(f"wordfreq_{category}", word_freq)
    wc_data = [{"text": w, "size": f} for w, f in word_freq.items() if f > 1]
    return jsonify(wc_data)

@app.route("/api/palettes")
def palettes():
    palettes = get_all_color_palettes()
    return jsonify([
        {'name': p.name, 'colors': p.colors}
        for p in palettes
    ])

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

if __name__ == "__main__":
    app.run(debug=True)
