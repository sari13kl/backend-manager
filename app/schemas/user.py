# schemas
from pydantic import BaseModel, Field
from pydantic.networks import EmailStr

class CreateSchema(BaseModel):
    name: str = Field(min_length=2)
    email: EmailStr
    password: str = Field(min_length=8)
    
        
class LoginSchema(BaseModel):
    email: EmailStr
    password: str
    

class UserSchema(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_active: bool

    model_config = {
        "from_attributes": True
    }