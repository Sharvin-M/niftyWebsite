from fastapi import FastAPI
from scraper import scrapee

app = FastAPI()


@app.get("/")
def read_projects():
    return scrapee("http://nifty.stanford.edu/")
