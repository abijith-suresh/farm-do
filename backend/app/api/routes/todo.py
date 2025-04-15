from bson import ObjectId
from fastapi import APIRouter, HTTPException, status, Depends

from app.crud import todo as crud
from app.models.todo import TodoCreate, TodoDB
from app.utils.validators import validate_object_id

router = APIRouter(prefix="/todos", tags=["Todos"])


@router.post("/", response_model=TodoDB, status_code=status.HTTP_201_CREATED)
async def create_todo(todo: TodoCreate):
    return await crud.create_todo(todo)


@router.get("/", response_model=list[TodoDB])
async def read_todos():
    return await crud.get_all_todos()


@router.get("/{todo_id}", response_model=TodoDB)
async def read_todo(todo_id: ObjectId = Depends(validate_object_id)):
    todo = await crud.get_todo_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.put("/{todo_id}", response_model=TodoDB)
async def update_todo(
    data: TodoCreate, todo_id: ObjectId = Depends(validate_object_id)
):
    success = await crud.update_todo(todo_id, data.model_dump())
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")
    updated = await crud.get_todo_by_id(todo_id)
    return updated


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: ObjectId = Depends(validate_object_id)):
    success = await crud.delete_todo(todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")
    return None
