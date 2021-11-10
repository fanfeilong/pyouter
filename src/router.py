
class Router:
    def __init__(self, config, options, **args):
        self.route = {}
        for key in args:
            self.route[key] = args[key]
        self.config = config
        self.options = options

    def dispatch(self, command: str):
        if "." in command:
            crt, nxt = command.split('.', 1)
            if crt not in self.route:
                raise NotFound(self.route, crt)
            return self.route[crt].dispatch(nxt)
        else:
            if command not in self.route:
                raise NotFound(self.route, command)
            return self.route[command]()

    def tasks(self, base=None):

        for key in self.route:
            current = f"{base}.{key}" if base else key
            item = self.route[key]
            if type(item) is Router:
                for task in item.tasks(current):
                    yield task
            else:
                yield current



