"""Файл для связи с Бд"""
from datetime import datetime

from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column, JSON

metadata = MetaData()

roles = Table(
    "roles",  # Создаём таблицу roles
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permission", JSON),
)

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("role_id", Integer, ForeignKey("roles.id")),
)



