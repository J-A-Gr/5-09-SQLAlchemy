from models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Departamentas(Base):
    __tablename__ = "departamentai"
    id = Column(Integer, primary_key=True, autoincrement=True)
    pavadinimas = Column(String(50), nullable=False)
    aktyvus = Column(Boolean, default=True, nullable=False)


    employees = relationship("Darbuotojas", back_populates="departament")