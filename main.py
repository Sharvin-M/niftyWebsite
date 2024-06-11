from fastapi import FastAPI
import requests
import random
from bs4 import BeautifulSoup as bs
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
handler = Mangum(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get(
    "/",
    description="Receive a singular, randomly chosen, key:value pair from Stanford's Nifty Projects List",
)
async def root():
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
            tag.append(("http://nifty.stanford.edu/" + str(all_links[i].get("href"))))

        dict = {k: v for (k, v) in zip(tag, text)}
        return random.choice(list(dict.items()))

    return scrapee("http://nifty.stanford.edu/")
