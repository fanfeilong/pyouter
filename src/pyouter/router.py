from .errors import NotFound


class Router(object):
    def __init__(self, **args):
        self.route = {}
        for key in args:
            self.route[key] = args[key]

    def context(self, config, options):
        self.config = config
        self.options = options
        for key in self.route:
            router = self.route[key]
            if type(router) == type(self):
                router.context(config, options)

    def dispatch(self, command: str):
        if "." in command:
            crt, nxt = command.split('.', 1)
            if crt not in self.route:
                raise NotFound(self.route, crt)
            if self.options.view:
                print(f'->router: {crt}')
            return self.route[crt].dispatch(nxt)
        else:
            if self.options.view:
                print(f'->action: {command}')
            if command not in self.route.keys():
                raise NotFound(self.route, command)

            return self.route[command](self.config, self.options)

    def tasks(self, base=None):

        for key in self.route:
            current = f"{base}.{key}" if base else key
            item = self.route[key]
            if type(item) is Router:
                for task in item.tasks(current):
                    yield task
            else:
                yield current
