from src.applications.sample.sample_dto import NewSampleInputDto
from src.applications.shared.context_interface import ContextInterface
from src.domains.sample.model.sample_model import SampleModel
from src.applications.sample.sample_service import SampleService


class NewSampleService:
    def __init__(self, context: ContextInterface, mapper: SampleService):
        self._context = context
        self._mapper = mapper

    def execute(self, input: NewSampleInputDto) -> SampleModel:
        new_sample = self._mapper.new(input)

        with self._context.transaction.begin() as tx:
            sample_repo = tx.repository_factory.sample_repository()
            return sample_repo.new_sample(new_sample)
