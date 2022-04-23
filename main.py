import os
from fastapi import FastAPI
from pydantic import BaseModel
from airtable import airtable
from dotenv import load_dotenv, dotenv_values
from schemas import User

load_dotenv()

# Config table data from airtable database
AIRTABLE_BASE_ID=os.environ.get("BASE_ID")
AIRTABLE_API_KEY=os.environ.get("API_KEY")
AIRTABLE_TABLE_NAME=os.environ.get("TABLE_NAME")

endpoint = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'

# 
app = FastAPI(title= 'Test-app',
                description= 'CRUD API WITH AIRTABLE AND FAST API',
                version='1.0.0')



# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# data class
class Data(BaseModel):
    name: str


    class Config:
        orm_mode = True

@app.post('/api/user/')
async def create_user(user: User):


    return user

@app.get('/')
async def root():
    return {'message': 'Hello World!'}

