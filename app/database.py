from tortoise import Tortoise

DATABASE_URL = "sqlite://db.sqlite3"

async def init_db():
    await Tortoise.init(
        db_url=DATABASE_URL,
        modules={"models": ["models"]},
    )
    await Tortoise.generate_schemas