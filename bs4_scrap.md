
# Maktabkhooneh Course Scraper

This script scrapes course information from the Maktabkhooneh website and saves it in a JSON format.

## Requirements:

- Python 3.6+
- BeautifulSoup
- requests

## Installation:

1. Ensure you have Python 3.x installed.
2. Install required packages:
```
pip install beautifulsoup4 requests
```

## How to Run:

1. Simply execute the script:
```
python beauty_scrap.py
```

2. The script will fetch course details from the Maktabkhooneh website.

3. Once the script finishes, you'll find a file named `courses.json` in the same directory containing the scraped course information.

## Features:

1. **URL Fetching**: The script fetches content from the base URL "https://maktabkhooneh.org".
2. **Pagination Handling**: The script correctly iterates through multiple pages of courses when available.
3. **Data Extraction**: The script extracts the following information for each course:
    - Title
    - Teacher's name
    - Price

4. **JSON Export**: The extracted course details are saved in a structured JSON format.
