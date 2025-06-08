import asyncio
import json
import os

class Chrome:

    def __init__(self):
        super().__init__()

    def run(self):
        self.running = True
        asyncio.run(self.main())

    def stop(self):
        self.running = False

    async def main(self):
        from ichrome import ChromeDaemon
        from pyppeteer import launch

        browser = await launch({
            'handleSIGINT': False,
            'handleSIGTERM': False,
            'handleSIGHUP': False,
            'headless': False,
            'ignoreHTTPSErrors': True,
            'executablePath': ChromeDaemon.get_chrome_path(),
            'userDataDir': os.path.join(os.getcwd(), 'chrome/'),
            'devtools': False,
            'defaultViewport': False,
            'autoClose': True,
            'ignoreDefaultArgs': [
                '--enable-automation',
                '--disable-extensions',
        ]})

        self.page = await browser.newPage()

        await self.start()

        while self.running:
            await asyncio.sleep(1)

        await browser.close()

    async def set_cookies_str(self, cookies_string):
        cookies = cookies_string.split('; ')
        cookie_list = []

        for cookie in cookies:
            name, value = cookie.split('=', 1)
            cookie_dict = {
                'name': name.strip(),
                'value': value.strip()
            }
            cookie_list.append(cookie_dict)
        json_output = json.dumps(cookie_list, indent=4)

        cookies = json.loads(json_output)
        await self.page.setCookie(*cookies)