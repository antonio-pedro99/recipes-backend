from fastapi import FastAPI
from routes.user import user
from routes.recipes import recipe
from config.db import database

app = FastAPI()
app.include_router(user)
app.include_router(recipe)

@app.get("/")
def root():
    return {"home"}

@app.on_event("startup")
async def startup():
    pass

@app.on_event("shutdown")
async def shutdwon():
    pass