from typing import List
from datetime import datetime
from src.domain.sample.interface.sample_repository_interface import (
    SampleRepositpryInterface,
)
from src.shared.exception.function_exeption import function_exeption
from src.domain.sample.model.sample_model import SampleModel
from src.domain.sample.model.new_sample_model import NewSampleModel
from src.infrastructure.db.model.sample import SampleDBModel
from src.domain.sample.model.sample_id import SampleID
from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.shared.logging.custom_logging import custom_logging

logger = custom_logging()


class SampleRepositpry(SampleRepositpryInterface):

    def __init__(self, session: Session):
        self.session = session

    @function_exeption
    def new_sample(self, sample: NewSampleModel) -> SampleModel:
        db_sample = SampleDBModel.create(sample)
        self.session.add(db_sample)
        self.session.flush()

        return db_sample.to_model()

    @function_exeption
    def list_sample(self) -> List[SampleModel]:
        query = self.session.query(SampleDBModel).filter(
            SampleDBModel.deleted_at == None
        )

        if not query:
            raise HTTPException(status_code=404, detail="Sample not found")

        return [data.to_model() for data in query.all()]

    @function_exeption
    def get_sample(self, sample_id: SampleID) -> SampleModel:
        query = self.session.query(SampleDBModel).filter(
            SampleDBModel.id == sample_id.value and SampleDBModel.deleted_at == None
        )

        if not query:
            raise HTTPException(status_code=404, detail="Sample not found")

        result = query.first()
        if result is None:
            raise HTTPException(status_code=404, detail="Sample not found")

        return result.to_model()

    @function_exeption
    def update(self, sample: SampleModel) -> SampleModel:
        db_sample = (
            self.session.query(SampleDBModel)
            .filter(
                SampleDBModel.id == sample.id.value and SampleDBModel.deleted_at == None
            )
            .first()
        )

        if not db_sample:
            raise HTTPException(status_code=404, detail="Sample not found")

        db_sample.update(sample)
        self.session.flush()

        return db_sample.to_model()

    @function_exeption
    def delete(self, sample_id: SampleID) -> None:
        db_sample = (
            self.session.query(SampleDBModel)
            .filter(
                SampleDBModel.id == sample_id.value and SampleDBModel.deleted_at == None
            )
            .first()
        )

        if not db_sample:
            raise HTTPException(status_code=404, detail="Sample not found")

        db_sample.deleted_at = datetime.now()  # type: ignore
        self.session.flush()
