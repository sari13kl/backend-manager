# logica de autenticacao
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from core.config import settings
from core.security import verify_password
from core.jwt_model import TokenData
from database.session import get_db
from database.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def autenticar_usuario(email: str, password: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user

def criar_token(id_usuario: int, duration: timedelta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)):
    data_expiracao = datetime.utcnow() + duration
    to_encode = {"sub": str(id_usuario), "exp": data_expiracao}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        id_usuario: str = payload.get("sub")
        if id_usuario is None:
            raise credentials_exception
        token_data = TokenData(id=id_usuario)
    except JWTError:
        raise credentials_exception
    user = db.query(User).filter(User.id == token_data.id).first()
    if user is None:
        raise credentials_exception
    return user