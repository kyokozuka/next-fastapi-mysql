from dataclasses import dataclass
from pydantic import BaseModel


@dataclass(frozen=True)
class SampleMessage(BaseModel):
    value: str
