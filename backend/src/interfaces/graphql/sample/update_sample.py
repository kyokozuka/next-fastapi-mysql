from typing import Any, Dict
from src.shared.exception.function_exception import function_exception
from src.shared.logging.function_logging import function_logging
from src.applications.sample.update_sample_service import UpdateSampleService
from src.applications.sample.sample_dto import UpdateSampleInputDto
from src.interfaces.shared.context import AppContext
from src.interfaces.graphql.sample.graphql_interface import UpdateSampleInput
from src.applications.sample.sample_service import SampleService


@function_exception
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

    context: AppContext = info.context
    mapper = SampleService()

    service = UpdateSampleService(context=context, mapper=mapper)

    sample_input = UpdateSampleInputDto(
        sample_id=sample_input.id,
        name=sample_input.name,
        message=sample_input.message,
    )

    result = service.execute(sample_input)
    return result.to_dict()
