from fastapi import FastAPI
from typing import Union
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/helloworld")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/funcaoteste")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0, 1000)}

