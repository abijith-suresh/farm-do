from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

MONGO_DETAILS = "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGO_DETAILS)

# Actual database
database = client.todo_app

# Collection
todo_collection = database.get_collection("todos")