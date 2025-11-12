thonimport requests
from bs4 import BeautifulSoup

def parse_post_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    posts = []
    for post in soup.find_all("div", class_="post"):
        posts.append({
            "content": post.find("p").text.strip(),
            "likes": post.find("span", class_="likes").text.strip(),
            "comments": post.find("span", class_="comments").text.strip()
        })
    return posts