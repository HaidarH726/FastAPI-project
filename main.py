from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()

# file constant
TASKS_FILE = "tasks.txt"

# models
class Task(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool = False


class TaskCreate(BaseModel):
    title: str
    description: str | None = None


# file functions
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    
    tasks = []
    with open(TASKS_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                tasks.append(json.loads(line))
    return tasks


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(json.dumps(task) + "\n")


# endpoints
@app.get("/")
def root():
    return {"message": "Task API is running"}
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")


@app.get("/tasks")
def get_tasks(completed: bool | None = None):
    tasks = load_tasks()

    if completed is None:
        return tasks

    return [task for task in tasks if task["completed"] == completed]
@app.post("/tasks")
def create_task(task: TaskCreate):
    tasks = load_tasks()

    new_id = 1 if not tasks else max(t["id"] for t in tasks) + 1

    new_task = {
        "id": new_id,
        "title": task.title,
        "description": task.description,
        "completed": False
    }

    tasks.append(new_task)
    save_tasks(tasks)

    return new_task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated: TaskCreate):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["title"] = updated.title
            task["description"] = updated.description
            save_tasks(tasks)
            return task

    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    tasks = load_tasks()

    new_tasks = [task for task in tasks if task["id"] != task_id]

    if len(new_tasks) == len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")

    save_tasks(new_tasks)
    return {"message": "Task deleted"}

@app.delete("/tasks")
def delete_all_tasks():
    save_tasks([])
    return {"message": "All tasks deleted"}

@app.get("/tasks/stats")
def task_stats():
    tasks = load_tasks()

    total = len(tasks)
    completed = sum(1 for t in tasks if t["completed"])
    pending = total - completed
    percentage = (completed / total * 100) if total > 0 else 0

    return {
        "total_tasks": total,
        "completed_tasks": completed,
        "pending_tasks": pending,
        "completion_percentage": percentage
    }