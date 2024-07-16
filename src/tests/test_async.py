import asyncio
import inspect

async def b():
    print("b")

def a():
    print("a")
    
async def c():
    await a()
    
async def d():
    await b()
    
class A:
    def test():
        print("A")

class B:
    async def test():
        print("B")

async def g(f):
    if inspect.iscoroutinefunction(f):
        print("await..")
        await f()
    else:
        f()

asyncio.get_event_loop().run_until_complete(g(a))
asyncio.get_event_loop().run_until_complete(g(b))

asyncio.get_event_loop().run_until_complete(g(A.test))
asyncio.get_event_loop().run_until_complete(g(B.test))