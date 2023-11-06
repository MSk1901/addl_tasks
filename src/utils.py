from functools import wraps
from typing import Callable


def memoized(func: Callable) -> Callable:
    """Добавляет функции мемоизацию"""
    @wraps(func)
    def wrapper(arg: int) -> int:
        if arg in args_used:
            result = args_used[arg]
        else:
            result = func(arg)
            args_used[arg] = result
        return result

    args_used = {}
    return wrapper
