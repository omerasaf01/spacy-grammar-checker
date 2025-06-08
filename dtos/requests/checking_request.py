from pydantic import BaseModel

class CheckingRequestDto(BaseModel):
    text: str
