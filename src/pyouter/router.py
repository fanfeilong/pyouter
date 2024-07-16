import asyncio

from .errors import NotFound
from .executor import LeafExecutor

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

    async def dispatch(self, pre:str|None, command: str, depth: int):
        show_path = self.options.inspect or self.options.view
        path_prefix = '  '*depth if self.options.inspect else ''
        run_action = not self.options.inspect
        
        def full_path(pre, command):
            if pre is not None and pre!='':
                return f'{pre}.{command}'
            else:
                return command
        
        if "." in command:
            crt, nxt = command.split('.', 1)
            if crt not in self.route:
                raise NotFound(self.route, crt)
            
            router_path = full_path(pre, crt)
            if show_path:
                print(f'[pyouter] {path_prefix}->router: {router_path}')
            
            return await self.route[crt].dispatch(router_path, nxt, depth+1)
        else:
            if command not in self.route.keys():
                raise NotFound(self.route, command)

            leaf = self.route[command]
            if isinstance(leaf, Router):
                tasks = []
                for crt in leaf.route:
                    router_path = full_path(pre, crt)
                    if show_path:
                        print(f'[pyouter] {path_prefix}->router: {router_path}')
                        
                    task = asyncio.create_task(leaf.dispatch(router_path, crt, depth+1))
                    tasks.append(task)
                
                await asyncio.gather(*tasks, return_exceptions=True)
            else:
                action_path = full_path(pre, command)
                if show_path:
                    print(f'[pyouter] {path_prefix}->action: {action_path}')
                
                if run_action:
                    executor = LeafExecutor(self.config, self.options, self.executor, leaf)
                    await executor.run()

    def tasks(self, base=None):

        for key in self.route:
            current = f"{base}.{key}" if base else key
            item = self.route[key]
            if type(item) is Router:
                for task in item.tasks(current):
                    yield task
            else:
                yield current
