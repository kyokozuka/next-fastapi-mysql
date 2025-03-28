from dataclasses import dataclass

from src.domain.sample.model.sample_id import SampleID
from src.domain.sample.model.sample_name import SampleName
from src.domain.sample.model.sample_message import SampleMessage


@dataclass(frozen=True)
class NewSampleInputDto:
    name: SampleName
    message: SampleMessage


@dataclass(frozen=True)
class UpdateSampleInputDto:
    sample_id: SampleID
    name: SampleName
    message: SampleMessage
