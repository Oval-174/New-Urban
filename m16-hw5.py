#m16-hw5 "Список пользователей в шаблоне"
from fastapi import FastAPI, status, Body, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

users = []
user = {"id": 1, "username": "user", "age": 15}
users.append(user)

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get("/")
def all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get("/users/{user_id}")
def one_user(request: Request, user_id: int) -> HTMLResponse:
    for u in users:
        if u["id"] == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": u})
    return HTMLResponse(status_code=404, content="User not found")
@app.post("/user/{username}/{age}")
def new_user(username: str, age: int) -> dict:
    if len(users) == 0:
        user_id = 1
    else:
        user = users[-1]
        user_id = user['id'] + 1
    user = {'id': user_id, 'username': username, 'age': age}
    users.append(user)
    return user

@app.put("/user/{user_id}/{username}/{age}")
def edit_user(user_id: int, username: str, age: int) -> dict:
    try:
        for i in range(0, len(users)):
            user = users[i]
            if user_id == user['id']:
                user = {'id': user_id, 'username': username, 'age': age}
                users[i] = user
                return user
        return users[len(users)]
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}")
def delete_user(user_id: int) -> dict:
    try:
        for i in range(0, len(users) - 1):
            user = users[i]
            if user_id == user['id']:
                users.pop(i)
                return user
        return users[len(users)]
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")