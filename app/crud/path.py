import logging

from typing import List
from tortoise.exceptions import DoesNotExist
from models import Path
from schemas.path import PathCreate, PathUpdate

async def create_path(path: PathCreate) -> Path:
    return await Path.create(**path.model_dump())
    
async def get_path(path_id: int) -> Path:
    return await Path.get(id=path_id)

async def get_paths() -> List[Path]:
    return await Path.all()

async def update_path(path_id: int, path_data: PathUpdate) -> Path:
    path = await Path.get(id=path_id)
    if not path:
        raise DoesNotExist(Path)
    
    for field, value in path_data.model_dump(exclude_unset=True).items():
            setattr(path, field, value)
    
    await path.save()
    return path

async def delete_path(path_id: int) -> None:
    path = await path.get(id=path_id)
    await path.delete()
    