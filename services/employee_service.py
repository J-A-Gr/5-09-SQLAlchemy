from models.employee import Darbuotojas
from models.duties import Pareigos
from sqlalchemy.exc import IntegrityError

def get_all_employees(session):
    return session.query(Darbuotojas).all()

def create_employee(session, vardas, pavarde, gimimo_data, atlyginimas, darboviete_id, pareigos_id):
    try:
        darbuotojas = Darbuotojas(
            vardas=vardas,
            pavarde=pavarde,
            gimimo_data=gimimo_data,
            atlyginimas=atlyginimas,
            darboviete_id=darboviete_id
        )
        pareigos = session.get(Pareigos, pareigos_id)
        darbuotojas.duties.append(pareigos)

        session.add(darbuotojas)
        session.commit()
        return darbuotojas

    except IntegrityError as e:
        session.rollback()
        raise ValueError(f"Duomenų bazės klaida: {e.orig}")
    except Exception as e:
        session.rollback()
        raise RuntimeError(f"Nenumatyta klaida: {str(e)}")

def update_employee_salary(session, employee_id, new_salary):
    darbuotojas = session.get(Darbuotojas, employee_id)
    if not darbuotojas:
        raise ValueError("Darbuotojas nerastas.")
    darbuotojas.atlyginimas = new_salary
    session.commit()
    return darbuotojas

def delete_employee(session, employee_id):
    darbuotojas = session.get(Darbuotojas, employee_id)
    if not darbuotojas:
        raise ValueError("Darbuotojas nerastas.")
    session.delete(darbuotojas)
    session.commit()