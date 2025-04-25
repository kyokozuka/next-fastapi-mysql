from typing import TypeVar, Generic
from pydantic import BaseModel


Model = TypeVar("Model", bound=BaseModel)
NewModel = TypeVar("NewModel", bound=BaseModel)


class BaseDBModel(Generic[Model, NewModel]):
    @classmethod
    def create(cls, new_model: NewModel) -> "BaseDBModel[Model, NewModel]":
        raise NotImplementedError("Must implement create method")

    def update(self, model: Model) -> "BaseDBModel[Model, NewModel]":
        raise NotImplementedError("Must implement update method")

    def to_model(self) -> Model:
        raise NotImplementedError("Must implement to_model method")
