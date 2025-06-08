import asyncio

from src.scripts import Chrome

class Google(Chrome):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        super().__init__()

    def __getattr__(self, attr):
        return getattr(self.parent, attr)

    async def start(self):
        self.process.emit('goto google')
        await self.page.goto('https://google.com/ncr')
        await asyncio.sleep(3)