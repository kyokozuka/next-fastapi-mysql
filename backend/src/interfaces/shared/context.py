from fastapi import Request
from src.applications.shared.context_interface import ContextInterface
from src.applications.shared.repository_facroty_interface import (
    RepositoryFactoryInterface,
)
from src.applications.shared.transaction_interface import TransactionInterface

# from src.domains.auth_user.model.auth_user_model import AuthUserModel


class AppContext(ContextInterface):
    def __init__(
        self,
        # user: AuthUserModel,
        request: Request,
        transaction: TransactionInterface,
    ):
        # self._user = user
        self._request = request
        self._transaction = transaction

    # @property
    # def user(self) -> AuthUserModel:
    #     return self._user

    @property
    def repository_factory(self) -> RepositoryFactoryInterface:
        return self._transaction.repository_factory

    @property
    def transaction(self) -> TransactionInterface:
        return self._transaction
