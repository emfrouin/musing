from pydantic import BaseModel
from typing import List
from schemas.student_path import StudentPath
from schemas.score import Score

class StudentReportBase(BaseModel):
    path: List[StudentPath]
    scores: List[Score]

    class Config:
        orm_mode = True

class StudentReportCreate(StudentReportBase):
    pass

class StudentReport(StudentReportBase):
    id: int

    class Config:
        orm_mode = True