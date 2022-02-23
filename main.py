from fastapi import FastAPI
from fake_db import fake_item_db

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}   

@app.get("/items/")
async def read_item(item_id: int):
    elm = filter(lambda x: x['id'] == item_id, fake_item_db)
    return elm

