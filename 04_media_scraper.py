# scripts/04_media_scraper.py

import json
import pandas as pd
import os
import random

# Simulated media source (in a real-world case, you'd use APIs or BeautifulSoup)
SIMULATED_MEDIA_POOL = [
    {"title": "Apprendre le français avec Netflix", "genre": "drama", "format": "YouTube", "duration_min": 12, "url": "https://youtube.com/french-netflix"},
    {"title": "Podcast: Le français quotidien", "genre": "documentary", "format": "podcast", "duration_min": 25, "url": "https://podcast.fr/french-daily"},
    {"title": "Les actualités en français", "genre": "news", "format": "article", "duration_min": 5, "url": "https://lemonde.fr/news"},
    {"title": "Sketch comique français", "genre": "comedy", "format": "YouTube", "duration_min": 8, "url": "https://youtube.com/sketchfr"},
    {"title": "Documentaire: Histoire de la France", "genre": "documentary", "format": "TV", "duration_min": 50, "url": "https://arte.tv/histoire"},
    {"title": "Lecture audio: Le Petit Prince", "genre": "literature", "format": "podcast", "duration_min": 30, "url": "https://audiobooks.fr/petitprince"}
]

def load_preferences():
    with open("config/user_preferences.json", "r") as f:
        return json.load(f)

def filter_media(prefs):
    filtered = []
    for item in SIMULATED_MEDIA_POOL:
        if item["genre"] in prefs["genres"] and item["format"] in prefs["formats"]:
            if prefs["max_length"].lower() != "any":
                try:
                    if item["duration_min"] > int(prefs["max_length"]):
                        continue
                except ValueError:
                    pass  # sskip filtering if non-int was entered
            filtered.append(item)
    return filtered

def main():
    os.makedirs("media", exist_ok=True)
    prefs = load_preferences()
    media_matches = filter_media(prefs)

    df = pd.DataFrame(media_matches)
    df.to_csv("media/matched_content_links.csv", index=False)
    print(f"Saved {len(df)} media matches to media/matched_content_links.csv")

if __name__ == "__main__":
    main()
