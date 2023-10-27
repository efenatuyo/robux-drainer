import src.cookie
import src.cookie.csrf_token as csrf_token
import src.cookie.rbx_authentication_ticket as rbx_authentication_ticket
import src.cookie.set_cookie as set_cookie

import aiohttp
import asyncio

cookieClass = cookie.refresh()

async def main():
    cookieClass.session = aiohttp.ClientSession()
    
    req = await csrf_token.get(cookieClass, "cookie")
    
    req = await rbx_authentication_ticket.get(cookieClass, "cookie")
    
    req = await set_cookie.get(cookieClass) # final cookie
    
    await cookieClass.session.close()
    
asyncio.run(main())