import requests, re

def extract_urls(url: str):
    response = str(requests.get(url).content)
    for url in re.findall(r'\"https?://[^\"]*\"', response):
        print(url)

extract_urls('http://fecalfunny.com')