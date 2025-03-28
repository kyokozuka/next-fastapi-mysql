import functools
from typing import Any, Callable, TypeVar, cast

from src.shared.logging.custom_logging import custom_logging


F = TypeVar("F", bound=Callable[..., Any])

logger = custom_logging()


def function_logging(func: F) -> F:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        logger.info(f"Function {func.__name__} called.")
        result = func(*args, **kwargs)
        logger.info(f"Function {func.__name__} returned.")
        return result

    return cast(F, wrapper)
