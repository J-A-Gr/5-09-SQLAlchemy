from models.employee import Darbuotojas
from models.company import Darboviete
from models.duties import Pareigos
from datetime import date
from tabulate import tabulate
from sqlalchemy.exc import IntegrityError

def add_darbuotojas(session):

    try:
        darbovietes = session.query(Darboviete).all()
        if not darbovietes:
            print("Nėra darboviečių. Pirmiausia pridėkite bent vieną darbovietę.")
            return

        pareigos_list = session.query(Pareigos).all()
        if not pareigos_list:
            print("Nėra pareigų. Pirmiausia pridėkite bent vienas pareigas.")
            return


        print("\nGalimos darbovietės:")
        for d in darbovietes:
            print(f"{d.id}: {d.pavadinimas}, {d.miestas}")
        darboviete_id = int(input("Pasirinkite darbovietės ID: "))

        vardas = input("Vardas: ") or None
        pavarde = input("Pavardė: ") or None
        gimimo_data_str = input("Gimimo data (YYYY-MM-DD): ") or None
        gimimo_data = date.fromisoformat(gimimo_data_str) if gimimo_data_str else None
        atlyginimas_input = input("Atlyginimas: ")
        atlyginimas = int(atlyginimas_input) if atlyginimas_input else None

        darbuotojas = Darbuotojas(
            vardas=vardas,
            pavarde=pavarde,
            gimimo_data=gimimo_data,
            atlyginimas=atlyginimas,
            darboviete_id=darboviete_id
        )
        # darbuotojo priskirimo funkcijos meniu (--> many to many)

        print("\nGalimos pareigos:")
        for p in pareigos_list:
            print(f"{p.id}: {p.pavadinimas} - {p.aprasymas or 'Nėra aprašymo'}")
        pareigos_id = int(input("Pasirinkite pareigų ID: "))
        pareigos = session.get(Pareigos, pareigos_id)

        darbuotojas.duties.append(pareigos)

        session.add(darbuotojas)
        session.commit()
        print("Darbuotojas sėkmingai pridėtas.")

    except ValueError:
        print("Įvesta netinkama reikšmė. Patikrinkite skaičius ir datas.")
    except IntegrityError as e:
        session.rollback()
        print(f"Duomenų bazės klaida: {e.orig}")
    except Exception as e:
        session.rollback()
        print(f"Nenumatyta klaida: {str(e)}")

def view_darbuotojai(session):
    try:
        darbuotojai = session.query(Darbuotojas).all()

            # Paruošiam duomenis kaip sąrašą sąrašų (rows)
        table = []
        for d in darbuotojai:
            table.append([
                d.id,
                d.vardas,
                d.pavarde, 
                d.gimimo_data,
                d.atlyginimas or "—",   # jei None – rodom brūkšnelį
                d.darboviete_id,
                d.nuo_kada_dirba.strftime('%Y-%m-%d %H:%M')
            ])

        # Lentelės stulpelių pavadinimai
        headers = ["ID", "Vardas", "Pavardė", "Gimimo data", "Atlyginimas", "Darbovietės ID", "Dirba nuo"]

        # Spausdinam gražiai
        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

    except Exception as e:
        print(f"Klaida rodant darbuotojus: {str(e)}")

def update_darbuotojas(session):
    try:
        id = int(input("Įveskite darbuotojo ID, kurį norite atnaujinti: "))
        d = session.query(Darbuotojas).filter_by(id=id).first()
        if not d:
            print("Darbuotojas nerastas.")
            return
        # or d.pareigos, palieka sena reiksme jeigu vartotojas neiveda nieko, tik enter spaudzia. or operatorius ne tik sulygina, bet ir pasirenka vertę
        # 'or' --> jeigu value "" - false(falsy), jeigu " " ar "Vadovas" - true(truthy). Under the hood momentai
        d.atlyginimas = int(input(f"Naujas atlyginimas (buvo: {d.atlyginimas}): ") or d.atlyginimas) 
        session.commit()
        print("Darbuotojas atnaujintas.")

    except ValueError:
        print("Įveskite tinkamą skaičių.")
    except IntegrityError as e:
        session.rollback()
        print(f"DB klaida: {e.orig}")
    except Exception as e:
        session.rollback()
        print(f"Nenumatyta klaida: {str(e)}")

def delete_darbuotojas(session):
    try:
        id = int(input("Įveskite darbuotojo ID, kurį norite ištrinti: "))
        d = session.query(Darbuotojas).filter_by(id=id).first()
        if not d:
            print("Darbuotojas nerastas.")
            return
        session.delete(d)
        session.commit()
        print("Darbuotojas ištrintas.")

    except ValueError:
        print("ID turi būti skaičius.")
    except Exception as e:
        session.rollback()
        print(f"Klaida trynimo metu: {str(e)}")
