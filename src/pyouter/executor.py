import asyncio
import inspect

from concurrent.futures import Executor
from functools import partial


class LeafExecutor:
    def __init__(self, config, options, executor, leaf):
        self.config = config
        self.options = options
        self.executor = executor
        self.leaf = leaf
        
    async def run(self):
        
        async def runner(leaf, config, options):
            if inspect.isfunction(leaf):
                if inspect.iscoroutinefunction(leaf):
                    return await leaf(config, options)
                else:
                    return leaf(config, options)
            else:
                if inspect.iscoroutinefunction(leaf.run):
                    return await leaf.run(config, options)
                else:
                    return leaf.run(config, options)
        
        def run_sync(leaf, config, options):
            asyncio.run(runner(leaf, config, options))
        
        loop = asyncio.get_running_loop()
        loop.run_until_complete(
            loop.run_in_executor(
                self.executor,
                partial(run_sync, self.leaf, self.config, self.options),
            )
        )
    