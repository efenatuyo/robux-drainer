import src.gamepasses as experiences
import src.gamepasses.games as games
import src.gamepasses.gamepasses as gamepasses

import aiohttp
import asyncio

gameClass = experiences.scrape(815394717)

async def main():
    gameClass.session = aiohttp.ClientSession()
    
    await games.get(gameClass)

    await gamepasses.get(gameClass)
    
    gameClass.gamepasses
    
    await gameClass.session.close()

asyncio.run(main())