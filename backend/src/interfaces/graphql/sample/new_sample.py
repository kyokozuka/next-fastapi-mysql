from typing import Any, Dict
from src.shared.exception.function_exception import function_exception
from src.shared.logging.function_logging import function_logging
from src.applications.sample.new_sample_service import NewSampleService
from src.applications.sample.sample_dto import NewSampleInputDto
from src.interfaces.shared.context import AppContext
from src.interfaces.graphql.sample.graphql_interface import NewSampleInput
from src.applications.sample.sample_service import SampleService


@function_exception
@function_logging
def resolve_new_sample(
    _,
    info: Any,
    input: NewSampleInput,
) -> Dict[str, int | str]:
    try:
        sample_input = NewSampleInput(**input)  # type: ignore
    except Exception as e:
        raise Exception(f"Error: {e}")

    context: AppContext = info.context
    mapper = SampleService()

    service = NewSampleService(context, mapper)

    new_sample_input = NewSampleInputDto(
        name=sample_input.name,
        message=sample_input.message,
    )
    print(new_sample_input)

    result = service.execute(new_sample_input)
    return result.to_dict()
