from pydantic import BaseModel
from typing import Optional

class UserIn(BaseModel):
    email: str
    uname: str
    password: str