__all__ = ["validate_object_id"]

from bson import ObjectId
from fastapi import Path, HTTPException


def validate_object_id(todo_id: str = Path(..., alias="todo_id")) -> ObjectId:
    if not ObjectId.is_valid(todo_id):
        raise HTTPException(status_code=400, detail="Invalid ID format")
    return ObjectId(todo_id)
