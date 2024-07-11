from typing import Any
from pyouter.app import App
from pyouter.router import Router


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
        print("hello class object")
    

def runner():
    '''
    示例:
        App.use 方法必须传入一个router，router内部可以嵌套子router，配置了后，路由从一级节点开始层层路由
    
    用例: 
        * python test.py test.hello.func
        * python test.py test.hello.obj
    '''
    app = App()
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
    app.run()
    
if __name__=="__main__":
    runner()