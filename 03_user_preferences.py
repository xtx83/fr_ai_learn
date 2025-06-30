# scripts/03_user_preferences.py
import json
import os

def get_user_preferences():
    print("Let's set up your French learning media preferences.")
    
    genres = input("Enter your favorite genres (comma-separated, e.g. drama,comedy,documentary): ")
    formats = input("Preferred formats (e.g. podcast, YouTube, TV, article): ")
    target_level = input("Your current French level (e.g. A1, B2, C1): ")
    max_length = input("Max content length (in minutes, or type 'any'): ")

    prefs = {
        "genres": [g.strip() for g in genres.split(',')],
        "formats": [f.strip() for f in formats.split(',')],
        "target_level": target_level.strip(),
        "max_length": max_length.strip()
    }

    os.makedirs("config", exist_ok=True)
    with open("config/user_preferences.json", "w") as f:
        json.dump(prefs, f, indent=2)

    print("Preferences saved to config/user_preferences.json")

if __name__ == "__main__":
    get_user_preferences()
