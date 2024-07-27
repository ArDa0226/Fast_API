
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def welcome() -> str:
    return 'Главная страница'


@app.get('/user/admin')
async def admin_enter() -> str:
    return 'Вы вошли как администратор'

@app.get('/user/{user_id}')
async def user_id(user_id: int):
    return f'Вы вошли как пользователь № {user_id}'

@app.get('/user')
async def user_name(username: str, age: int) -> dict:
    return {'Информация о пользователе. Имя:': username, 'Возраст:': age}