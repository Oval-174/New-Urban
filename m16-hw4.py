#m16-hw3 "Имитация работы с БД"
from fastapi import FastAPI, Path, status, Body, HTTPException
from typing import Annotated
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []

class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users")
def all_users() -> List[User]:
    return users

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
        for i in range(0, len(users) - 1):
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
