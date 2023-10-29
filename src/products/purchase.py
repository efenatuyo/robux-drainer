async def buy(self, cookie, xtoken, product_id, price, expected_seller_id):
    while True:
        purchase = (await self.session.post(f"https://economy.roblox.com/v1/purchases/products/{product_id}", 
                                       json={"expectedCurrency": 1, "expectedPrice": price, "expectedSellerId": expected_seller_id}, 
                                       headers={"X-CSRF-TOKEN": xtoken}, 
                                       cookies={".ROBLOSECURITY": cookie}))
        
        if purchase.status == 429:
            continue
        break

    
    if purchase.status == 200:
        self.total_robux_spend += price
        await delete_from_inventory(self, cookie, xtoken, self.products[str(price)][2])
        
    return purchase.status

async def delete_from_inventory(self, cookie, xtoken, id):
    while True:
        delete = (await self.session.post(f"https://www.roblox.com/game-pass/revoke", 
                                        json={"id": id}, 
                                        headers={"X-CSRF-TOKEN": xtoken}, 
                                        cookies={".ROBLOSECURITY": cookie}))
        
        if delete.status == 429: 
            continue
        
        return delete.status