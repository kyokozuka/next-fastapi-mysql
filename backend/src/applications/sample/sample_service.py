from src.domains.sample.model.sample_model import SampleModel
from src.domains.sample.model.new_sample_model import NewSampleModel
from src.domains.sample.model.sample_id import SampleID
from src.domains.sample.model.sample_name import SampleName
from src.domains.sample.model.sample_message import SampleMessage
from src.applications.sample.sample_dto import NewSampleInputDto, UpdateSampleInputDto


class SampleService:
    def new(self, dto: NewSampleInputDto) -> NewSampleModel:
        return NewSampleModel(
            name=SampleName(dto.name), message=SampleMessage(dto.message)
        )

    def update(self, dto: UpdateSampleInputDto) -> SampleModel:
        return SampleModel(
            id=SampleID(dto.sample_id),
            name=SampleName(dto.name),
            message=SampleMessage(dto.message),
        )
