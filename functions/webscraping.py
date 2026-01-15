import requests
from bs4 import BeautifulSoup

response = requests.get("https://bbc.com")
content = response.text

soup = BeautifulSoup(content, 'html.parser')

title = soup.find_all('title')
print(title)