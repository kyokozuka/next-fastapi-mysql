from abc import ABC, abstractmethod
from typing import List

from src.domain.sample.model.sample_model import SampleModel
from src.domain.sample.model.new_sample_model import NewSampleModel
from src.domain.sample.model.sample_id import SampleID


class SampleRepositpryInterface(ABC):

    @abstractmethod
    def new_sample(self, sample: NewSampleModel) -> SampleModel:
        raise NotImplementedError

    @abstractmethod
    def list_sample(self) -> List[SampleModel]:
        raise NotImplementedError

    @abstractmethod
    def get_sample(self, sample_id: SampleID) -> SampleModel:
        raise NotImplementedError

    @abstractmethod
    def update(self, sample: SampleModel) -> SampleModel:
        raise NotImplementedError

    @abstractmethod
    def delete(self, sample_id: SampleID) -> None:
        raise NotImplementedError
