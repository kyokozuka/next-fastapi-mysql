from src.application.shared.transaction_interface import TransactionInterface
from typing import Final, Generator, Tuple
from sqlalchemy.orm import Session
from src.application.shared.repository_facroty_interface import (
    RepositoryFactoryInterface,
)
from contextlib import contextmanager


class Transaction(TransactionInterface):

    _session: Final[Session]
    __repository_factory: Final[RepositoryFactoryInterface]

    def __init__(
        self, session: Session, repository_factory: RepositoryFactoryInterface
    ):
        self._session = session
        self.__repository_factory = repository_factory

    @contextmanager
    def begin(
        self,
    ) -> Generator[
        Tuple[RepositoryFactoryInterface, TransactionInterface],
        None,
        None,
    ]:
        try:
            yield self.__repository_factory, self
            self._session.commit()
        except Exception as e:
            self._session.rollback()
            raise e

    def commit(self) -> None:
        self._session.commit()

    def rollback(self) -> None:
        self._session.rollback()
