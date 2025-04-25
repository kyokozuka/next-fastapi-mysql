from src.applications.shared.context_interface import ContextInterface
from src.domains.sample.model.sample_model import SampleModel
from src.domains.sample.model.sample_id import SampleID
from typing import List


class DeleteSampleService:
    def __init__(self, context: ContextInterface):
        self._context = context

    def execute(self, sample_id: SampleID) -> List[SampleModel]:
        with self._context.transaction.begin() as tx:
            sample_repo = tx.repository_factory.sample_repository()

            sample_repo.delete(sample_id)

            result = sample_repo.list_sample()

            return result
