from pydantic import BaseModel
from typing import List, Optional
from schemas.skill import Skill
from schemas.path import Path

class LevelBase(BaseModel):
    name: str
    description: Optional[str] = None
    path_id: int

    class Config:
        orm_mode = True

class LevelCreate(LevelBase):
    pass

class LevelUpdate(LevelBase):
    pass

class Level(LevelBase):
    id: int

    class Config:
        orm_mode = True