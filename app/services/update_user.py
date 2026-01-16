# atualizar somente nome e senha do usuario
from sqlalchemy.orm import Session
from repositories.user_repository import UserRepository
from database.models.user import User
from core.security import get_password_hash

class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)
        
    def update_user(self, user_id: int, name: str | None = None, password: str | None = None) -> User | None:
        user = self.repo.get_user_by_id(user_id)
        if not user:
            return None
        
        if name is not None:
            user.name = name
        if password is not None:
            user.password = password_hash(password)
        
        self.repo.db.commit()
        self.repo.db.refresh(user)
        return user