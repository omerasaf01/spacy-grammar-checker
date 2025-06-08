from pydantic import BaseModel

class CheckingResponseDto(BaseModel):
    suggestions: list
