from fastapi import APIRouter
from app.news_scraper import scrape_moneycontrol, scrape_economic_times
from app.routes.portfolio import portfolio_store

router = APIRouter()

def scrape_news():
    return scrape_moneycontrol() + scrape_economic_times()

@router.get("/general")
def get_general_news():
    all_news = scrape_news()
    return all_news[:10]  # only top 10 headlines for general display

@router.get("/filtered")
def get_filtered_news():
    portfolio = portfolio_store.get("user", [])
    all_news = scrape_news()  # get all articles
    filtered = [
        article for article in all_news
        if any(sym.lower() in article["title"].lower() for sym in portfolio)
    ]
    return filtered
