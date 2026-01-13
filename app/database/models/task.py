from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    status = Column(String, default="pendente")
    priority = Column(String, default="baixa")
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="tasks")
    
    def __init__(self, title: str, description: str, user_id: int, status: str = "pendente", priority: str = "baixa"):
        self.title = title
        self.description = description
        self.user_id = user_id
        self.status = status
        self.priority = priority