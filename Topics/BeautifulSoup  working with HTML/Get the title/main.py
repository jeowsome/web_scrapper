import requests

from bs4 import BeautifulSoup

r = requests.get(input())
soup = BeautifulSoup(r.content, "html.parser")
h1 = soup.findAll('h1')

for h in h1:
    print(h.text)