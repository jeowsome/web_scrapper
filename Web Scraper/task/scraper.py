import requests

INVALID_REQUEST = "Invalid quote resource!"


def process_request(url):
    r = requests.get(url)

    if r:
        result = r.json()
        return result.get("content", INVALID_REQUEST)
    return INVALID_REQUEST


input_url = input("Input the URL:\n")
print(process_request(input_url))
