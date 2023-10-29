async def get(self, cookie, xtoken):
    rbx = (await self.session.get("https://www.roblox.com/mobileapi/userinfo",
                                          cookies={".ROBLOSECURITY": cookie},
                                          headers={"x-csrf-token": xtoken}))
    
    if rbx.status == 200:
        robux = (await rbx.json())["RobuxBalance"]
    else:
        robux = False
    
    return rbx.status != 429, robux

def split_money(self, balance: int):
    buy_form = {}
    for number in self.products:
        number = int(number)
        if number == 0: continue
        while True:
            if balance >= number:
                balance -= number
                if str(number) in buy_form:
                    buy_form[str(number)] += 1
                else:
                    buy_form[str(number)] = 1
            else:
                break
    return buy_form
