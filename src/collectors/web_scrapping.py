import requests
from bs4 import BeautifulSoup

class WebsiteCollector:
    """
    Collects text data from website.
    """
    def __init__(self, urls):
        self.urls = urls

    def fetch_content(self):
        contents = []
        for url in self.urls:
            try:
                r = requests.get(url=url, timeout=10)
                if r.status_code == 200:
                    soup = BeautifulSoup(r.text, "html.parser")
                    contents.append(soup.get_text())
            except Exception as e:
                print(f"[ERROR] Failed to fetch {url}: {e}")


        return contents
    