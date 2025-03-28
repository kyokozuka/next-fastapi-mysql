from typing import Any, Dict
from src.shared.exception.function_exeption import function_exeption
from src.shared.logging.function_logging import function_logging
from src.domain.sample.model.sample_name import SampleName
from src.domain.sample.model.sample_id import SampleID
from src.domain.sample.model.sample_message import SampleMessage
from src.application.sample.update_sample_service import UpdateSampleService
from src.application.sample.sample_dto import UpdateSampleInputDto
from src.infrastructure.db.base import SessionLocal
from src.interfaces.shared.repository_factory import RepositoryFactory
from src.interfaces.shared.transaction import Transaction
from src.interfaces.graphql.sample.graphql_interface import UpdateSampleInput


@function_exeption
@function_logging
def resolve_update_sample(
    _,
    info: Any,
    input: UpdateSampleInput,
) -> Dict[str, int | str]:
    try:
        sample_input = UpdateSampleInput(**input)  # type: ignore
    except Exception as e:
        raise Exception(f"Error: {e}")

    session = SessionLocal()
    factory = RepositoryFactory(session)
    transaction = Transaction(session=session, repository_factory=factory)

    service = UpdateSampleService(transaction)

    sample_input = UpdateSampleInputDto(
        sample_id=SampleID(value=sample_input.id),
        name=SampleName(value=sample_input.name),
        message=SampleMessage(value=sample_input.message),
    )

    result = service.execute(sample_input)
    return result.to_dict()
