thonimport requests
from bs4 import BeautifulSoup

def parse_company_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    company = {
        "company_name": soup.find("h1").text.strip(),
        "industry": soup.find("span", class_="industry").text.strip(),
        "size": soup.find("span", class_="size").text.strip(),
        "location": soup.find("span", class_="location").text.strip()
    }
    return company