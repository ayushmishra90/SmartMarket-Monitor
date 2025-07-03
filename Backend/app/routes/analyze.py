from fastapi import APIRouter, Body
from app.ai_analysis import analyze_headlines

router = APIRouter()

@router.post("")
def analyze_news(headlines: list = Body(...)):
    return analyze_headlines(headlines)
