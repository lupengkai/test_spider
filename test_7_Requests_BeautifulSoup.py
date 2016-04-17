import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.jd.com')
soup = BeautifulSoup(response.text)

print(soup.title.text)

print(soup.body.text)

for x in soup.findAll('a'):
    print(x['href'])
