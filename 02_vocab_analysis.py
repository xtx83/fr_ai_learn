# scripts/02_vocab_analysis.py

import pandas as pd
from collections import Counter
import os

INPUT_PATH = "../data/parsed_output/cleaned_tokens.csv"
OUTPUT_PATH = "../data/parsed_output/user_vocab_stats.csv"

# Load cleaned tokens
df = pd.read_csv(INPUT_PATH)
tokens = df['token'].tolist()

# Count frequency
counts = Counter(tokens)

# Convert to DataFrame
stats = pd.DataFrame(counts.items(), columns=["word", "frequency"])
stats = stats.sort_values(by="frequency", ascending=False).reset_index(drop=True)

# Add dummy "difficulty" score (to be refined later)
stats["difficulty"] = stats["frequency"].apply(lambda x: 5 if x == 1 else 3 if x == 2 else 1)

# Save
stats.to_csv(OUTPUT_PATH, index=False)
print(f"Wrote vocab stats to {OUTPUT_PATH}")
