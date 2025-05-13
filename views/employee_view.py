from services.employee_service import add_darbuotojas, view_darbuotojai, update_darbuotojas, delete_darbuotojas, prideti_darboviete, prideti_pareigas
from database import get_session


def main_menu():  # CLI (Command line interface)
    while True:
        print("\n--- DARBUOTOJŲ VALDYMAS ---")
        print("1. Pridėti darbovietę")
        print("2. Pridėti pareigas")
        print("3. Pridėti darbuotoją")
        print("4. Peržiūrėti visus")
        print("5. Atnaujinti darbuotoją")
        print("6. Ištrinti darbuotoją")
        print("0. Išeiti")
        choice = input("Pasirinkite: ")

        with get_session() as session:
            if choice == "1":
                prideti_darboviete(session)
                input()
            elif choice == "2":
                prideti_pareigas(session)
                input()
            elif choice == "3":
                add_darbuotojas(session)
                input()
            elif choice == "4":
                view_darbuotojai(session)
                input()
            elif choice == "5":
                update_darbuotojas(session)
                input()
            elif choice == "6":
                delete_darbuotojas(session)
                input()
            elif choice == "0":
                print("Command line interface pabaiga...")
                break
            else:
                print("Neteisingas pasirinkimas.")
