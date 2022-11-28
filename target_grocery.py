import pprint

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
        return response['data']['search']['products']

    def mock_search(self, search_keyword: None):
        print("data from mock")
        with open("target_mock.json", "r") as f:
            response = json.load(f)
            return response['data']['search']['products']


# target = Target()
# res = target.get_search("almond milk")
# # res = target.mock_search("almond+milk")

# print(res)