from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Dict, Optional

app = FastAPI(
    title="FastAPI CRUD API",
    description="A simple CRUD API example using FastAPI and Pydantic with in-memory storage.",
    version="1.0.0"
)

# Pydantic model for Item
class Item(BaseModel):
    name: str = Field(..., example="Laptop")
    description: Optional[str] = Field(None, example="A high-performance gaming laptop")
    price: float = Field(..., gt=0, example=999.99)
    tax: Optional[float] = Field(None, example=80.0)

# Simulate a database with an in-memory dictionary
db: Dict[int, Item] = {}
current_id = 0

@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    """
    Create a new item.
    """
    global current_id
    current_id += 1
    db[current_id] = item
    return item

@app.get("/items/", response_model=Dict[int, Item])
def read_all_items():
    """
    Retrieve all items.
    """
    return db

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    """
    Retrieve a specific item by its ID.
    """
    if item_id not in db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found"
        )
    return db[item_id]

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    """
    Update an existing item by its ID.
    """
    if item_id not in db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found"
        )
    db[item_id] = item
    return item

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    """
    Delete an item by its ID.
    """
    if item_id not in db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found"
        )
    del db[item_id]
    return None
