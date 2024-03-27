import json
from abc import update_abstractmethods
from copy import copy
from typing import Optional

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

task_list = [
    {
        "id": 0,
        "title": "Task1",
        "content": "Task1 content",
        "is_deleted": False,
    },
    {
        "id": 1,
        "title": "Task2",
        "content": "Task2 content",
        "is_deleted": False,
    },
]


class Task(BaseModel):
    id: Optional[int] = None
    title: str
    content: Optional[str] = None
    is_deleted: bool = False


@app.get("/tasks")
async def get_task_list():
    validated_data = [Task(**task) for task in task_list]
    data = [task.model_dump() for task in validated_data]
    return JSONResponse(content=data, status_code=200)


@app.get("/tasks/{id}")
async def get_task(id: int):
    validated_task = Task(**task_list[id])
    data = validated_task.model_dump()
    return JSONResponse(content=data, status_code=200)


@app.post("/tasks")
async def create_task(task: Task):
    task.id = len(task_list)
    data = task.model_dump()
    task_list.append(data)
    return JSONResponse(content=data, status_code=201)


@app.put("/tasks/{id}")
async def update_task(id: int, task: Task):
    updated_task = task_list[id]
    if task.title is not None:
        updated_task["title"] = task.title
    if task.content is not None:
        updated_task["content"] = task.content
    validated_task = Task(**updated_task)
    data = validated_task.model_dump()
    task_list.insert(id, data)
    task_list.pop(id + 1)
    return JSONResponse(content=data, status_code=200)


@app.delete("/tasks/{id}")
async def delete_task(id: int):
    task = task_list[id]
    task["is_deleted"] = True
    validated_task = Task(**task)
    data = validated_task.model_dump()
    return JSONResponse(content=data, status_code=200)
