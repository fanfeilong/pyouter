

from default import create_parser
from errors import NotInit
from router import Router


class App(object):
    def __init__(self, **args):
        opt_parser = create_parser("tasks router runner")
        self.options = opt_parser.parse_args()
        self.config = {}
        self.router: Router = None

    def use(self, router: Router):
        self.router = router
        self.router.context(self.config, self.options)
        return self

    def run(self):
        if self.router is None:
            raise NotInit("self.router in App")

        if self.options.tasks:
            for task in self.router.tasks():
                print(task)
        else:
            self.router.dispatch(self.options.action)
        return self
