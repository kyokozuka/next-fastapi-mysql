from typing import Any, Dict

from src.applications.sample.get_sample_service import GetSampleService
from src.domains.sample.model.sample_id import SampleID
from src.shared.logging.function_logging import function_logging
from src.shared.exception.function_exception import function_exception
from src.interfaces.shared.context import AppContext


@function_exception
@function_logging
def resolve_get_sample(_, info: Any, id: int) -> Dict[str, int | str] | None:
    context: AppContext = info.context

    service = GetSampleService(context=context)
    result = service.execute(SampleID(value=id))
    return result.to_dict()
