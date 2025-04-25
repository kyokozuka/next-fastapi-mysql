from typing import Any, Dict, List

from src.applications.sample.list_sample_service import ListSampleService
from src.shared.logging.function_logging import function_logging
from src.shared.exception.function_exception import function_exception
from src.interfaces.shared.context import AppContext


@function_exception
@function_logging
def resolve_list_sample(_, info: Any) -> List[Dict[str, int | str]] | None:
    context: AppContext = info.context

    service = ListSampleService(context)
    results = service.execute()
    return [result.to_dict() for result in results]
