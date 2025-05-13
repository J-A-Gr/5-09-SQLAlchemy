from database import Base
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from models.employee_duties import employee_duties




class Darbuotojas(Base):
    __tablename__ = "darbuotojai"
    id = Column(Integer, primary_key=True, autoincrement=True)
    vardas = Column(String(50))
    pavarde = Column(String(50))
    gimimo_data = Column(Date)
    atlyginimas = Column(Integer)
    pareigos_id = Column(Integer)
    darboviete_id = Column(Integer, ForeignKey("darbovietes.id"), nullable=False)
    nuo_kada_dirba = Column(DateTime, default=datetime.utcnow)


    company = relationship("Darboviete", back_populates="employees")

    duties = relationship("Pareigos", secondary=employee_duties, back_populates="employees")
