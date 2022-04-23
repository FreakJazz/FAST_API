from datetime import date
from pydantic import BaseModel
from typing import Optional

# data class
class User(BaseModel):
    Name: str
    LastName: str
    Email: str
    Cellphone: int
    # Para que los campos sean opcionales al momento de ingresar
    Birthday: Optional[date] = None
    Sex: str
    Adress: str
    State: bool

    class Config:
        orm_mode = True