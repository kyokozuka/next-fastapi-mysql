from typing import List
from src.domain.sample.model.sample_model import SampleModel
from src.application.shared.transaction_interface import TransactionInterface


class ListSmapleService:

    def __init__(self, transaction: TransactionInterface):
        self.transaction = transaction

    def execute(self) -> List[SampleModel]:
        with self.transaction.begin() as (repo, _):
            sample_repo = repo.create_sample_repository()
            return sample_repo.list_sample()
