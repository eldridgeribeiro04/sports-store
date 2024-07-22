from bs4 import BeautifulSoup as bs
import requests

url = 'http://127.0.0.1:8000/Asos/'
response = requests.get(url)
html_content = response.content
print(html_content)

soup = bs(html_content, 'html.parser')

def get_all_links(url):
    for link in soup.find_all('a'):
        print(link)
        
get_all_links(url)
    