import pprint

import json
import requests
# from lxml import etree
from lxml import html, etree
from bs4 import BeautifulSoup


class Wholefoods:

    def __init__(self, key=None, channel=None, count=None, offset=None, pricing_store_id=None, visitor_id=None):
        pass
        
    def get_url(self, keyword: str) -> str:
        # need to figure out the store keyword situation
        return f"https://www.wholefoodsmarket.com/_next/data/gA_0Z8pXk88CJBarkJ90-/search.json?text={keyword}&store=10518"
        
    def convert_to_keyword(self, search_keyword: str) -> str:
        return "+".join(search_keyword.split(" "))

    def get_search(self, search_keyword: str) -> list[dict]:
        keyword = self.convert_to_keyword(search_keyword)
        url = self.get_url(keyword)
        response = (requests.get(url)).json()
        products_data = response['pageProps']['data']['results']
        products = self.format_data(products_data)
        return products
    
    def format_data(self, products_data):
        products = []
        for product in products_data:
            item = {
                "buy_url": f"https://www.wholefoodsmarket.com/product/{product['slug']}",
                "image": product['imageThumbnail'],
                'title': product['name'],
                'price': product['regularPrice']
            }
            products.append(item)
        return products  

    def mock_search(self, search_keyword: None):
        print("MOCK DATA")
        with open("stores/mocks/wholefoods_mock.json", "r") as f:
            response = json.load(f)
            products_data = response['pageProps']['data']['results']
            products = self.format_data(products_data)
            return products


# wf = Wholefoods()
# res = wf.get_search("dog food")
# # res = wf.mock_search("almond+milk")
# print(res)