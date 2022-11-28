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
        return f"https://www.wholefoodsmarket.com/_next/data/gA_0Z8pXk88CJBarkJ90-/search.json?text={keyword}"
        
    def convert_to_keyword(self, search_keyword: str) -> str:
        return "+".join(search_keyword.split(" "))

    def get_search(self, search_keyword: str) -> list[dict]:
        keyword = self.convert_to_keyword(search_keyword)
        url = self.get_url(keyword)
        response = (requests.get(url)).json()
        return response['data']['search']['products']

    def mock_search(self, search_keyword: None):
        print("data from mock")
        with open("wholefoods_mock.json", "r") as f:
            response = json.load(f)
            return response['pageProps']['data']['results']


wf = Wholefoods()
# print(target.convert_to_keyword('almond milk'))
# print(target.convert_to_keyword('eggs'))
# url = wf.get_url(keyword="almond+milk")
# print(url)
# res = target.get_search("almond milk")
res = wf.mock_search("almond+milk")
# import pprint
print(res)