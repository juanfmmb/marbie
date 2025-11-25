from pydantic import BaseModel

class devopsRequest(BaseModel):
    message: str
    to: str
    from_: str | None = None
    timeToLifeSec: int

class devopsResponse(BaseModel):
    message: str
