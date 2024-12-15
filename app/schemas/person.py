from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PersonBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    address: Optional[str] = None

    class Config:
        orm_mode = True

class PersonCreate(PersonBase):
    pass

class Person(PersonBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True