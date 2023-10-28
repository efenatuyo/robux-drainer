async def get(self):
    set_cookie = (await self.session.post("https://auth.roblox.com/v1/authentication-ticket/redeem", 
                                          headers={"rbxauthenticationnegotiation":"1"}, 
                                          json={"authenticationTicket": self.rbx_authentication_ticket}))
    try:
        set_cookie_headers = set_cookie.headers.getall("set-cookie")[1].split(";")[0]
    except:
        set_cookie_headers = False
    return set_cookie.status != 429, set_cookie_headers