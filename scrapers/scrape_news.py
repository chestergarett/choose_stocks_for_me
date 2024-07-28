import re
import requests
from bs4 import BeautifulSoup
import json

class NewsScraper:
    def __init__(self,url):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        self.response = requests.get(url,headers=self.headers)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        self.links = [a['href'] for a in self.soup.find_all('a', href=True) if a['href'].startswith('/news/articles')]
        
        with open(r'scrapers/scraped_links.json', 'w') as json_file:
            json.dump(self.links, json_file)

    def extract_content_from_links(self,updated_url): 
        for link in self.links:
            updated_link = f'{updated_url}{link}'
            self.response = requests.get(url,headers=self.headers)
            self.soup = BeautifulSoup(self.response.text, 'html.parser')
            page_text = self.soup.get_text()
            sanitized_link = re.sub(r'[^\w\s-]', '_', updated_link)

            with open(f'scrapers/{sanitized_link}.txt', 'w', encoding='utf-8') as file:
                file.write(page_text)
            
            break
        
        return

url = 'https://www.bloomberg.com/markets'
base_url = 'https://www.bloomberg.com'
bloomberg_news = NewsScraper(url)
bloomberg_news.extract_content_from_links(base_url)

