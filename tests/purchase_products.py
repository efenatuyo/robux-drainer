import src.products as products

import asyncio

productsClass = products.products(products={"price": ("product_id", "seller_id")}, cookies=[])

async def main():
    await productsClass.run()

asyncio.run(main())