from .errors import NotFound
import asyncio
import inspect
import multiprocessing
from .executor import run_in_executor
from functools import partial

class Router(object):
    def __init__(self, **args):
        self.route = {}
        for key in args:
            self.route[key] = args[key]

    def context(self, config, options, executor):
        self.config = config
        self.options = options
        self.executor = executor
        for key in self.route:
            router = self.route[key]
            if type(router) == type(self):
                router.context(config, options, executor)

    async def dispatch(self, command: str):
        if "." in command:
            crt, nxt = command.split('.', 1)
            if crt not in self.route:
                raise NotFound(self.route, crt)
            if self.options.view:
                print(f'->router: {crt}')
            return await self.route[crt].dispatch(nxt)
        else:
            if self.options.view:
                print(f'->action: {command}')
            if command not in self.route.keys():
                raise NotFound(self.route, command)

            leaf = self.route[command]
            
            if isinstance(leaf, Router):
                print("router ...")
                tasks = []
                for key in leaf.route:
                    task = asyncio.create_task(leaf.dispatch(key))
                    tasks.append(task)
                await asyncio.gather(*tasks, return_exceptions=True)
            else:
                async def runner(config, options):
                    if inspect.isfunction(leaf):
                        return await leaf(config, options)
                    else:
                        return await leaf.run(config, options)
                
                def run(config, options):
                    asyncio.run(runner(config, options))
                
                loop = asyncio.get_running_loop()
                loop.run_until_complete(
                    loop.run_in_executor(
                        self.executor,
                        partial(run, self.config, self.options),
                    )
                )

    def tasks(self, base=None):

        for key in self.route:
            current = f"{base}.{key}" if base else key
            item = self.route[key]
            if type(item) is Router:
                for task in item.tasks(current):
                    yield task
            else:
                yield current
