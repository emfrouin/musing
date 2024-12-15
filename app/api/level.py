import logging
from fastapi import APIRouter, HTTPException, status
from tortoise.exceptions import IntegrityError, DoesNotExist
from pydantic import ValidationError

from schemas.level import LevelCreate, LevelUpdate
from crud.level import create_level, get_levels, get_level, update_level, delete_level
from crud.path import get_path

from models import Path

# Initialize logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

router = APIRouter()

@router.post("/")
async def create_level_api(level: LevelCreate):
    try:
        path = await get_path(path_id=level.path_id)
        logger.error(f"Path to be associated to level {path}")
        if not path:
            raise DoesNotExist(Path)
        return await create_level(
            name=level.name,
            description=level.description,
            path=path
            )
    except IntegrityError as e:
        # Handle unique constraint violations or other DB errors
        logger.error(f"Integrity error: {e}")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Database integrity error, possibly due to duplicate entries"
        ) from e
    
    except ValidationError as e:
        # Handle errors related to Pydantic validation
        logger.error(f"Validation error: {e}")
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Request data is invalid or malformed"
        ) from e
    
    except DoesNotExist as e:
        # Handle Tortoise ORM model lookup errors
        logger.error(f"Does not exist error: {e}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Requested resource not found"
        ) from e
    
    except Exception as e:
        # Catch any other unexpected errors
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'{type(e)}'
        ) from e

@router.get("/")
async def get_all_levels_api():
    try:
        return await get_levels()
    except DoesNotExist as e:
        # Handle Tortoise ORM model lookup errors
        logger.error(f"Does not exist error: {e}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Requested resource not found"
        ) from e
    
    except Exception as e:
        # Catch any other unexpected errors
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'{type(e)}'
        ) from e

@router.get("/{level_id}")
async def get_level_api(level_id: int):
    try:
        return await get_level(level_id)
    except DoesNotExist as e:
        # Handle Tortoise ORM model lookup errors
        logger.error(f"Does not exist error: {e}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Requested resource not found"
        ) from e
    
    except Exception as e:
        # Catch any other unexpected errors
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'{type(e)}'
        ) from e

@router.put("/{level_id}")
async def update_level_api(level_id: int, level: LevelUpdate ):
    try:
        return await update_level(level_id, level)
    except DoesNotExist as e:
        # Handle Tortoise ORM model lookup errors
        logger.error(f"Does not exist error: {e}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Requested resource not found"
        ) from e
    
    except Exception as e:
        # Catch any other unexpected errors
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'{type(e)}'
        ) from e

