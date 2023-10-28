import aiohttp, asyncio

from . import games
from . import gamepasses

class scrape:
    gamepasses = {}
    games: list
    session: any

    def __init__(self, user_id):
        self.user_id = user_id
        
    async def run(self):
        self.session = aiohttp.ClientSession()
        
        while True:
            gam = await games.get(self)
            if not gam[1]:
                if gam[0]:
                    await self.session.close()
                    return {"success": False, "error": "Failed to scrape games"}
                else:
                    await asyncio.sleep(1)
            else:
                break
            
        while True:
            gamepa = await gamepasses.get(self)
            if not self.gamepasses:
                    await self.session.close()
                    return {"success": False, "error": "Failed to scrape gamepasses"}
            else:
                await self.session.close()
                return {"success": True, "game_passes": self.gamepasses}
            