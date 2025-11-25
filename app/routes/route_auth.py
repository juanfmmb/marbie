from fastapi import APIRouter, HTTPException
from schemas.schema_auth import authRequest, authResponse
from validations.validation_jwt import create_jwt

router = APIRouter()

@router.post("/login", response_model=authResponse)
def login(playload: authRequest):
    if playload.username != "admin" or playload.password != "devopsapitest":
        raise HTTPException(status_code=401, detail="Claves de acceso incorrectas")
    
    token = create_jwt(playload.username)
    return authResponse(access_token=token)