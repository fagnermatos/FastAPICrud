from sqlalchemy.orm import Session

from . import models, database, schemas


class PersonRepository:

    def __init__(self) -> None:
        super().__init__()
        self.db: Session = database.get_db().__next__()

    def find_by(self, id: str):
        return self.db.query(models.Person).filter(models.Person.id == id).first()

    def count(self):
        return self.db.query(models.Person).count()

    def search(self, filter: str):
        query = f'%{filter}%'
        return self.db.query(models.Person).filter(
            (models.Person.apelido.ilike(query))
            | (models.Person.nome.ilike(query))
            # | (models.Person.stack == query)
        ).all()

    def save(self, person: schemas.Person):
        model = models.Person(
            apelido=person.apelido,
            nome=person.nome,
            nascimento=person.nascimento,
            # stack=person.stack,
        )
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return model
