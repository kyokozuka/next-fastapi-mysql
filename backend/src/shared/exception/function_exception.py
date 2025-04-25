import functools
from typing import Any, Callable, TypeVar, cast

from src.shared.logging.function_logging import function_logging
from src.shared.logging.custom_logging import custom_logging

F = TypeVar("F", bound=Callable[..., Any])
logger = custom_logging()


def function_exception(func: F) -> F:
    @function_logging
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            logger.error(f"Function {func.__name__} raised an exception: {e}")
            raise e

    return cast(F, wrapper)
