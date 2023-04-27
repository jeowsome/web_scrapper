import requests
from bs4 import BeautifulSoup
import string


def remove_punctuations(word: string) -> string:
    return word.translate(str.maketrans('', '', string.punctuation))


def get_filename(word: string) -> string:
    _name = remove_punctuations(word)
    filename = string.Template("${name}.txt")
    _name = _name.replace(" ", "_")
    return filename.substitute(name=_name)


def write_content(filename, path):
    article_page = requests.get(URL.substitute(path=path))
    page_soup = BeautifulSoup(article_page.content, PARSER_OPTION)
    content = page_soup.select_one(".article__teaser").text
    with open(filename, 'wb') as file:
        file.write(content.encode("utf-8"))

    file_list.append(filename)


URL = string.Template("https://www.nature.com${path}")
PARSER_OPTION = "html.parser"
r = requests.get(URL.substitute(path="/nature/articles?sort=PubDate&year=2020&page=3"))
soup = BeautifulSoup(r.content, PARSER_OPTION)
article_list = soup.find_all("article")
file_list = []

for article in article_list:
    meta = article.select_one("div > span[data-test='article.type'] > span.c-meta__type")

    if meta.text == 'News':
        title_container = article.select_one('[data-track-action="view article"]')
        title = get_filename(title_container.text)
        write_content(filename=title, path=title_container.get('href'))


print("Saved articles:", file_list)
