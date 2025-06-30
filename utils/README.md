# fr_ai_learn

A Python-based system for personalized French learning using voice transcript analysis and media recommendation. It leverages AI-generated speech-to-text data, pandas-based vocabulary processing, and web scraping to match users with media that fits both their learning needs and interests.

## Features
- Processes raw speech transcripts (e.g. from OpenAI Whisper)
- Cleans and tokenizes text for vocabulary analysis
- Detects commonly used and potentially difficult words
- Allows users to specify their media preferences
- Scrapes and filters media content by genre, format, and learning relevance
- Ranks content by how well it matches user vocabulary gaps

## Folder Structure
```
fr_ai_learn/
├── data/
│   ├── raw_transcripts/        # Raw voice-to-text input
│   └── parsed_output/          # Cleaned tokens and vocab analysis
├── media/                      # Recommended media links
├── scripts/                    # Functional scripts for each pipeline step
├── utils/                      # Reusable cleaning and NLP components
├── notebooks/                  # Exploratory data analysis notebook
├── config/                     # User preferences
├── README.md
└── requirements.txt
```

## Requirements
- Python 3.9+
- pandas
- matplotlib
- seaborn
- requests (if expanding scraper)

Install with:
```bash
pip install -r requirements.txt
```

## Status
WIP (Work in Progress) — structure and scripts working independently. Full integration and UI/UX polish to follow.
