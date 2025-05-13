from models.duties import Pareigos
from sqlalchemy.exc import IntegrityError


def get_all_duties(session):
    return session.query(Pareigos).all()


def create_duties(session, pavadinimas, aprasymas=None):
    try:
        pareigos = Pareigos(pavadinimas=pavadinimas, aprasymas=aprasymas)
        session.add(pareigos)
        session.commit()
        return pareigos
    except IntegrityError as e:
        session.rollback()
        raise ValueError(f"DB klaida: {e.orig}")
    except Exception as e:
        session.rollback()
        raise RuntimeError(f"Klaida: {str(e)}")