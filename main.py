from fastapi import FastAPI
from scraper import scrapee

app = FastAPI()


@app.get(
    "/",
    description="Recieve a key:value store with the latest from Stanford's Nifty Projects List",
)
async def read_projects():
    return scrapee("http://nifty.stanford.edu/")
