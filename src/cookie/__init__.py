import aiohttp, asyncio

from . import csrf_token
from . import rbx_authentication_ticket
from . import set_cookie

class refresh:
    csrf_token: str
    rbx_authentication_ticket: str
    session: any
    
    async def run(self, cookie):
        self.session = aiohttp.ClientSession()
        
        while True:
            xtoken = await csrf_token.get(self, cookie)
            if not xtoken[1]:
                if xtoken[0]:
                    return {"success": False, "error": "Failed to scrape csrf_token"}
                else:
                    await asyncio.sleep(1)
            else:
                break
        
        while True:
            rbx_authentication_ticke = await rbx_authentication_ticket.get(self, cookie)
            if not rbx_authentication_ticke[1]:
                if rbx_authentication_ticke[0]:
                    return {"success": False, "error": "Failed to scrape rbx_authentication_ticket"}
                else:
                    await asyncio.sleep(1)
            else:
                break
        
        while True:
            set_cooki = await set_cookie.get(self)
            if not set_cooki[1]:
                if set_cooki[0]:
                    return {"success": False, "error": "Failed to scrape rbx_authentication_ticket"}
                else:
                    await asyncio.sleep(1)
            else:
                return {"success": True, "cookie": set_cooki[1]}
        
        