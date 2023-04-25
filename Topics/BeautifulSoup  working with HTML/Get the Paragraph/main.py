import requests

from bs4 import BeautifulSoup

word = input()
url = input()

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
p_list = soup.find_all('p')

for p in p_list:
    if word in p.text:
        print(p.text)
        break
