import logging
from fastapi import APIRouter, HTTPException, status
from tortoise.exceptions import IntegrityError, DoesNotExist
from pydantic import ValidationError

from schemas.path import Path, PathCreate, PathUpdate
from models import Path
from crud.path import create_path, get_paths, get_path, update_path, delete_path

# Initialize logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

router = APIRouter()

@router.post("/")
async def create_path_api(path: PathCreate):
    try:
        return await create_path(path)
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
async def get_all_paths_api():
    try:
        return await get_paths()
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

@router.get("/{path_id}")
async def get_path_api(path_id: int):
    try:
        return await get_path(path_id)
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

@router.put("/{path_id}")
async def update_path_api(path_id: int, path: PathUpdate ):
    try:
        return await update_path(path_id, path)
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

