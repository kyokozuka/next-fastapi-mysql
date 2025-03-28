from src.application.shared.transaction_interface import TransactionInterface
from src.domain.sample.model.sample_model import SampleModel
from src.domain.sample.model.sample_id import SampleID
from typing import List


class DeleteSampleService:
    def __init__(self, transaction: TransactionInterface):
        self.transaction = transaction

    def execute(self, sample_id: SampleID) -> List[SampleModel]:
        with self.transaction.begin() as (repo, _):
            sample_repo = repo.create_sample_repository()

            sample_repo.delete(sample_id)

            result = sample_repo.list_sample()

            return result
