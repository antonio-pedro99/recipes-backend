from config.db import meta, engine
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import *


recipes = Table(
    "recipes",
    meta,
    Column("id", Integer, primary_key=True),
    Column("title", String(255),unique=True, nullable=False),
    Column("description", String(255),),
    Column("author", Integer, ForeignKey("users.id"), nullable=False),
    Column("ingredients", String(1024), nullable=True),
    Column("steps", String(1024), nullable=False),
    Column("images", String(255), nullable=False)
    #foreign key (author) references users(id)
)
    
meta.create_all(engine)