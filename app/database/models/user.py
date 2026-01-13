from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.database.base import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name= Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    active = Column(Boolean, default=True)
# relacionamento com tarefas
    tasks = relationship("Task", back_populates="user", cascade="all, delete-orphan")
    
    def __init__(self, name: str, email: str, password: str, active: bool = True):
        self.name = name
        self.email = email
        self.password = password
        self.active = active