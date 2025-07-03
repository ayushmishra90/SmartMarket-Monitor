# app/routes/portfolio.py
from fastapi import APIRouter
from app.schemas import PortfolioInput

router = APIRouter()

portfolio_store = {}

@router.post("/")
def save_portfolio(portfolio: PortfolioInput):
    portfolio_store["user"] = portfolio.symbols
    return {"message": "Portfolio saved.", "symbols": portfolio.symbols}

@router.get("/")
def get_portfolio():
    return {"symbols": portfolio_store.get("user", [])}
