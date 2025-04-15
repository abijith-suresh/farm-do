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
        todos.append(TodoDB(**doc))
    return todos

# Get a single Todo by ID
async def get_todo_by_id(todo_id: str) -> TodoDB | None:
    if not ObjectId.is_valid(todo_id):
        return None
    todo = await todo_collection.find_one({"_id": ObjectId(todo_id)})
    if todo:
        todo["_id"] = str(todo["_id"])
        return TodoDB(**todo)
    return None

# Update a Todo
async def update_todo(todo_id: str, data: dict) -> bool:
    if not ObjectId.is_valid(todo_id):
        return False
    result = await todo_collection.update_one(
        {"_id": ObjectId(todo_id)},
        {"$set": data}
    )
    return result.modified_count == 1

# Delete a Todo
async def delete_todo(todo_id: str) -> bool:
    if not ObjectId.is_valid(todo_id):
        return False
    result = await todo_collection.delete_one({"_id": ObjectId(todo_id)})
    return result.deleted_count == 1
