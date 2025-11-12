thonimport requests
from bs4 import BeautifulSoup
import json

class LinkedInScraper:
    def __init__(self, session_cookies):
        self.session = requests.Session()
        self.session.cookies.update(session_cookies)
    
    def fetch_profile(self, profile_url):
        response = self.session.get(profile_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        profile_data = self.extract_profile_data(soup)
        return profile_data

    def extract_profile_data(self, soup):
        # Extracting name, headline, location (for example)
        profile_data = {
            "name": soup.find("h1").text.strip(),
            "headline": soup.find("h2").text.strip(),
            "location": soup.find("span", class_="location").text.strip()
        }
        return profile_data

    def fetch_company(self, company_url):
        response = self.session.get(company_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        company_data = self.extract_company_data(soup)
        return company_data

    def extract_company_data(self, soup):
        company_data = {
            "company_name": soup.find("h1").text.strip(),
            "industry": soup.find("span", class_="industry").text.strip(),
            "size": soup.find("span", class_="size").text.strip(),
            "location": soup.find("span", class_="location").text.strip()
        }
        return company_data

    def fetch_posts(self, profile_url):
        response = self.session.get(profile_url + "/posts")
        soup = BeautifulSoup(response.text, 'html.parser')
        posts_data = self.extract_posts_data(soup)
        return posts_data

    def extract_posts_data(self, soup):
        posts = []
        for post in soup.find_all("div", class_="post"):
            posts.append({
                "content": post.find("p").text.strip(),
                "likes": post.find("span", class_="likes").text.strip(),
                "comments": post.find("span", class_="comments").text.strip()
            })
        return posts

# Example usage:
session_cookies = {'li_at': 'your_cookie_value', 'JSESSIONID': 'your_cookie_value'}
scraper = LinkedInScraper(session_cookies)
profile_data = scraper.fetch_profile("https://www.linkedin.com/in/johndoe")
print(json.dumps(profile_data, indent=2))