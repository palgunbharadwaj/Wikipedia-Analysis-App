# Wikipedia Analysis App

A web application that generates interactive word clouds from Wikipedia category articles, with selectable color palettes and a sidebar of raw word frequencies.

## Features
- **Analyze Wikipedia Categories:** Enter a Wikipedia category (e.g. `Artificial_intelligence`) and generate a word cloud from all articles in that category.
- **Color Palette Selection:** Choose from multiple color palettes to customize your word cloud.
- **Raw Frequency Sidebar:** View a sidebar with the raw word frequency counts for the selected category.
- **Caching:** Speeds up repeated analysis by caching Wikipedia API responses.
- **Modern UI:** Built with D3.js for interactive, visually appealing word clouds.

## Usage
1. **Install dependencies:**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   pip install -r requirements.txt
   ```
2. **Run the app:**
   ```sh
   python app.py
   ```
3. **Open your browser:**
   Go to [http://localhost:5000](http://localhost:5000)
4. **Enter a Wikipedia category** and click "Generate Word Cloud".

## Project Structure
- `app.py` — Flask backend serving API endpoints and static files
- `index.html` — Main frontend (D3.js, palette selector, sidebar)
- `color_palette.py` — Color palette definitions and palette API
- `min_wikipedia_word_freq.py` — Wikipedia fetching, word frequency, and caching logic
- `requirements.txt` — Python dependencies
- `cache/` — Stores cached Wikipedia API responses (ignored by git)
- `venv/` — Python virtual environment (ignored by git)

## Notes
- The app uses only files in the project root (no `templates/` or `static/` folders).
- The virtual environment and cache are not tracked by git (`.gitignore` is set up).
- Supports large Wikipedia categories by fetching up to 500 articles if needed.

## Example Categories
- `Machine_learning_algorithms`
- `Physics`

> **Note:** Not all Wikipedia categories will work. The app only analyzes categories that contain direct articles, not just subcategories. If you get "No data found," try a more specific category.

## License
MIT License (see LICENSE file)
