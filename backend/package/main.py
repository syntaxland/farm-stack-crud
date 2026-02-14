import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from model import Todo, TodoUpdate
from database import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo,
)

app = FastAPI()

origins = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/api/todo")
async def get_todo():
    return await fetch_all_todos()

@app.get("/api/todo/{title}", response_model=Todo)
async def get_todo_by_title(title: str):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {title}")

@app.post("/api/todo", response_model=Todo)
async def post_todo(todo: Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@app.put("/api/todo/{title}", response_model=Todo)
async def put_todo(title: str, payload: TodoUpdate):
    response = await update_todo(title, payload.desc)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {title}")

@app.delete("/api/todo/{title}")
async def delete_todo(title: str):
    response = await remove_todo(title)
    if response:
        return {"message": "Successfully deleted todo"}
    raise HTTPException(404, f"There is no todo with the title {title}")

# AWS Lambda entrypoint
handler = Mangum(app)
