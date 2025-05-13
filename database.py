from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.employee import Darbuotojas
from models.company import Darboviete
from models.duties import Pareigos


engine = create_engine("mysql://root:915276MySQL@localhost:3306/0509sqlalchemy_classwork", echo=True)

def create_database():
    Base.metadata.create_all(engine)


def get_session():
    Session = sessionmaker(bind=engine)
    return Session()
                           