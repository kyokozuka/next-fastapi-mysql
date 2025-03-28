from abc import ABCMeta, abstractmethod
from src.domain.sample.interface.sample_repository_interface import (
    SampleRepositpryInterface,
)


class RepositoryFactoryInterface(metaclass=ABCMeta):

    @abstractmethod
    def create_sample_repository(self) -> SampleRepositpryInterface:
        raise NotImplementedError("create_sample_repository method not implemented")
