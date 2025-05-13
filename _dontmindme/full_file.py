from sqlalchemy import create_engine, Column, Integer, String, Date, DateTime
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from datetime import datetime, date
from tabulate import tabulate

engine = create_engine("mysql://root:915276MySQL@localhost:3306/0509sqlalchemy_classwork")

class Base(DeclarativeBase):
    pass

class Darbuotojas(Base):
    __tablename__ = "darbuotojai"
    id = Column(Integer, primary_key=True, autoincrement=True)
    vardas = Column(String(50))
    pavarde = Column(String(50))
    gimimo_data = Column(Date)
    pareigos = Column(String(100), nullable=True)
    atlyginimas = Column(Integer)
    nuo_kada_dirba = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Crud sistema, create, read ,update, delete

def add_darbuotojas(session):
    vardas = input("Vardas: ")
    pavarde = input("Pavardė: ")
    gimimo_data_str = input("Gimimo data (YYYY-MM-DD): ")
    gimimo_data = date.fromisoformat(gimimo_data_str)
    pareigos = input("Pareigos (palik tuščią jei nėra): ") or None
    atlyginimas = int(input("Atlyginimas: "))

    darbuotojas = Darbuotojas(
        vardas=vardas,
        pavarde=pavarde,
        gimimo_data=gimimo_data,
        pareigos=pareigos,
        atlyginimas=atlyginimas
    )
    session.add(darbuotojas)
    session.commit()
    print("Darbuotojas pridėtas.")

def view_darbuotojai(session):
    darbuotojai = session.query(Darbuotojas).all()

        # Paruošiam duomenis kaip sąrašą sąrašų (rows)
    table = []
    for d in darbuotojai:
        table.append([
            d.id,
            d.vardas,
            d.pavarde,
            d.gimimo_data,
            d.pareigos or "—",   # jei None – rodom brūkšnelį
            d.atlyginimas,
            d.nuo_kada_dirba.strftime('%Y-%m-%d %H:%M')
        ])

    # Lentelės stulpelių pavadinimai
    headers = ["ID", "Vardas", "Pavardė", "Gimimo data", "Pareigos", "Atlyginimas", "Dirba nuo"]

    # Spausdinam gražiai
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

def update_darbuotojas(session):
    id = int(input("Įveskite darbuotojo ID, kurį norite atnaujinti: "))
    d = session.query(Darbuotojas).filter_by(id=id).first()
    if not d:
        print("Darbuotojas nerastas.")
        return
    d.pareigos = input(f"Naujos pareigos (buvo: {d.pareigos}): ") or d.pareigos  # or d.pareigos, palieka sena reiksme jeigu vartotojas neiveda nieko, tik enter spaudzia. or operatorius ne tik sulygina, bet ir pasirenka vertę
    d.atlyginimas = int(input(f"Naujas atlyginimas (buvo: {d.atlyginimas}): ") or d.atlyginimas) # 'or' --> jeigu value "" - false(falsy), jeigu " " ar "Vadovas" - true(truthy). Under the hood momentai
    session.commit()
    print("Darbuotojas atnaujintas.")

def delete_darbuotojas(session):
    id = int(input("Įveskite darbuotojo ID, kurį norite ištrinti: "))
    d = session.query(Darbuotojas).filter_by(id=id).first()
    if not d:
        print("Darbuotojas nerastas.")
        return
    session.delete(d)
    session.commit()
    print("Darbuotojas ištrintas.")

def main_menu():  # CLI meniu, Command line interface
    while True:
        print("\n--- DARBUOTOJŲ VALDYMAS ---")
        print("1. Pridėti darbuotoją")
        print("2. Peržiūrėti visus")
        print("3. Atnaujinti darbuotoją")
        print("4. Ištrinti darbuotoją")
        print("5. Išeiti")
        choice = input("Pasirinkite: ")

        with Session() as session:
            if choice == "1":
                add_darbuotojas(session)
            elif choice == "2":
                view_darbuotojai(session)
                input()
            elif choice == "3":
                update_darbuotojas(session)
            elif choice == "4":
                delete_darbuotojas(session)
            elif choice == "5":
                print("CLI meniu pabaiga...")
                break
            else:
                print("Neteisingas pasirinkimas.")

main_menu()