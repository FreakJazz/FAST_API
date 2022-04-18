import os
from typing import Optional
from fastapi import FastAPI
from airtable import airtable
from dotenv import load_dotenv, dotenv_values
load_dotenv()

AIRTABLE_BASE_ID=os.environ.get("BASE_ID")
AIRTABLE_API_KEY=os.environ.get("API_KEY")
AIRTABLE_TABLE_NAME=os.environ.get("TABLE_NAME")
endpoint = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/api/post")
def post_data(data):
    print(data)

    return {data}


