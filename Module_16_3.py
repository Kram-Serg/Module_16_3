from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()

users = {'1':'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_users():
    return users


@app.post('/user/{username}/{age}')
async def get_user(username: Annotated[str, Path(min_length=3,
                                                 max_length=20,
                                                 description='Enter Username',
                                                 example='Ilya')],
                   age: Annotated[int, Path(ge=18, le=120,
                                            description='Enter User age',
                                            example='24')] ):
    user_id = int(max(users.keys())) + 1 if users else 1
    new_user = {str(user_id): f'Имя: {username}, возраст: {age}'}
    users.update(new_user)
    return f'User {user_id} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1,
                                                   le=100,
                                                   description='Enter User ID',
                                                   example='12')],
                      username: Annotated[str, Path(min_length=3,
                                                 max_length=20,
                                                 description='Enter Username',
                                                 example='Ilya')],
                   age: Annotated[int, Path(ge=18, le=120,
                                            description='Enter User age',
                                            example='24')] ):
    for u_id in users:
        if int(u_id) == user_id:
            users[u_id] = f'Имя: {username}, возраст: {age}'
            return f'The user {user_id} is updated'


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1,
                                                   le=100,
                                                   description='Enter User ID',
                                                   example='12')]):
    for u_id in users:
        if int(u_id) == user_id:
            del users[u_id]
            return f'User {user_id} has been deleted'
