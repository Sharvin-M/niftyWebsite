import requests
from bs4 import BeautifulSoup as bs

url = 'http://nifty.stanford.edu/'

page = requests.get(url)
soup = bs(page.content, "html.parser")

all_links = soup.find_all('a')
text = []
tag = []
for i in range(2, len(all_links)):
    if (all_links[i].text == '(Video)' or all_links[i].text == 'PDF version'):
        continue
    text.append(all_links[i].text)
    tag.append(all_links[i].get('href'))
print(text)
print(tag)

tag_text = { k:v for (k,v) in zip(tag, text)}  

print(tag_text)