thonimport requests
from bs4 import BeautifulSoup

def parse_profile_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    profile = {
        "name": soup.find("h1").text.strip(),
        "headline": soup.find("h2").text.strip(),
        "location": soup.find("span", class_="location").text.strip(),
        "skills": [skill.text.strip() for skill in soup.find_all("span", class_="skill")]
    }
    return profile