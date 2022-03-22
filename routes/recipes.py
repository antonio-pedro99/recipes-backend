from unittest import result
from fastapi import APIRouter
from config.db import conn
from models.users import users
from models.recipes import recipes
from schemas.recipe import Recipe


recipe = APIRouter()


@recipe.get("/recipes", description="", tags= ["Recipe"])
def get_recipe():
    return conn.execute("select * from recipes").fetchall()

@recipe.post("/recipes/", tags= ["Recipe"])
def create_recipe(recipe:Recipe):
    new_recipe = {
        "title": recipe.title, 
        "description":recipe.description, 
        "author": recipe.author,
        "steps": recipe.steps,
        "images":recipe.images}
    result = conn.execute(recipes.insert().values(new_recipe))

    return conn.execute(recipes.select().where(recipes.c.id == result.lastrowid)).first()