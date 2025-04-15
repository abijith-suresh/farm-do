__all__ = ["validate_object_id"]

from fastapi import Path, HTTPException
from bson import ObjectId

def validate_object_id(todo_id: str = Path(..., alias="todo_id")) -> ObjectId:
    if not ObjectId.is_valid(todo_id):
        raise HTTPException(status_code=400, detail="Invalid ID format")
    return ObjectId(todo_id)