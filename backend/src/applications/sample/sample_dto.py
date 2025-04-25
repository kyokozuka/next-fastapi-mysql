from pydantic import BaseModel, Field


class NewSampleInputDto(BaseModel):
    name: str = Field(..., min_length=1, description="Sample name")
    message: str = Field(..., min_length=1, description="Sample message")


class UpdateSampleInputDto(BaseModel):
    sample_id: int = Field(..., description="Sample ID")
    name: str = Field(..., min_length=1, description="Sample name")
    message: str = Field(..., min_length=1, description="Sample message")
