from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
api = FastAPI()

class Todo(BaseModel):
    id : int
    name: str
    description: str

todos : List[Todo] = []

@api.get("/")
def read_root():
    return {"Hello": "World"}

@api.get("/todo")
def get_todo():
    return todos

@api.post("/todo")
def post_todo(todo: Todo):
    todos.append(todo)
    return todos
@api.put("/todo/{todo_id}")
def update_todo(todo_id: int, update_todo:Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todo[index]=update_todo
            return todos
    return {"message":"Error in Update"}

@api.delete("/todo/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            deleted = todos.pop(index)
            return todos
    return {"message: Error in deletion!"}
