import logging

from typing import List
from tortoise.exceptions import DoesNotExist
from models import Level, Path
from crud.path import get_path
from schemas.level import LevelCreate, LevelUpdate

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

async def create_level(name: str, description:str, path:Path) -> Level:
    return await Level.create(
            name=name,
            description=description,
            path=path
            )

async def get_level(level_id: int) -> Level:
    return await Level.get(id=level_id)

async def get_levels() -> List[Level]:
    return await Level.all()

async def update_level(level_id: int, level_data: LevelUpdate) -> Level:
    level = await Level.get(id=level_id)
    if not level:
        raise DoesNotExist(Level)
    
    for field, value in level_data.model_dump(exclude_unset=True).items():
            setattr(level, field, value)
    
    await level.save()
    return level

async def delete_level(level_id: int) -> None:
    level = await level.get(id=level_id)
    await level.delete()
    