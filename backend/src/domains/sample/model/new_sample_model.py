from dataclasses import dataclass

from src.domains.sample.model.sample_name import SampleName
from src.domains.sample.model.sample_message import SampleMessage


@dataclass(frozen=True)
class NewSampleModel:
    name: SampleName
    message: SampleMessage
