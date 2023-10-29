import src.cookie as cookie

import asyncio

cookieClass = cookie.refresh()

async def main():
    print(await cookieClass.run(["_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|"]))

asyncio.run(main())