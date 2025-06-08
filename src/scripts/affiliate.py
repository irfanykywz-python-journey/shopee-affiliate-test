import asyncio

from src.scripts import Chrome

class Affiliate(Chrome):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        super().__init__()

    def __getattr__(self, attr):
        return getattr(self.parent, attr)

    async def start(self):
        self.process.emit('goto affliate shopee')
        await self.page.goto('https://affiliate.shopee.co.id/')
        await asyncio.sleep(3)

        self.process.emit('set cookies')
        await self.set_cookies_str(self.payload['cookies'])

        self.process.emit('reload page')
        await self.page.reload()

        self.process.emit('goto product offer')
        await self.page.goto('https://affiliate.shopee.co.id/offer/product_offer')

        """
        shopee otomatis detek bot pas ada aktifitas klik-klik...
        """
        # self.process.emit('click next button')
        # next_selector = 'span[class*="page-next"]'
        # await self.page.waitForSelector(next_selector)
        # await self.page.click(next_selector)