from pydantic import BaseModel
from typing import List

class PortfolioInput(BaseModel):
    symbols: List[str]

