import jwt
from fastapi import HTTPException, Header
from config import JWT_SECRET, JWT_ALGORITHM

def create_jwt(username: str) -> str:
    payload = {
        "sub": username
    }

    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

def validation_jwt(X_JWT_KWY: str = Header(alias="X-JWT-KWY")) -> str:
    if X_JWT_KWY is None or not X_JWT_KWY.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="JWT invalida, intente nuevamente")
    
    jwt_token = X_JWT_KWY.split(" ")[1]

    try:
        payload = jwt.decode(jwt_token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token vencido")
    except Exception:
        raise HTTPException(status_code=401, detail="Token invalido")