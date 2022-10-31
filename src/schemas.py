from datetime import date
from pydantic import BaseModel


class Request(BaseModel):
    id: int
    date: date
    duration: int

    class Config:
        orm_mode = True