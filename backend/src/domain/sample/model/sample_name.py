from dataclasses import dataclass

from pydantic import BaseModel


@dataclass(frozen=True)
class SampleName(BaseModel):
    value: str
