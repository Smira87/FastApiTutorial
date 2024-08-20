from sqlalchemy import MetaData, Table, Column, TIMESTAMP, Integer, String, ForeignKey, JSON

metaData = MetaData()

roles = Table(
    "roles",
    metaData,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)