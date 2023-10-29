import aiohttp, asyncio

from . import csrf_token
from . import rbx_authentication_ticket
from . import set_cookie

class refresh:
    csrf_token: str
    rbx_authentication_ticket: str
    session: any
    working_cookies = []
    responses = []
    
    async def run(self, cookies):
        self.session = aiohttp.ClientSession()
        for cookie in cookies:
         while True:
            xtoken = await csrf_token.get(self, cookie)
            if not xtoken[1]:
                if xtoken[0]:
                    self.responses.append({"success": False, "error": "Failed to scrape csrf_token"})
                    break
                else:
                    await asyncio.sleep(1)
            else:
                break
        
         while True:
            rbx_authentication_ticke = await rbx_authentication_ticket.get(self, cookie)
            if not rbx_authentication_ticke[1]:
                if rbx_authentication_ticke[0]:
                    self.responses.append({"success": False, "error": "Failed to scrape rbx_authentication_ticket"})
                    break
                else:
                    await asyncio.sleep(1)
            else:
                break
        
         while True:
            set_cooki = await set_cookie.get(self)
            if not set_cooki[1]:
                if set_cooki[0]:
                    self.responses.append({"success": False, "error": "Failed to scrape set_cookie"})
                    break
                else:
                    await asyncio.sleep(1)
            else:
                self.responses.append({"success": True, "cookie": set_cooki[1]})
                self.working_cookies.append(set_cooki[1])
                break
        await self.session.close()
        return self.responses, self.working_cookies
        
        