from typing import List
from src.models.user_model import User
from src.repositories.user_repository import UserRepository
from sqlalchemy.orm import Session


class UserService:
    def __init__(self, db_session: Session):
        self.repository = UserRepository(db_session)

    def create_user(self, user: User) -> User:
        return self.repository.create(user)

    def get_users(self, user_id: int) -> User:
        return self.repository.get(user_id)

    def get_all_users(self) -> List[User]:
        return self.repository.get_all()

    def update_user(self, user_id: int, user: User) -> User:
        return self.repository.update(user_id, user)

    def delete_user(self, user_id: int) -> bool:
        return self.repository.delete(user_id)
