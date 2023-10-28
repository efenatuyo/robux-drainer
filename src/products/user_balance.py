async def get(self, cookie):
    rbx = (await self.session.post("https://www.roblox.com/mobileapi/userinfo", 
                                          cookies={".ROBLOSECURITY": cookie}))
    
    if rbx.status == 200:
        robux = (await rbx.json())["RobuxBalance"]
    else:
        robux = False
        
    return rbx.status != 429, robux

def split_money(self, balance: int):
    buy_form = []
    for number in self.products:
        number = int(number)
        while True:
            if balance >= number:
                if number in buy_form:
                    buy_form[number] += 1
                else:
                    buy_form[number] = 1
            else:
                break
    return buy_form