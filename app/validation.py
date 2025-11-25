from fastapi import HTTPException, Header

api_key = "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c"

def validationApiKey(X_Parse_REST_API_Key: str = Header(None)):
    if X_Parse_REST_API_Key != api_key:
        raise HTTPException(
            status_code=401,
            detail="API KEY invalida, intente nuevamente"
        )
    return True