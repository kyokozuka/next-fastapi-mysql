from dataclasses import dataclass
from pydantic import BaseModel

from src.domain.sample.model.sample_name import SampleName
from src.domain.sample.model.sample_message import SampleMessage


@dataclass(frozen=True)
class NewSampleModel(BaseModel):
    name: SampleName
    message: SampleMessage
