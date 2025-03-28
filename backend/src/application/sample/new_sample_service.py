from src.application.sample.sample_dto import NewSampleInputDto
from src.domain.sample.model.new_sample_model import NewSampleModel
from src.application.shared.transaction_interface import TransactionInterface
from src.domain.sample.model.sample_model import SampleModel


class NewSampleService:
    def __init__(self, transaction: TransactionInterface):
        self.transaction = transaction

    def execute(self, input: NewSampleInputDto) -> SampleModel:
        with self.transaction.begin() as (repo, _):
            sample_repo = repo.create_sample_repository()

            new_sample = NewSampleModel(name=input.name, message=input.message)

            result = sample_repo.new_sample(new_sample)

            return result
