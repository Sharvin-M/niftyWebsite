from fastapi import FastAPI
from scraper import scrapee
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

@app.get(
    "/",
    description="Receive a singular, randomly chosen, key:value pair from Stanford's Nifty Projects List",
)
async def root():
    return scrapee("http://nifty.stanford.edu/")
