from src.applications.shared.repository_facroty_interface import (
    RepositoryFactoryInterface,
)
from src.infrastructures.repository.sample_repository import SampleRepositpry
from src.domains.sample.interface.sample_repository_interface import (
    SampleRepositpryInterface,
)
from sqlalchemy.orm import Session
from typing import Final


class RepositoryFactory(RepositoryFactoryInterface):

    _session: Final[Session]

    def __init__(self, session: Session):
        self._session = session

    def sample_repository(self) -> SampleRepositpryInterface:
        return SampleRepositpry(session=self._session)
