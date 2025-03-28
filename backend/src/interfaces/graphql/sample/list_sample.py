from typing import Any, Dict, List

from src.application.sample.list_sample_service import ListSmapleService
from src.shared.logging.function_logging import function_logging
from src.shared.exception.function_exeption import function_exeption
from src.infrastructure.db.base import SessionLocal
from src.interfaces.shared.repository_factory import RepositoryFactory
from src.interfaces.shared.transaction import Transaction


@function_exeption
@function_logging
def resolve_list_sample(_, info: Any) -> List[Dict[str, int | str]] | None:
    session = SessionLocal()
    factory = RepositoryFactory(session)
    transaction = Transaction(session=session, repository_factory=factory)

    service = ListSmapleService(transaction)
    results = service.execute()
    return [result.to_dict() for result in results]
