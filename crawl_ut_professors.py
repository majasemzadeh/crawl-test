import requests
from bs4 import BeautifulSoup
import json

url = "https://ece.ut.ac.ir/academic-staff"

teachers = []

while url:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the required section
    taglib_search_iterator = soup.find(class_="taglib-search-iterator")

    # Extract teacher info
    teachers_info = taglib_search_iterator.find_all(class_="portlet-section-body results-row")

    # Extract and save required details
    for teacher in teachers_info:
        teacher_details = teacher.find(class_="teacher-info")

        name = teacher_details.h3.a.text.strip()
        position = teacher_details.find_all(class_="info-field")[0].text.strip()
        field = teacher_details.find_all(class_="info-field")[1].text.strip()
        contact_no = teacher_details.find_all(class_="info-field")[2].text.strip()
        room = teacher_details.find_all(class_="info-field")[3].text.strip()
        # Extract email if you can decode the base64 image to text. Otherwise, it will be skipped.

        teacher_dict = {
            "Name": name,
            "Position": position,
            "Field": field,
            "Contact No": contact_no,
            "Room": room
        }

        teachers.append(teacher_dict)

    # Find the next page link
    next_page = soup.find('a', class_='next')

    # If a next page is found, update the URL; otherwise, break the loop
    if next_page:
        url = next_page['href']
    else:
        url = None

# Save the collected data to a JSON file
with open('teachers.json', 'w', encoding='utf-8') as f:
    json.dump(teachers, f, ensure_ascii=False, indent=4)