from services.employee_service import (
    get_all_employees,
    create_employee,
    update_employee_salary,
    delete_employee
)
from services.company_service import get_all_companies
from services.duties_service import get_all_duties
from datetime import date
from tabulate import tabulate

def add_employee_view(session):
    try:
        darbovietes = get_all_companies(session)
        pareigos_list = get_all_duties(session)

        if not darbovietes:
            print("Nėra darboviečių. Pirmiausia pridėkite bent vieną.")
            return
        if not pareigos_list:
            print("Nėra pareigų. Pirmiausia pridėkite bent vienas.")
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

        print("\nGalimos pareigos:")
        for p in pareigos_list:
            print(f"{p.id}: {p.pavadinimas} - {p.aprasymas or 'Nėra aprašymo'}")
        pareigos_id = int(input("Pasirinkite pareigų ID: "))

        darbuotojas = create_employee(session, vardas, pavarde, gimimo_data, atlyginimas, darboviete_id, pareigos_id)
        print(f"Darbuotojas pridėtas: {darbuotojas.vardas} {darbuotojas.pavarde}")

    except Exception as e:
        print(str(e))

def view_employees_view(session):
    try:
        darbuotojai = get_all_employees(session)
        table = [
            [
                d.id,
                d.vardas,
                d.pavarde,
                d.gimimo_data,
                d.atlyginimas or "—",
                d.darboviete_id,
                d.nuo_kada_dirba.strftime('%Y-%m-%d %H:%M')
            ]
            for d in darbuotojai
        ]
        headers = ["ID", "Vardas", "Pavardė", "Gimimo data", "Atlyginimas", "Darbovietės ID", "Dirba nuo"]
        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

    except Exception as e:
        print(f"Klaida rodant darbuotojus: {str(e)}")

def update_employee_view(session):
    try:
        id = int(input("Įveskite darbuotojo ID: "))
        new_salary = int(input("Naujas atlyginimas: "))
        darbuotojas = update_employee_salary(session, id, new_salary)
        print(f"Atlyginimas atnaujintas: {darbuotojas.vardas} {darbuotojas.pavarde}")
    except Exception as e:
        print(str(e))

def delete_employee_view(session):
    try:
        id = int(input("Įveskite darbuotojo ID, kurį norite ištrinti: "))
        delete_employee(session, id)
        print("Darbuotojas ištrintas.")
    except Exception as e:
        print(str(e))
