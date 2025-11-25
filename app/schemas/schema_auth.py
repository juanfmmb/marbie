from pydantic import BaseModel

class authRequest(BaseModel):
    username: str
    password: str

class authResponse(BaseModel):
    access_token: str
    token_type: str = "Bearer"