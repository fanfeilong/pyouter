from typing import Any
from pyouter.app import App
from pyouter.router import Router

import json

def hello(config, options):
    print("hello function")

class Hello:
    def __init__(self) -> None:
        pass 
        
    def __call__(self, config, options) -> Any:
        self.config = config
        self.options = options
        self.inner()
    
    def inner(self):
        print(f"hello class object, self.options.debug:{self.options.debug}")
        if self.options.debug:
            print('debug')

if __name__=="__main__":
    '''
    Usage:
        * python test.py test.hello.func
        * python test.py test.hello.obj
    '''
    
    app = App(config='config.json')
    
    app.option(
        '-d', '--debug',
        dest='debug',
        action="store_true",
        help='debug'
    )
    
    app.use(
        router=Router(
            test=Router(
                hello=Router(
                    func=hello,
                    obj=Hello()
                )
            )
        )
    )
    
    print("run")
    app.run()