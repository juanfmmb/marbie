from fastapi import APIRouter, Depends
from schemas.schema_devops import devopsRequest, devopsResponse
from validations.validation_api_key import validationApiKey
from validations.validation_jwt import validation_jwt

router = APIRouter()

@router.post("/DevOps", response_model=devopsResponse)
def devops(playload: devopsRequest, _: None = Depends(validationApiKey), username: str = Depends(validation_jwt)):
    responseMessage = f"Hello {playload.to}, your message will be send"
    return devopsResponse(message=responseMessage)