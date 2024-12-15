from pydantic import BaseModel
from enum import Enum
from typing import List

class SkillTypeEnum(str, Enum):
    TECHNICAL = 'Technical'
    STYLE = 'Style'
    PERFORMANCE = 'Performance'

class SkillBase(BaseModel):
    name: str
    type: SkillTypeEnum

    class Config:
        orm_mode = True

class SkillCreate(SkillBase):
    pass

class Skill(SkillBase):
    id: int
