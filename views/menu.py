from views.employee_view import (
    add_employee_view,
    view_employees_view,
    update_employee_view,
    delete_employee_view
)
from views.company_view import add_company_view
from views.duties_view import add_duties_view
from views.departament_view import add_departament_view
from database import get_session


def main_menu():
    while True:
        print("\n--- DARBUOTOJŲ VALDYMAS ---")
        print("1. Pridėti darbovietę")
        print("2. Pridėti pareigas")
        print("3. Pridėti darbuotoją")
        print("4. Peržiūrėti visus darbuotojus")
        print("5. Atnaujinti darbuotojo atlyginimą")
        print("6. Ištrinti darbuotoją")
        print("7. Pridėti departamentą")
        print("0. Išeiti")
        choice = input("Pasirinkite: ")

        with get_session() as session:
            try:
                if choice == "1":
                    add_company_view(session)
                elif choice == "2":
                    add_duties_view(session)
                elif choice == "3":
                    add_employee_view(session)
                elif choice == "4":
                    view_employees_view(session)
                elif choice == "5":
                    update_employee_view(session)
                elif choice == "6":
                    delete_employee_view(session)
                elif choice == "7":
                    add_departament_view(session)
                    input("Spauskite Enter, kad tęstumėte...")
                elif choice == "0":
                    print("CLI END. BYE BYE...")
                    break
                else:
                    print("Neteisingas pasirinkimas.")
            except Exception as e:
                print(f"Klaida: {str(e)}")

        input("\nSpauskite Enter, kad tęstumėte...")
