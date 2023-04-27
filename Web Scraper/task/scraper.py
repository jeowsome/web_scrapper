import requests
from bs4 import BeautifulSoup

INVALID_REQUEST = "Invalid page!"


def get_request(url):
    r = requests.get(url)

    if r:
        return r.content
    print(f"The URL returned {r.status_code}!")


def process_result(get_result):
    result = {}
    if get_result == INVALID_REQUEST:
        return get_result

    soup = BeautifulSoup(get_result, 'html.parser')

    if soup.find('title').text and soup.select('meta[name="description"]'):
        result.update({
            'title': soup.find('title').text,
            'description': soup.select_one('meta[name="description"]').get('content')
        })

    if result.get('title') and result.get('description'):
        return result
    return INVALID_REQUEST


def save_to_html(content):
    with open("source.html", "wb") as file:
        file.write(content)

    print("Content saved.")


input_url = input("Input the URL:\n")
res = get_request(input_url)

if res:
    save_to_html(res)
