from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("helloworld")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("funcaoteste")
async def funcaoteste():
    return {"teste": "deu certo"}