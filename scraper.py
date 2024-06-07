import requests
from bs4 import BeautifulSoup as bs


def scrapee(url):
    page = requests.get(url)
    soup = bs(page.content, "html.parser")

    all_links = soup.find_all("a")
    text = []
    tag = []
    for i in range(2, len(all_links)):
        if all_links[i].text == "(Video)" or all_links[i].text == "PDF version":
            continue
        text.append(all_links[i].text)
        tag.append(('http://nifty.stanford.edu/' + str(all_links[i].get("href"))))
    print(text)
    print(tag)

    return {k: v for (k, v) in zip(tag, text)}
