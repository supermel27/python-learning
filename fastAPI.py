from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}


@app.get("/items")
def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}


#Pydantic — модели данных
class User(BaseModel):
    name: str
    age: int
    email: str


@app.post("/users")
def create_user(user: User):
    return {"message": f"Создан пользователь {user.name}", "user": user}


#Пример с обработкой ошибок

users = {
    1: {"name": "Serg", "age": 35},
    2: {"name": "Alex", "age": 23},
}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not founded")
    return users[user_id]


#Полный пример: TODO API

class Todo(BaseModel):
    title: str
    done: bool = False

class TodoCreate(BaseModel):
    title: str

todos: dict[int, dict] = {}
next_id = 1

@app.get("/todos")
def list_todos():
    return list(todos.values())


@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    if todo_id not in todos:
        raise HTTPException(404, "Task not found")
    return todos[todo_id]


@app.post("/todos", status_code=201)
def create_todo(data: TodoCreate):
    global next_id
    todo = {"id": next_id, "title": data.title, "done": False}
    todos[next_id] = todo
    next_id += 1
    return todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    if todo_id not in todos:
        raise HTTPException(404, "Task not found")
    del todos[todo_id]
    return {"message": "Deleted"}