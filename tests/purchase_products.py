import src.products as products

import asyncio

productsClass = products.products(products={"price": ("product_id", "seller_id", "asset_id")}, cookies=["_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|"])

async def main():
    await productsClass.run()

asyncio.run(main())