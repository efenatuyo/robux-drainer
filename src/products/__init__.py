import aiohttp

class products:
    bought = []
    session = aiohttp.ClientSession()

    def __init__(self, products, cookies: list):
        self.products = products
        self.cookies = cookies
        
        
    async def xtoken_get(self, cookie):
        csrf_token = (await self.session.post("https://economy.roblox.com/", 
                                          cookies={".ROBLOSECURITY": cookie}))
        
        x_token = csrf_token.headers.get("x-csrf-token")
        return csrf_token.status != 429, bool(x_token), x_token