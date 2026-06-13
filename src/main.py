from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

items: dict[int, Item] = {}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items/{item_id}", status_code=201)
def create_item(item_id: int, item: Item):
    if item_id in items:
        raise HTTPException(status_code=409, detail="Item already exists")
    items[item_id] = item
    return {"item_id": item_id, **item.model_dump()}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "q": q, **items[item_id].model_dump()}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return {"item_id": item_id, **item.model_dump()}
