from fastapi import HTTPException, Header
from config import API_KEY

def validationApiKey(X_Parse_REST_API_Key: str = Header(None)):
    if X_Parse_REST_API_Key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="API KEY invalida, intente nuevamente"
        )
    return True