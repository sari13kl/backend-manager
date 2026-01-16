from sqlalchemy.orm import Session
import re
from database.models.user import User
from repositories.user_repository import UserRepository
from core.security import hash_password, verify_password


class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def validate_password(self, password: str) -> bool:
        if (len(password) < 8):
            return False
        if not re.search(r'[A-Z]', password):
            return False
        if not re.search(r'[a-z]', password):
            return False
        return True

    def create_user(self, name: str, email: str, password: str) -> User | None:
        # verificar se email existe
        existing_user = self.repo.get_user_by_email(email)
        if existing_user:
            return None
        else:
            hashed_password = hash_password(password)
            user = User(name=name, email=email, password=hashed_password)
            self.repo.create_user(user)
            return user
