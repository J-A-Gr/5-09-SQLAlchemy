
from models.department import Departamentas
from sqlalchemy.exc import IntegrityError

def get_all_departments(session):
    return session.query(Departamentas).all()

def create_department(session, pavadinimas, aktyvus=True):
    try:
        department = Departamentas(
            pavadinimas=pavadinimas,
            aktyvus=aktyvus
        )
        session.add(department)
        session.commit()
        return department
    except IntegrityError as e:
        session.rollback()
        raise ValueError(f"Duomenų bazės klaida: {e.orig}")
    except Exception as e:
        session.rollback()
        raise RuntimeError(f"Nenumatyta klaida: {str(e)}")

def delete_department(session, department_id):
    department = session.get(Departamentas, department_id)
    if not department:
        raise ValueError("Departamentas nerastas.")
    session.delete(department)
    session.commit()
