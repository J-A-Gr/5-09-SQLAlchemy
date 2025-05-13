from services.company_service import get_all_companies, add_company

def add_company_view(session):
    try:
        existing = get_all_companies(session)
        if existing:
            print("\nGalimos darbovietės:")
            for d in existing:
                print(f"{d.id}: {d.pavadinimas}, {d.miestas}")

        pavadinimas = input("Įveskite darbovietės pavadinimą: ").strip()
        if not pavadinimas:
            print("Darbovietė nebuvo pridėta.")
            return
        miestas = input("Įveskite darbovietės miestą: ").strip() or None

        darboviete = add_company(session, pavadinimas, miestas)
        print(f"[{darboviete.id}] ID | {darboviete.pavadinimas}. Darbovietė pridėta.")

    except Exception as e:
        print(f"Klaida: {str(e)}")
