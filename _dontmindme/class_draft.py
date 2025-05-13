from sqlalchemy import create_engine, Column, Integer, String, DateTime, select
from sqlalchemy.orm import DeclarativeBase, sessionmaker
 
engine = create_engine("mysql://root:915276MySQL@localhost:3306/test")
 
class Base(DeclarativeBase):
    pass
 
class Device(Base):
    __tablename__ = "device"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    created_at = Column(DateTime)
 
class Shop(Base):
    __tablename__ = "shop"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    created_at = Column(DateTime)
 
Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)

# with Session() as session:
#     new_shop = Shop(name = "TopoCentras")
#     session.add(new_shop)3
#     session.commit()


# with Session() as session:
#     shop = session.get(Shop, 3)
#     if shop:
#         print(shop.name)



# with Session() as session:
#     query = select(Shop) #.filter_by(name = "TopoCentras")
#     # shop = session.execute(query).scalar_one()
#     shops = session.execute(query).scalars().all()

#     for shop in shops:
#         print(shop.id, shop.name)



# with Session() as session:
#     query = select(Shop).where(Shop.id > 2)
#     shops = session.execute(query).scalars().all()

#     for shop in shops:
#         print(shop.id, shop.name)



# with Session() as session:
#     query = select(Shop).where(Shop.name.ilike("T%"))
#     shops = session.execute(query).scalars().all()

#     for shop in shops:
#         print(shop.id, shop.name)



with Session() as session:
    query = select(Shop).filter_by(name = "Elektromartk")
    shops = session.execute(query).scalars().all()

    for shop in shops:
        print(shop.id, shop.name)
        shop.name = "Elektromarkt"
        session.commit()