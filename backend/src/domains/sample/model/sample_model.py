from dataclasses import dataclass

from src.domains.sample.model.sample_id import SampleID
from src.domains.sample.model.sample_name import SampleName
from src.domains.sample.model.sample_message import SampleMessage


@dataclass(frozen=True)
class SampleModel:
    id: SampleID
    name: SampleName
    message: SampleMessage

    def to_dict(self) -> dict[str, int | str]:
        return {
            "id": self.id.value,
            "name": self.name.value,
            "message": self.message.value,
        }
