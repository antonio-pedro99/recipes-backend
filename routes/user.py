from fastapi import APIRouter, Form
from config.db import conn
from models.users import users
from schemas.user import UserIn
from cryptography.fernet import Fernet


user = APIRouter()

key = Fernet.generate_key()
fern = Fernet(key)

@user.get("/users", tags= ["User"])
def get_users():
    return conn.execute(users.select()).fetchall()

@user.post("/users/", tags= ["User"])
async def create_user(user: UserIn):
    new_user = {"uname": user.uname, "email": user.email}
    new_user["password"] = fern.encrypt(user.password.encode("utf-8"))
    result = conn.execute(users.insert().values(new_user))
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()


@user.get("/users/{user_id}", tags= ["User"])
async def get_user_by_id(user_id):
    return conn.execute(users.select().where(users.c.id == user_id)).first()

""" @user.post("/login/", tags= ["User"])
async def login(email:str = Form(...), password:str = Form(...)):


    return conn.execute(users.select().where()) """