from typing import List
from sqlalchemy.orm import Session
from src.models.user_model import User
from src.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db)

    def add(self, entity) -> None:
        self._db.add(entity)
        self._db.commit()

    def create(self, user: User) -> User:
        self.add(user)
        self._db.refresh(user)
        return user

    def get(self, user_id: int) -> User:
        return self._db.query(User).filter(User.id == user_id).first()

    def get_all(self) -> List[User]:
        return self._db.query(User).all()

    def update(self, user_id: int, user: User) -> User:
        user_in_db = self._db.query(User).filter(User.id == user_id).first()
        if user_in_db:
            user_dict = user.dict(exclude_unset=True)
            for key, value in user_dict.items():
                setattr(user_in_db, key, value)
            self._db.commit()
            self._db.refresh(user_in_db)
            return user_in_db

    def delete(self, user_id: int) -> bool:
        user = self._db.query(User).filter(User.id == user_id).first()
        if user:
            self._db.delete(user)
            self._db.commit()
            return True
        return False
