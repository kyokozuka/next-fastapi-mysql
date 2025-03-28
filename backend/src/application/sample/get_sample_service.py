from src.application.shared.transaction_interface import TransactionInterface
from src.domain.sample.model.sample_id import SampleID


class GetSampleService:

    def __init__(self, transaction: TransactionInterface):
        self.transaction = transaction

    def execute(self, sample_id: SampleID):
        if sample_id.value <= 0:
            raise ValueError("Invalid sample ID")

        with self.transaction.begin() as (repo, _):
            sample_repo = repo.create_sample_repository()
            result = sample_repo.get_sample(sample_id)

            if not result:
                raise ValueError("Sample not found")

            return result
