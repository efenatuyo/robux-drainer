async def get(self):
    set_cookie = (await self.session.post("https://auth.roblox.com/v1/authentication-ticket/redeem", 
                                          headers={"rbxauthenticationnegotiation":"1"}, 
                                          json={"authenticationTicket": self.rbx_authentication_ticket}))
    set_cookie_headers = False
    try:
        cookies = set_cookie.headers.getall("set-cookie")
        for cookie in cookies:
            if cookie.startswith(".ROBLOSECURITY="):
                set_cookie_headers = cookie.split(";")[0].lstrip(".ROBLOSECURITY=")
    except:
        pass
        
    return set_cookie.status != 429, set_cookie_headers