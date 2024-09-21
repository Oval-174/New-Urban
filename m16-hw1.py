#m16-hw1 "Начало пути"
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def main_message() -> dict:
    return {'message': 'Главная страница'}

@app.get("/user")
async def user_age(username: str, age: int) -> dict:
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}

@app.get("/user/admin")
async def user_admin() -> dict:
    return {'message': 'Вы вошли как администратор'}

@app.get("/user/{user_id}")
async def user_id(user_id: int) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}

