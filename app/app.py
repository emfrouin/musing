import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
from models import Item
from database import init_db

from api.path import router as path_router
from api.level import router as level_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # allow Vite frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

app.include_router(path_router, prefix="/paths", tags=["paths"])
app.include_router(level_router, prefix="/levels", tags=["levels"])


# Define the lifespan context manager function
async def asyncio_lifespan(app: FastAPI):
    # Initialize the database at startup
    await init_db()
    # Yield control to FastAPI (this is where the app is running)
    yield
    # Any cleanup code (optional) goes here for shutdown


# initialize Tortoise ORM with FastAPI
register_tortoise(
    app, 
    db_url= "sqlite://db.sqlite3",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)