from pydantic import BaseModel
# TpkenData(sub, email)
class JWTData(BaseModel):
    sub: int # user id
    email: str