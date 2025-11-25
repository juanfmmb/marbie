from fastapi import APIRouter, Depends
from schemas import devopsRequest, devopsResponse
from validation import validationApiKey

router = APIRouter()

@router.post("/DevOps", response_model=devopsResponse, dependencies=[Depends(validationApiKey)])
def devops(playload: devopsRequest):
    responseMessage = f"Hello {playload.to}, your message will be send"
    return devopsResponse(message=responseMessage)