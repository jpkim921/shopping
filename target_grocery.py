import re

import json
import requests
# from lxml import etree
from lxml import html, etree
from bs4 import BeautifulSoup


class Target:

    def __init__(self, key=None, channel=None, count=None, offset=None, pricing_store_id=None, visitor_id=None):
        if key is not None:
            self.key = key
            self.channel = channel
            self.count = count
            self.offset = offset
            self.pricing_store_id = pricing_store_id
            self.visitor_id = visitor_id
        else:
            self.key = "9f36aeafbe60771e321a7cc95a78140772ab3e96"
            self.channel = "WEB"
            self.count = 24
            self.keyword = ""
            # self.keyword = "almond+milk"
            self.offset = 0
            # self.page = "%2Fs%2Falmond+milk"
            self.page = ""
            self.pricing_store_id = 3280
            self.visitor_id = "01845E8A4CC70201BD74085F456E2230"

    def get_url(self, keyword: str) -> str:
        page = f"%2Fs%2F{keyword}"
        return f"https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v2?key={self.key}&channel={self.channel}&count={self.count}&keyword={keyword}&offset={self.offset}&page={page}&pricing_store_id={self.pricing_store_id}&visitor_id={self.visitor_id}"
    
    def convert_to_keyword(self, search_keyword: str) -> str:
        return "+".join(search_keyword.split(" "))

    def get_search(self, search_keyword: str) -> list[dict]:
        keyword = self.convert_to_keyword(search_keyword)
        url = self.get_url(keyword)
        response = (requests.get(url)).json()
        products_data = response['data']['search']['products']
        products = self.format_data(products_data)
        return products
    
    def replace_char(self, text: str, pattern: str = '(&#(\w*?);)') -> str:
        """
            Method to help convert unicode to a character.
            Specifically for Target's 'Good &#38; Gather&#8482;' but can be used for others.

            '&#38;' -> '&'  

            '&#8482;' -> '™'
        """
        groups = re.findall(pattern, text)
        for group in groups:
            text = text.replace(group[0], chr(int(group[1])))
        return text

    def format_data(self, products_data):
        products = []
        for product in products_data:           
            item = {
                "buy_url": product['item']['enrichment']['buy_url'],
                "image": product['item']['enrichment']['images']['primary_image_url'],
                'title': self.replace_char(product['item']['product_description']['title']),
                'price': product['price']['formatted_current_price']
            }
            products.append(item)
        return products  


    def mock_search(self, search_keyword: None):
        print("MOCK DATA")
        with open("target_mock.json", "r") as f:
            response = json.load(f)
            products_data = response['data']['search']['products']
            # print(products_data)
            products = self.format_data(products_data)
            return products


# target = Target()
# res = target.get_search("almond milk")
# res = target.mock_search("almond+milk")
# print(res)