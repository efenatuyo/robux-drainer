import src.gamepasses as experiences

import asyncio

gameClass = experiences.scrape(815394717)

async def main():
    await gameClass.run()

asyncio.run(main())