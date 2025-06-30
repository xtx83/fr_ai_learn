# utils/cleaner.py
import re

def clean_text(text):
    """
    Basic cleanup for raw transcript text.
    Removes filler sounds, unwanted punctuation, extra spaces.
    """
    fillers = ["euh", "bah", "bon", "ben"]
    text = text.lower()

    # Remove filler words
    for word in fillers:
        text = re.sub(rf"\\b{word}\\b", "", text)

    # Remove punctuation except apostrophes
    text = re.sub(r"[.,!?;:\\\"()\\[\\]{}]", " ", text)

    # Collapse multiple spaces
    text = re.sub(r"\\s+", " ", text).strip()
    return text
