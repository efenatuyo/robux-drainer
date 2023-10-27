import src.gamepasses as gamepasses
import src.gamepasses.games as games

import aiohttp
import asyncio
gameClass = gamepasses.scrape(80254)

async def main():
    gameClass.session = aiohttp.ClientSession()
    
    print(await games.get(gameClass))
    await gameClass.session.close()

asyncio.run(main())