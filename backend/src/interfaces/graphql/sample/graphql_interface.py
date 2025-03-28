from pydantic import BaseModel


class NewSampleInput(BaseModel):
    name: str
    message: str


class UpdateSampleInput(BaseModel):
    id: int
    name: str
    message: str
