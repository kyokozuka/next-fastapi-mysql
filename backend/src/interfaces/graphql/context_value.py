from fastapi import Request
from src.interfaces.shared.context import AppContext
from src.interfaces.shared.transaction import Transaction
from src.interfaces.shared.repository_factory import RepositoryFactory
from src.infrastructures.db.db import SessionLocal

# from src.domains.auth_user.model.auth_user_model import AuthUserModel
# from src.domains.auth_user.model.auth_user_email import AuthUserEmail


async def context_value(request: Request) -> AppContext:
    session = SessionLocal()
    repository_factory = RepositoryFactory(session)
    transaction = Transaction(session=session, repository_factory=repository_factory)

    return AppContext(
        request=request,
        transaction=transaction,
    )
