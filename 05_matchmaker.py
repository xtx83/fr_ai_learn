# scripts/05_matchmaker.py

import pandas as pd
import os

VOCAB_PATH = "../data/parsed_output/user_vocab_stats.csv"
MEDIA_PATH = "../media/matched_content_links.csv"
OUTPUT_PATH = "../media/matched_content_links_ranked.csv"

# Load vocab data
vocab_df = pd.read_csv(VOCAB_PATH)
target_words = set(vocab_df[vocab_df['difficulty'] >= 3]['word'])

# Load media content
media_df = pd.read_csv(MEDIA_PATH)

# Simulate content text (in reality, you'd scrape/transcribe it)
media_df['sample_text'] = [
    "Aujourd'hui nous allons apprendre le français avec Netflix et discuter des films français.",
    "Un podcast éducatif sur la vie quotidienne en France.",
    "Résumé des nouvelles en France aujourd'hui, avec un vocabulaire simple.",
    "Une vidéo humoristique qui utilise des expressions idiomatiques françaises.",
    "Un documentaire complet sur l'histoire politique de la France.",
    "Lecture du Petit Prince avec des expressions littéraires avancées."
]

# Count how many target words appear in each sample_text
media_df['relevance_score'] = media_df['sample_text'].apply(
    lambda text: sum(1 for word in text.lower().split() if word in target_words)
)

# Sort by relevance
media_df = media_df.sort_values(by='relevance_score', ascending=False)

# Save
media_df.to_csv(OUTPUT_PATH, index=False)
print(f"Saved ranked media content to {OUTPUT_PATH}")
