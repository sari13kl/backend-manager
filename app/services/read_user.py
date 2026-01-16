from sqlalchemy.orm import Session

from repositories.user_repository import UserRepository
from database.models.user import User

class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)
        
    def get_user_id(self, user_id: int) -> User | None:
        return self.repo.get_user_by_id(user_id)