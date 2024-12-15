from pydantic import BaseModel
from typing import List
from schemas.person import PersonBase
from schemas.path import Path

class TeacherCreate(PersonBase):
    pass

class Teacher(PersonBase):
    id: int
    paths: List[Path]

    class Config:
        orm_mode = True