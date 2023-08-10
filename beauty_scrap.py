from bs4 import BeautifulSoup
import requests
import json


def get_html_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    return None


# Base URL
base_url = "https://maktabkhooneh.org"

response = requests.get(base_url)
courses = []
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    elements = soup.find_all(class_="swiper")

    if elements:
        hrefs = [link['href'] for link in elements[0].find_all('a', href=True)]

        for href in hrefs:
            p = 1
            new_html_content = get_html_content(base_url + href)
            new_soup = BeautifulSoup(new_html_content, 'html.parser')

            paginator_links = new_soup.find_all(class_="paginator__link")[-1]

            while p < int(paginator_links.text):

                if p == 1:
                    new_html_content = get_html_content(base_url + href)
                else:
                    new_html_content = get_html_content(base_url + href+ f"?p={p}")

                if new_html_content:
                    new_soup = BeautifulSoup(new_html_content, 'html.parser')
                    cards = new_soup.find_all(class_="course-card")

                    for card in cards :

                        title = card.find(class_="course-card__title")
                        teacher = card.find(class_="course-card__teacher")
                        hierarchie = card.find(class_="course-card-extra__hierarchy")
                        price = card.find(class_="course-card-extra__price")
                        discount = card.find(class_="course-card__discount")
                        old_price = card.find(class_="course-card-extra__price--old")

                        course_info = {
                                'title': title.text if title else "",
                                'teacher': teacher.text if teacher else "",
                                'price': price.text if price else 0,
                        }
                        courses.append(course_info)
                p += 1

        # Save courses info to a JSON file
        with open('courses.json', 'w', encoding='utf-8') as f:
            json.dump(courses, f, ensure_ascii=False, indent=4)
        print("Courses info saved to courses.json.")

