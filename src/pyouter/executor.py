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
        
        def is_continufunction(leaf):
            if inspect.isfunction(leaf):
                return inspect.iscoroutinefunction(leaf)
            else:
                return inspect.iscoroutinefunction(leaf.run)
            
        async def run_async(leaf, config, options):
            if inspect.isfunction(leaf):
                return await leaf(config, options)
            else:
                return await leaf.run(config, options)
            
        def run_sync(leaf, config, options):
            if inspect.isfunction(leaf):
                return leaf(config, options)
            else:
                return leaf.run(config, options)
        
        if is_continufunction(self.leaf):
            await run_async(self.leaf, self.config, self.options)
        else:
            loop = asyncio.get_running_loop()
            await loop.run_in_executor(
                self.executor,
                partial(run_sync, self.leaf, self.config, self.options),
            )