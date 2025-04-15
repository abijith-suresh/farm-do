from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field, ConfigDict
from bson import ObjectId
from enum import Enum

class PyObjectId(ObjectId):
    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema, handler):
        return {"type": "string"}

    @classmethod
    def __get_pydantic_core_schema__(cls, source, handler):
        from pydantic_core import core_schema

        return core_schema.no_info_after_validator_function(
            cls.validate,
            core_schema.str_schema()
        )

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError(f"Invalid ObjectId: {v}")
        return ObjectId(v)

class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

# Shared fields for Todo
class TodoBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=250)
    completed: bool = False
    priority: Priority = Priority.medium
    due_date: Optional[datetime] = None
    tags: Optional[List[str]] = []
    list_id: Optional[PyObjectId] = None

# Model used when creating a Todo
class TodoCreate(TodoBase):
    pass

# Model used when returning a Todo from DB
class TodoDB(TodoBase):
    id: PyObjectId = Field(alias="_id")

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str}
    )
