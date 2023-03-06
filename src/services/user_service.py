from typing import List
from src.models.user_model import User
from src.repositories.user_repository import UserRepository
from src.models.user_model import User


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user: User) -> User:
        return self.user_repository.create(user)

    def get_users(self, user_id: int) -> User:
        return self.user_repository.get(user_id)

    def get_all_users(self) -> List[User]:
        return self.user_repository.get_all()

    def update_user(self, user_id: int, user: User) -> User:
        return self.user_repository.update(user_id, user)

    def delete_user(self, user_id: int) -> bool:
        return self.user_repository.delete(user_id)
