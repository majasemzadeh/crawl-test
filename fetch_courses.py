import requests
import json

all_responses = []


def extract_data(slug):
    """Fetch data for a category"""

    res = requests.get(
        f"https://maktabkhooneh.org/api/v1/courses/categories/{slug}/search/?page={1}&offset=24&limit=1000&required_filter=1")
    data = res.json()
    all_responses.append(data)

    children = data.get('children', [])
    for child in children:
        extract_data(child['slug'])


res = requests.get("https://maktabkhooneh.org/api/v1/courses/categories/")
root_categories = res.json()

for category in root_categories:
    extract_data(category['slug'])


file_path = "all_data.json"
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(all_responses, f, indent=4, ensure_ascii=False)
