from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base
from models.employee_duties import employee_duties

class Pareigos(Base):
    __tablename__ = "pareigos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    pavadinimas = Column(String(50), nullable=False)
    aprasymas = Column(String(200), nullable=True)

    employees = relationship("Darbuotojas", secondary=employee_duties, back_populates="duties")
