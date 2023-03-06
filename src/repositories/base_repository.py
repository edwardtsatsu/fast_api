from typing import List
from sqlalchemy.orm import Session

class BaseRepository:
    def __init__(self, db: Session):
        self._db = db

    def create(self, entity) -> None:
        self._db.add(entity)
        self._db.commit()

    def get(self, id: int):
        return self._db.query(self.model).get(id)

    def get_all(self) -> List:
        return self._db.query(self.model).all()

    def update(self, entity) -> None:
        self._db.merge(entity)
        self._db.commit()

    def delete(self, entity) -> None:
        self._db.delete(entity)
        self._db.commit()
