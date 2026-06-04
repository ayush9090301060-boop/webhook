from fastapi import FastAPI
app = FastAPI()

@app.get("/items")
def list_items():
    return []

@app.post("/items/{item_id}")
def create_item(item_id: int):
    return {"status": "created"}
