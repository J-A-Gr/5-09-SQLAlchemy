from services.duties_service import get_all_duties, create_duties


def add_duties_view(session):
    try:
        existing = get_all_duties(session)
        if existing:
            print("\nGalimos pareigos:")
            for p in existing:
                print(f"{p.id}: {p.pavadinimas} - {p.aprasymas or 'Nėra aprašymo'}")

        pavadinimas = input("Įveskite pareigas: ").strip()
        if not pavadinimas:
            print("Pareigos nebuvo pridėtos.")
            return

        aprasymas = input("Įveskite pareigų atsakomybes: ").strip() or None

        pareigos = create_duties(session, pavadinimas, aprasymas)
        print(f"[{pareigos.id}] ID | {pareigos.pavadinimas}. Naujos pareigos pridėtos.")

    except Exception as e:
        print(f"Klaida: {str(e)}") 