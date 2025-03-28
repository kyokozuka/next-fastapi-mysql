from typing import Any, Dict

from src.application.sample.get_sample_service import GetSampleService
from src.domain.sample.model.sample_id import SampleID
from src.shared.logging.function_logging import function_logging
from src.shared.exception.function_exeption import function_exeption
from src.infrastructure.db.base import SessionLocal
from src.interfaces.shared.repository_factory import RepositoryFactory
from src.interfaces.shared.transaction import Transaction


@function_exeption
@function_logging
def resolve_get_sample(_, info: Any, id: int) -> Dict[str, int | str] | None:
    session = SessionLocal()
    factory = RepositoryFactory(session)
    transaction = Transaction(session=session, repository_factory=factory)

    service = GetSampleService(transaction)
    result = service.execute(SampleID(value=id))
    return result.to_dict()
