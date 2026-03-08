from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    completed: bool = False

db: List[Item] = []

@app.post("/items", response_model=Item)
def create_item(item: Item):
    db.append(item)
    return item 

@app.get("/items/", response_model=List[Item])
def get_all_item():
    return db

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(db):
        if item.id == item_id:
            updated_item.id = item_id
            db[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(db):
        if item.id == item_id:
            return db.pop(index)
    raise HTTPException(status_code=404, detail="Item not found")