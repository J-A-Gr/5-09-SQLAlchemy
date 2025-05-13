from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Darboviete(Base):
    __tablename__ = "darbovietes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    pavadinimas = Column(String(50), nullable=False)
    miestas = Column(String(50), nullable=False)

    employees = relationship("Darbuotojas", back_populates="company")