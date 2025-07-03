# app/main.py
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from app.routes import news, portfolio, analyze

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(news.router, prefix="/news")
app.include_router(portfolio.router, prefix="/portfolio")
app.include_router(analyze.router, prefix="/analyze")
