from abc import ABCMeta, abstractmethod
from contextlib import contextmanager
from typing import Generator, Tuple
from src.application.shared.repository_facroty_interface import (
    RepositoryFactoryInterface,
)


class TransactionInterface(metaclass=ABCMeta):

    @abstractmethod
    @contextmanager
    def begin(
        self,
    ) -> Generator[
        Tuple[RepositoryFactoryInterface, "TransactionInterface"],
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
