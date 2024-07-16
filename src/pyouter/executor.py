import asyncio
from concurrent.futures import Executor
from functools import partial
from typing import Any, Callable, Optional, TypeVar

T = TypeVar("T")

async def run_in_executor(
    executor: Optional[Executor],
    func: Callable[..., T],
    /,
    *args: Any,
    **kwargs: Any,
) -> T:
    """
    Run `func(*args, **kwargs)` asynchronously, using an executor.

    If the executor is None, use the default ThreadPoolExecutor.
    """
    return await asyncio.get_running_loop().run_in_executor(
        executor,
        partial(func, *args, **kwargs),
    )