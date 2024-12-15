from pydantic import BaseModel
from typing import Optional

class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int