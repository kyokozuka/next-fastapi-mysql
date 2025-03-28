from typing import Any, Dict, List
from src.shared.exception.function_exeption import function_exeption
from src.shared.logging.function_logging import function_logging
from src.domain.sample.model.sample_id import SampleID
from src.application.sample.delete_sample_service import DeleteSampleService
from src.infrastructure.db.base import SessionLocal
from src.interfaces.shared.repository_factory import RepositoryFactory
from src.interfaces.shared.transaction import Transaction
from src.domain.sample.model.sample_id import SampleID


@function_exeption
@function_logging
def resolve_delete_sample(
    _,
    info: Any,
    id: int,
) -> List[Dict[str, int | str]]:

    session = SessionLocal()
    factory = RepositoryFactory(session)
    transaction = Transaction(session=session, repository_factory=factory)

    service = DeleteSampleService(transaction)

    results = service.execute(sample_id=SampleID(value=id))
    return [result.to_dict() for result in results]
