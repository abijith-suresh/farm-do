from bson import ObjectId

from app.core.database import todo_collection
from app.models.todo import TodoCreate, TodoDB


# Create a new Todo
async def create_todo(todo: TodoCreate) -> TodoDB:
    todo_dict = todo.model_dump()
    result = await todo_collection.insert_one(todo_dict)
    todo_dict["_id"] = str(result.inserted_id)
    return TodoDB(**todo_dict)


# Get all Todos
async def get_all_todos() -> list[TodoDB]:
    todos = []
    async for doc in todo_collection.find():
        doc["_id"] = str(doc["_id"])
        if doc.get("list_id"):
            doc["list_id"] = str(doc["list_id"])
        todos.append(TodoDB(**doc))
    return todos


# Get a single Todo by ID
async def get_todo_by_id(todo_id: ObjectId) -> TodoDB | None:
    todo = await todo_collection.find_one({"_id": todo_id})
    if todo:
        todo["_id"] = str(todo["_id"])
        if todo.get("list_id"):
            todo["list_id"] = str(todo["list_id"])
        return TodoDB(**todo)
    return None


# Update a Todo
async def update_todo(todo_id: ObjectId, data: dict) -> bool:
    result = await todo_collection.update_one({"_id": todo_id}, {"$set": data})
    return result.modified_count == 1


# Delete a Todo
async def delete_todo(todo_id: ObjectId) -> bool:
    result = await todo_collection.delete_one({"_id": todo_id})
    return result.deleted_count == 1
