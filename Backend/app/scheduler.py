# app/scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from app.news_scraper import scrape_news

scheduler = BackgroundScheduler()
scheduler.add_job(scrape_news, "interval", minutes=30)
scheduler.start()
