from fastapi import FastAPI

app = FastAPI()
fake_item_db = [
    {
        "id": 1,
        "name": "Foo"
    },
    {
        "id": 2,
        "name": "Bar"
    },
    {
        "id": 3,
        "name": "Baz"
    },
]

@app.get("/")
async def root():
    return {"message": "Hello World"}   

@app.get("/items/")
async def read_item(item_id: int):
    elm = filter(lambda x: x['id'] == item_id, fake_item_db)

    return elm