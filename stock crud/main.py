from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel
from typing import List, Optional
import yfinance as yf

app = FastAPI()

# 1. Define the Model FIRST
class Stock(BaseModel):
    id: int
    name: str
    price: float
    shares: int

# 2. Define the Database AFTER the class
db: List[Stock] = []

# --- ENDPOINTS ---

@app.post("/stocks/", response_model=Stock)
def create_stock(stock: Stock):
    db.append(stock)
    return stock

@app.get("/stocks/", response_model=List[Stock])
def get_all_stocks():
    return db

@app.get("/stocks/{stock_id}", response_model=Stock)
def get_stock(stock_id: int):
    for stock in db: 
        if stock.id == stock_id:
            return stock 
    raise HTTPException(status_code=404, detail="Stock not found") 

@app.put("/stocks/{stock_id}", response_model=Stock)
def update_stock(stock_id: int, updated_stock: Stock):
    for index, stock in enumerate(db):
        if stock.id == stock_id:
            # Ensure the ID from the URL stays the same
            updated_stock.id = stock_id
            db[index] = updated_stock
            return updated_stock
    raise HTTPException(status_code=404, detail="Stock not found") 

@app.delete("/stocks/{stock_id}")
def delete_stock(stock_id: int):
    for index, stock in enumerate(db):
        if stock.id == stock_id:
            return db.pop(index)
    raise HTTPException(status_code=404, detail="Stock not found")