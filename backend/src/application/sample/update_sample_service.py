from src.application.sample.sample_dto import UpdateSampleInputDto
from src.application.shared.transaction_interface import TransactionInterface
from src.domain.sample.model.sample_model import SampleModel


class UpdateSampleService:
    def __init__(self, transaction: TransactionInterface):
        self.transaction = transaction

    def execute(self, input: UpdateSampleInputDto) -> SampleModel:
        with self.transaction.begin() as (repo, _):
            sample_repo = repo.create_sample_repository()

            update_sample = SampleModel(
                id=input.sample_id, name=input.name, message=input.message
            )

            result = sample_repo.update(update_sample)

            return result
