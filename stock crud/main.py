from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel
from typing import List, Optional
import yfinance as yf

app = FastAPI()

class Stock(BaseModel):
    id: int
    name: str
    price: float
    shares: int


db: List[Stock] = []

@app.post("/stock/", response_model=Stock)
def create_stock(stock: Stock):
    db.append(stock)
    return stock

# Get All Stocks
@app.get("/stocks/", response_model=List[Stock])
def get_all_stocks():
    return db

# Get One Stock by ID
@app.get("/stock/{stock_id}", response_model=Stock)
def get_stock(stock_id: int):
    for stock in db: 
        if stock.id == stock_id:
            return stock 
    raise HTTPException(status_code=404, detail="Stock not found") 