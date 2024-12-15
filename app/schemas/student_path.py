from pydantic import BaseModel
from typing import List
from schemas.student import Student
from schemas.path import Path
from schemas.level import Level

class StudentPathBase(BaseModel):
    student: List[Student]
    path: List[Path]
    level: List[Level]

    class Config:
        orm_mode = True

class StudentPathCreate(StudentPathBase):
    pass

class StudentPath(StudentPathBase):
    id: int

    class Config:
        orm_mode = True