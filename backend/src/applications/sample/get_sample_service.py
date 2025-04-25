from src.domains.sample.model.sample_id import SampleID
from src.applications.shared.context_interface import ContextInterface


class GetSampleService:

    def __init__(self, context: ContextInterface):
        self._context = context

    def execute(self, sample_id: SampleID):
        if sample_id.value <= 0:
            raise ValueError("Invalid sample ID")

        with self._context.transaction.begin() as tx:
            sample_repo = tx.repository_factory.sample_repository()
            result = sample_repo.get_sample(sample_id)

            if not result:
                raise ValueError("Sample not found")

            return result
