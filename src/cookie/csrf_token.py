async def get(self, cookie):
    csrf_token = (await self.session.post("https://economy.roblox.com/", 
                                          cookies={".ROBLOSECURITY": cookie}))
    
    self.csrf_token = csrf_token.headers.get("x-csrf-token")
    return csrf_token.status != 429, bool(self.csrf_token)