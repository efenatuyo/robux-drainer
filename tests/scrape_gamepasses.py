import src.gamepasses as experiences

import aiohttp
import asyncio

gameClass = experiences.scrape(815394717)

async def main():
    await gameClass.run()
    
    await gameClass.session.close()

asyncio.run(main())