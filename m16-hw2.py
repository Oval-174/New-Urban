#m16-hw2 "Аннотация и валидация"
from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def main_message() -> dict:
    return {'message': 'Главная страница'}

@app.get("/user/{username}/{age}")
async def user_age(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                   age: int = Path(ge=18, le=120, description='Enter age', example='24')) -> dict:
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}

@app.get("/user/admin")
async def user_admin() -> dict:
    return {'message': 'Вы вошли как администратор'}

@app.get("/user/{user_id}")
async def user_id(user_id: int = Path(ge=1, le=100, description='Enter User ID', example='18')) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}

