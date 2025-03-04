from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from database import get_db
from typing import Optional

app = FastAPI()



class TaskScheme(BaseModel):
    id: int
    name: str
    des: str
    priority: Optional[int] = None

class UpdateTaskScheme(BaseModel):
    name: Optional[str] = None
    des: Optional[str] = None
    priority: Optional[int] = None

class TaskResponse(BaseModel):
    message: str
    values: Optional[list] = None

@app.get("/")
async def root():
    return {"message": "# Welcome to To-do List\nYou can add, get, update, delete"}

@app.post("/items", response_model=TaskResponse)
async def add_item(task: TaskScheme, cursor=Depends(get_db)):
    cols = ["id", "name", "des"]
    values = [task.id, task.name, task.des]
    if task.priority is not None:
        cols.append("priority")
        values.append(task.priority)
    command = f"INSERT INTO to_do ({', '.join(cols)}) VALUES ({', '.join(['%s'] * len(values))})"
    cursor.execute(command, values)
    cursor.connection.commit()
    return {"message": "Added an item", "values": values}

@app.get("/items", response_model=TaskResponse)
async def get_items(cursor=Depends(get_db)):
    cursor.execute("SELECT * FROM to_do")
    results = cursor.fetchall()
    if not results:
        raise HTTPException(status_code=404, detail="No tasks found")
    return {"message": "Fetched the entire to-do list", "values": results}

@app.get("/items/{item_id}", response_model=TaskResponse)
async def get_item(item_id: int, cursor=Depends(get_db)):
    cursor.execute("SELECT * FROM to_do WHERE id = %s", (item_id,))
    result = cursor.fetchall()
    if not result:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Fetched a single task", "values": result}

@app.put("/items/{item_id}", response_model=TaskResponse)
async def update_item(item_id: int, item: UpdateTaskScheme, cursor=Depends(get_db)):
    update_fields = []
    values = []
    if item.name:
        update_fields.append("name = %s")
        values.append(item.name)
    if item.des:
        update_fields.append("des = %s")
        values.append(item.des)
    if item.priority is not None:
        update_fields.append("priority = %s")
        values.append(item.priority)
    if not update_fields:
        return {"message": "No fields to update"}
    values.append(item_id)
    command = f"UPDATE to_do SET {', '.join(update_fields)} WHERE id = %s"
    cursor.execute(command, values)
    cursor.connection.commit()
    cursor.execute("SELECT * FROM to_do WHERE id = %s", (item_id,))
    updated_task = cursor.fetchall()
    return {"message": "Updated an item", "values": updated_task}

@app.delete("/items/{item_id}", response_model=TaskResponse)
async def delete_item(item_id: int, cursor=Depends(get_db)):
    cursor.execute("DELETE FROM to_do WHERE id = %s", (item_id,))
    cursor.connection.commit()
    return {"message": "Deleted an item"}
