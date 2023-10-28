import aiohttp
from .. import cookie

class products:
    bought = []
    session: any

    def __init__(self, products, cookies: list):
        self.products = products
        self.cookies = cookies
        