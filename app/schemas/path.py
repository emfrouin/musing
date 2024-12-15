from pydantic import BaseModel
from typing import List, Optional

class PathBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True

class PathCreate(PathBase):
    name: str

class PathUpdate(PathBase):
    pass

class Path(PathBase):
    id: int
    

    class Config:
        orm_mode = True