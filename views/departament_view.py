from services.departament_service import create_department

def add_departament_view(session):
    try:
        pavadinimas = input("Įveskite departamento pavadinimą: ").strip()
        aktyvus_input = input("Ar aktyvus? (1 = taip, 0 = ne): ").strip()
        aktyvus = aktyvus_input != "0"

        department = create_department(
            session,
            pavadinimas=pavadinimas,
            aktyvus=aktyvus
        )

        print(f"Departamentas pridėtas: {department.pavadinimas}")

    except Exception as e:
        print(f"Klaida: {e}")
