from abc import ABC, abstractmethod

from src.applications.shared.repository_facroty_interface import (
    RepositoryFactoryInterface,
)
from src.applications.shared.transaction_interface import TransactionInterface

# from src.domains.auth_user.model.auth_user_model import AuthUserModel


class ContextInterface(ABC):

    # @property
    # @abstractmethod
    # def user(self) -> AuthUserModel:
    #     """
    #     Get the user associated with the context.
    #     """
    #     raise NotImplementedError("User property not implemented")

    @property
    @abstractmethod
    def repository_factory(self) -> RepositoryFactoryInterface:
        raise NotImplementedError("Repository factory property not implemented")

    @property
    @abstractmethod
    def transaction(self) -> TransactionInterface:
        """
        Get the transaction status of the context.
        """
        raise NotImplementedError("Transaction property not implemented")
