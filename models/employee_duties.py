from sqlalchemy import Column, ForeignKey, Integer, Table
from models.base import Base





employee_duties = Table(
    "darbuotojo_pareigos",
    Base.metadata,
    Column("darbuotojas_id", Integer, ForeignKey("darbuotojai.id"), primary_key=True),
    Column("pareigos_id", Integer, ForeignKey("pareigos.id"), primary_key=True),
)