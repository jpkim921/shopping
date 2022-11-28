import pprint

import json
import requests
# from lxml import etree
from lxml import html, etree
from bs4 import BeautifulSoup

# url = "https://www.target.com/c/grocery/-/N-5xt1a"
# groceries = requests.get(url)
# # print(groceries.text)

# soup = BeautifulSoup(groceries.text, "html.parser")
# # soup
# scripts = soup.findAll('script')
# len(scripts)
# # scripts[71]
# target_script = ""
# for i, s in enumerate(scripts):
#     if '__TGT_DATA__' in s.text:
#         print(i)
#         target_script = s.text.strip()
#         break


# target_script = target_script.replace("\\", "")
# target_script
# # s_split = "'__TGT_DATA__': { configurable: false, enumerable: true, value: deepFreeze(JSON.parse(\""
# s_split = '{ "__PRELOADED_QUERIES__": {"queries":[[["@web/domain-content/get-page-content",{"breadcrumbs":true,"children":true,"url":"/c/-/N-5xt1a"'
# first = target_script.split(s_split)
# first[1]
# end = len(first[1])-71437
# final = first[1][615:end]
# final
# j = json.dumps([final])
# # j = json.loads(final)
# json.loads(j)


base_url = "https://redsky.target.com/redsky_aggregations/v1/web/taxonomy_subcategories_v1?category_id=5xt1a&key=9f36aeafbe60771e321a7cc95a78140772ab3e96&channel=WEB&page=%2Fc%2F5xt1a"
url2 = "https://redsky.target.com/redsky_aggregations/v1/web/taxonomy_subcategories_v1?category_id=5xt1a&key=9f36aeafbe60771e321a7cc95a78140772ab3e96&channel=WEB&page=%2Fc%2F5xt1a"
url3 = "https://redsky.target.com/redsky_aggregations/v1/web/taxonomy_subcategories_v1?category_id=u7fty&key=9f36aeafbe60771e321a7cc95a78140772ab3e96&channel=WEB&page=%2Fc%2Fu7fty"
r = requests.get(url2)
data = json.loads(r.text)
pprint.pprint(data['data']['related_categories']['children'])