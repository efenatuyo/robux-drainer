import aiohttp

from .. import cookie as ccookie
from . import user_balance
from . import purchase

class products:
    total_robux_spend = 0
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
                balance = await user_balance.get(self, cookie)
                if not balance[0]:
                    continue
                else:
                    break
                
            if not balance[1]:
                continue
            
            buy_form = user_balance.split_money(self, balance[1])
            for price, amount in buy_form.items():
                for i in range(amount):
                    await purchase.buy(self, cookie, xtoken[-1], self.products[price][0], int(price), self.products[price][1])
            
        await self.session.close()
        return self.total_robux_spend
