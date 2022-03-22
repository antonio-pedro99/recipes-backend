from config.db import meta, engine
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import *

users = Table(
    "Users",
    meta,
    Column("id", Integer, primary_key=True),
    Column("uname", String(255)),
    Column("email", String(255)),
    Column("password", String(255))
)
meta.create_all(engine)