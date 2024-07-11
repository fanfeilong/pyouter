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
    

def runner():
    '''
    示例:
        App.use 方法必须传入一个router，router内部可以嵌套子router，配置了后，路由从一级节点开始层层路由
    
    用例: 
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
    
if __name__=="__main__":
    runner()