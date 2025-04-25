from typing import Any, Dict, List
from src.shared.exception.function_exception import function_exception
from src.shared.logging.function_logging import function_logging
from src.domains.sample.model.sample_id import SampleID
from src.applications.sample.delete_sample_service import DeleteSampleService
from src.interfaces.shared.context import AppContext
from src.domains.sample.model.sample_id import SampleID


@function_exception
@function_logging
def resolve_delete_sample(
    _,
    info: Any,
    id: int,
) -> List[Dict[str, int | str]]:
    context: AppContext = info.context

    service = DeleteSampleService(context=context)

    results = service.execute(sample_id=SampleID(value=id))
    return [result.to_dict() for result in results]
