from fastapi import APIRouter
from config.db import conn
from models.users import users
from schemas.user import UserIn
from cryptography.fernet import Fernet

user = APIRouter()

key = Fernet.generate_key()
fern = Fernet(key)

@user.get("/users")
def get_user():
    return conn.execute(users.select()).fetchall()

@user.post("/users/")
async def create_user(user: UserIn):
    new_user = {"uname": user.uname, "email": user.email}
    new_user["password"] = fern.encrypt(user.password.encode("utf-8"))
    result = conn.execute(users.insert().values(new_user))
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()
    