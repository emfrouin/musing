from pydantic import BaseModel
from datetime import datetime
from schemas.person import PersonBase

class StudentCreate(PersonBase):
    birthday: datetime

class Student(PersonBase):
    id: int
    birthday: datetime

    class Config:
        orm_mode = True