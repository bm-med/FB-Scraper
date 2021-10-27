from fastapi import FastAPI
import scraper

app=FastAPI()
posts=scraper.scraper()

@app.get("/scrape")
async def read_item(url:str,num:str):
    return posts.scrapedata(url,num)
