from typing import List
from src.domains.sample.model.sample_model import SampleModel
from src.applications.shared.context_interface import ContextInterface


class ListSampleService:

    def __init__(self, context: ContextInterface):
        self._context = context

    def execute(self) -> List[SampleModel]:
        with self._context.transaction.begin() as tx:
            sample_repo = tx.repository_factory.sample_repository()
            return sample_repo.list_sample()
