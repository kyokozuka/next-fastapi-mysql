from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from src.infrastructures.db.db import Base
from src.domains.sample.model.sample_model import SampleModel
from src.domains.sample.model.sample_name import SampleName
from src.domains.sample.model.sample_message import SampleMessage
from src.domains.sample.model.sample_id import SampleID
from src.infrastructures.db.model.mixin import TimestampMixin
from src.domains.sample.model.new_sample_model import NewSampleModel
from src.infrastructures.db.model.base_model import BaseDBModel


class SampleDBModel(BaseDBModel[SampleModel, NewSampleModel], TimestampMixin, Base):
    __tablename__ = "samples"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    message = Column(Text)

    deleted_at = Column(Timestamp, nullable=False, server_default="0000-00-00 00:00:00")

    def __init__(
        self,
        name: str,
        message: str,
    ) -> None:
        self.name = name
        self.message = message

    @classmethod
    def create(
        cls, new_model: NewSampleModel
    ) -> "BaseDBModel[SampleModel, NewSampleModel]":
        return cls(
            name=new_model.name.value,  # type: ignore
            message=new_model.message.value,  # type: ignore
        )

    def update(self, model: SampleModel) -> "BaseDBModel[SampleModel, NewSampleModel]":
        self.name = model.name.value  # type: ignore
        self.message = model.message.value  # type: ignore

        return self

    def to_model(self) -> SampleModel:
        return SampleModel(
            id=SampleID(value=self.id),  # type: ignore
            name=SampleName(value=self.name),  # type: ignore
            message=SampleMessage(value=self.message),  # type: ignore
        )
