from pydantic import BaseModel
from typing import List, Optional

class Recipe(BaseModel):
    title:str
    description:str
    author:Optional[int]
    ingredients:str
    steps:str
    images:str