import aiohttp

from .. import ccookie
from . import user_balance

class products:
    bought = []
    session: any

    def __init__(self, products, cookies: list):
        self.products = dict(sorted(products.items(), key=lambda item: int(item[0]), reverse=True))
        self.cookies = cookies
    
    async def run(self):
        self.session = aiohttp.ClientSession()
        
        for cookie in self.cookies:
            
            while True:
                xtoken = await ccookie.csrf_token.get(self, cookie)
                if not xtoken[0]:
                    continue
                else:
                    break
                
            if not xtoken[1]:
                continue
            
            while True:
                balance = user_balance.get(self, cookie)
                if not balance[0]:
                    break
                else:
                    continue
                
            if not balance[1]:
                continue
            
            
                
        await self.session.close()