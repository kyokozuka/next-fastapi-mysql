from src.application.shared.repository_facroty_interface import (
    RepositoryFactoryInterface,
)
from src.infrastructure.repository.sample_repository import SampleRepositpry
from src.domain.sample.interface.sample_repository_interface import (
    SampleRepositpryInterface,
)
from sqlalchemy.orm import Session
from typing import Final


class RepositoryFactory(RepositoryFactoryInterface):

    _session: Final[Session]

    def __init__(self, session: Session):
        self._session = session

    def create_sample_repository(self) -> SampleRepositpryInterface:
        return SampleRepositpry(session=self._session)
