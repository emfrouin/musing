from pydantic import BaseModel
from enum import Enum
from typing import List
from schemas.skill import Skill

class ScoreEnum(str, Enum):
    COMPLETE = 'Complete'
    INCOMPLETE = 'Incomplete'
    NOT_ATTEMPTED = 'Not Attempted'

class ScoreBase(BaseModel):
    score: ScoreEnum
    comment: str

    class Config:
        orm_mode = True

class ScoreCreate(ScoreBase):
    pass

class Score(ScoreBase):
    id: int
    skill: List[Skill]  # Assuming skill is linked via a ManyToManyField

    class Config:
        orm_mode = True