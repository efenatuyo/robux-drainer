async def get(self, cookie):
    rbx_authentication_ticket = (await self.session.post("https://auth.roblox.com/v1/authentication-ticket", 
                                                         headers={"rbxauthenticationnegotiation":"1", "referer": "https://www.roblox.com/camel", 'Content-Type': 'application/json', "x-csrf-token": self.csrf_token}, 
                                                         cookies={".ROBLOSECURITY": cookie}))
    
    self.rbx_authentication_ticket = rbx_authentication_ticket.headers.get("rbx-authentication-ticket")
    return rbx_authentication_ticket.status != 429, bool(self.rbx_authentication_ticket)