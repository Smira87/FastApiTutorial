from sqlalchemy import MetaData, Table, Column, TIMESTAMP, Integer, String, ForeignKey, JSON
from datetime import datetime

metaData = MetaData()

roles = Table(
    "roles",
    metaData,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

users = Table(
    "users",
    metaData,
    Column("id", Integer, primary_key=True),
    Column("email", String),
    Column("usernam", String, nullable=False),
    Column("password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("role_id", Integer, ForeignKey("roles.id")),
)

