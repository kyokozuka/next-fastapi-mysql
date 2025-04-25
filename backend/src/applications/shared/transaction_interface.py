from abc import ABCMeta, abstractmethod
from contextlib import contextmanager
from typing import Generator
from src.applications.shared.repository_facroty_interface import (
    RepositoryFactoryInterface,
)


class TransactionInterface(metaclass=ABCMeta):

    @property
    def repository_factory(self) -> RepositoryFactoryInterface:
        raise NotImplementedError("Repository factory property not implemented")

    @abstractmethod
    @contextmanager
    def begin(
        self,
    ) -> Generator[
        "TransactionInterface",
        None,
        None,
    ]:
        raise NotImplementedError

    @abstractmethod
    def commit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def rollback(self) -> None:
        raise NotImplementedError
