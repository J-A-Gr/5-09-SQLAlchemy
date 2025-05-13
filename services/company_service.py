from models.company import Darboviete
from sqlalchemy.exc import IntegrityError

def get_all_companies(session):
    return session.query(Darboviete).all()

def add_company(session, pavadinimas, miestas):
    try:
        darboviete = Darboviete(pavadinimas=pavadinimas, miestas=miestas)
        session.add(darboviete)
        session.commit()
        return darboviete
    except IntegrityError as e:
        session.rollback()
        raise ValueError(f"DB klaida: {e.orig}")
    except Exception as e:
        session.rollback()
        raise RuntimeError(f"Klaida: {str(e)}")
