thonimport requests
from bs4 import BeautifulSoup

def parse_message_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    messages = []
    for message in soup.find_all("div", class_="message"):
        messages.append({
            "sender": message.find("span", class_="sender").text.strip(),
            "content": message.find("p", class_="content").text.strip(),
            "timestamp": message.find("span", class_="timestamp").text.strip()
        })
    return messages