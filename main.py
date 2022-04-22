import dataclasses
import os
from typing import Optional
from fastapi import FastAPI
from h11 import InformationalResponse
from pydantic import BaseModel
from airtable import airtable
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy import Boolean, Column, Float, String, Integer
from dotenv import load_dotenv, dotenv_values
load_dotenv()

app = FastAPI()

AIRTABLE_BASE_ID=os.environ.get("BASE_ID")
AIRTABLE_API_KEY=os.environ.get("API_KEY")
AIRTABLE_TABLE_NAME=os.environ.get("TABLE_NAME")

# SQLALCHEMY_DATABASE_URL = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'
SQLALCHEMY_DATABASE_URL = f"airtable://:keyXXXX@appYYY?peek_rows=10&tables=tableA&tables=tableB"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

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
    description: Optional[str] = None
    values : Optional[int] = None

    class Config:
        orm_mode = True

@app.post('/places/')
async def create_place_view(data: Data):
    return data

@app.get('/')
async def root():
    return {'message': 'Hello World!'}

