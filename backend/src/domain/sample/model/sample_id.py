from dataclasses import dataclass

from pydantic import BaseModel


@dataclass(frozen=True)
class SampleID(BaseModel):
    value: int
