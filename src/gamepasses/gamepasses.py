import asyncio

async def get(self):
    await asyncio.gather(*[single_get(self, f"https://games.roblox.com/v1/games/{universe}/game-passes?limit=100&sortOrder=Asc") for universe in self.games])
    return bool(self.gamepasses)

async def single_get(self, url):
    gamepasses = await self.session.get(url)
    if gamepasses.status == 200:
        gamepasses_json = await gamepasses.json()
        for product in gamepasses_json["data"]:
            self.gamepasses[product["price"]] = product["productId"], product["sellerId"]