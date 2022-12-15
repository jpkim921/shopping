import json
import pprint
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

def mock_html_response():
    with open('stores/mocks/walmart_mock.html', 'r') as f:
        return BeautifulSoup(f.read(), 'html.parser')

# soup = BeautifulSoup(mock_html_response(), 'html.parser')
# print(soup)

def keyword(search_keyword):
    return "+".join(search_keyword.split(" "))

def get_html(search_keyword: str = "almond milk"):
    base_url = "https://www.walmart.com/search"
    params = {
        "q":keyword(search_keyword)
    }
    headers = {
    "Host": "www.walmart.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:107.0) Gecko/20100101 Firefox/107.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    # "Cookie": 'vtc=Szt7bf2OXvokSSnuxyu72g; dimensionData=733; TS012768cf=01a226317f4be69eb931493489399bc4d8a7de0c8e945d0c6f8cdd6ea20234590e5c07c0882c82d7fafb7886dcb18b938450318381; TS2a5e0c5c027=08b99f1cf2ab2000321619ab57466c7c010e948d745586a3faa20a4482a08e17162fae5df1b45b430819fccc2a113000fb396f8a9de22979caf7ed752b6339f60304b2713785b8edb5ffc95fb041b9a0350c5cf184ecf80a14a29e362d70a143; akavpau_p2=1669989232~id=e17b8b5e3fc4a53745946153ebff17d0; ACID=42276c36-06a0-45ec-ad18-d6cb4acf488b; hasACID=true; assortmentStoreId=3520; hasLocData=1; TB_Latency_Tracker_100=1; TB_Navigation_Preload_01=1; TB_SFOU-100=; _pxhd=49ace01de70d884d09191ebc0b0c691efaf155134e53f3444cceb2b54f765c91:c41e0e01-71c5-11ed-9bf4-4b5a504f6757; xptwg=497242603:BB2BB9817C2A78:1E16042:1DB56B52:397AC7BA:DD8A782A:; xptwj=rq:27bf4de040028c5b5930:5ggOXlxLn/L7j55uQ+lYi+7qD7rv30tQEOWhW5daBOY8uEXJj7qYiF1KTYE4KgGc3GK/ivVCZD61WxF4Wl1svZvTtQx801WqQ5dycnOWiDFn4z8lJ1dmOCjl4+c9GRs=; TS01a90220=01a226317f4be69eb931493489399bc4d8a7de0c8e945d0c6f8cdd6ea20234590e5c07c0882c82d7fafb7886dcb18b938450318381; com.wm.reflector="reflectorid:0000000000000000000000@lastupd:1669988637000@firstcreate:1669932974257"; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjpmYWxzZSwicGlja3VwIjp7Im5vZGVJZCI6IjM1MjAiLCJ0aW1lc3RhbXAiOjE2Njk5MzI5NzQzMTh9LCJwb3N0YWxDb2RlIjp7InRpbWVzdGFtcCI6MTY2OTkzMjk3NDMxOCwiYmFzZSI6IjExMzczIn0sIm1wIjpbXSwidmFsaWRhdGVLZXkiOiJwcm9kOnYyOjQyMjc2YzM2LTA2YTAtNDVlYy1hZDE4LWQ2Y2I0YWNmNDg4YiJ9; TBV=7; pxcts=c5f28df9-71c5-11ed-a147-4d6352426766; _pxvid=c41e0e01-71c5-11ed-9bf4-4b5a504f6757; _astc=e0c2a4be6f2891090b35585d3b6bfba9; adblocked=false; wmlh=a54553cd074e29673f1176e82eeec13bf1fc10e021d4525a676388226f89a44b; tb_sw_supported=false; auth=MTAyOTYyMDE4LhGcrc9AZF8J74Y640iYUN8qKQFbOzmWh9sydlzaZ3HJIitcXrjcGZBYkfB%2BoOOb5FXxVuRJ8Y0DU556EHzz5lWjztKVbktrrgy3q48aBJpyx3iwkGE3X6taP%2F5RYqjt767wuZloTfhm7Wk2Kcjygp0i2CSRVbB3L7ys%2FtvUzQeDsi12po5J%2FGygmo6v0uBaCjQwCGbq6br2RjGujmR48xYQWzgGGT7%2B0W2j3n5%2BAuwUMk70P8glgOEpLOprhDfMM%2FFHGZ2dCNmxWrdkwqEKruFFhBx3O9%2FNt071DSoTPHcNq%2B4%2Fj8Ftd38xBix5qT0XUgR5NUtecM%2BvWA%2BpMqKEyVZo6jW9Ur1Ij%2BSN%2Bw0%2BcUO6qBIZF%2BZhhryedrdpEKqtlhrjpBQyqvytQiK9tsTJiVjKcklje4R5ioW78kDnDBU%3D; bstc=W16cFzqBGq4nDqq9yWTB4Q; mobileweb=0; xptc=assortmentStoreId%2B3520; xpth=x-o-mverified%2Bfalse; xpa=-D7hT|7DSK-|jowo9|vZXvx; xpm=0%2B1669988640%2BSzt7bf2OXvokSSnuxyu72g~%2B0; exp-ck=-D7hT17DSK-1jowo92; ak_bmsc=A8A7BE2E5AEABB6E30ECD4DE02BAA125~000000000000000000000000000000~YAAQRJUzuEOXooeEAQAAKk0U0xEiClmI8eNuFgzy5mYgySMd+BpZrnvnOBtI8nJASUzGxORvlr3bYXQEXDgXP0REDrZeuHLsWPCNm7hoD60F5YGSnPQB5XAeAZFUcE4HciSI+7WVc3vuuMiYZpNa7SdyOXaETfliX5NsT+4llnym7syRmWkJov3v1NlZSfxe7wcnNrRX+7sqm2UkSXfL63KNLkMvwWwfjplHs+ovdKg3ZOt0C9AByksED/lgHKE0oMOY/ep8p1RcxSimax+1kiQbYZaQCINsjWsocbRkjZ0VXefPeYCgLeTj1qtTOBZI/hQVuMbTYO184yum2OZwZwcg9gCDPj5vcPNlZXwZOMUyRTw9TxkzvrYpB1aL1u+xS/L5QqzcMSP7cfr1ch/HKkuWQW65xwAHa8NXsKWFDgUe3i+8mEw9QQMgA12mq6szGLWThq5JyhI+ayFojhOgqL66J1AWiZEl+GKpbig=; bm_sv=E37DD029B74A3782B0E6B850BEC42E86~YAAQRJUzuFWZooeEAQAAVFsU0xEOJVCklFMR7XzK7Wkcv+oYlsarjkLXLhbCAqi6LTor/ukucXAiTt+PBpCM8at2+N6tsM+HH1H9Dxb6wA+RnJUG8qi9phcZUPOQ2++PHSQdOF48cTuHIQPpwj2AOPJZvXvYMPnRYoUDD29IPZ70lxrOVUFWDo2bWlfjcdF8JnwS+zquVHxqjcX8WhJExsROspY0Hm1vMNPdIlmzZuN8r4pklK/bXQUBdekJo1eVOA==~1; locDataV3=eyJpc0RlZmF1bHRlZCI6ZmFsc2UsImlzRXhwbGljaXQiOmZhbHNlLCJpbnRlbnQiOiJTSElQUElORyIsInBpY2t1cCI6W3siYnVJZCI6IjAiLCJub2RlSWQiOiIzNTIwIiwiZGlzcGxheU5hbWUiOiJTZWNhdWN1cyBTdXBlcmNlbnRlciIsIm5vZGVUeXBlIjoiU1RPUkUiLCJhZGRyZXNzIjp7InBvc3RhbENvZGUiOiIwNzA5NCIsImFkZHJlc3NMaW5lMSI6IjQwMCBQYXJrIFBsIiwiY2l0eSI6IlNlY2F1Y3VzIiwic3RhdGUiOiJOSiIsImNvdW50cnkiOiJVUyIsInBvc3RhbENvZGU5IjoiMDcwOTQtMzY1NCJ9LCJnZW9Qb2ludCI6eyJsYXRpdHVkZSI6NDAuNzkyOTg3LCJsb25naXR1ZGUiOi03NC4wNDI0Mjl9LCJpc0dsYXNzRW5hYmxlZCI6dHJ1ZSwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJodWJOb2RlSWQiOiIzNTIwIiwic3RvcmVIcnMiOiIwNjowMC0yMzowMCIsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIlBJQ0tVUF9DVVJCU0lERSIsIlBJQ0tVUF9JTlNUT1JFIl19XSwic2hpcHBpbmdBZGRyZXNzIjp7ImxhdGl0dWRlIjo0MC43Mzc4LCJsb25naXR1ZGUiOi03My44NzgyLCJwb3N0YWxDb2RlIjoiMTEzNzMiLCJjaXR5IjoiRWxtaHVyc3QiLCJzdGF0ZSI6Ik5ZIiwiY291bnRyeUNvZGUiOiJVU0EiLCJnaWZ0QWRkcmVzcyI6ZmFsc2V9LCJhc3NvcnRtZW50Ijp7Im5vZGVJZCI6IjM1MjAiLCJkaXNwbGF5TmFtZSI6IlNlY2F1Y3VzIFN1cGVyY2VudGVyIiwiYWNjZXNzUG9pbnRzIjpudWxsLCJzdXBwb3J0ZWRBY2Nlc3NUeXBlcyI6W10sImludGVudCI6IlBJQ0tVUCIsInNjaGVkdWxlRW5hYmxlZCI6ZmFsc2V9LCJpbnN0b3JlIjpmYWxzZSwicmVmcmVzaEF0IjoxNjcwMDEwMjM3MjgwLCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6NDIyNzZjMzYtMDZhMC00NWVjLWFkMTgtZDZjYjRhY2Y0ODhiIn0%3D; __cf_bm=bag4lHb1u6MAeAKS3.woWJmjh.9qnpQ4EBz9gkcDvHk-1669988641-0-Ac4FY3If3uDc+n+6VZdKV5Ps/ioImpkpynYZ7f/ELmrNjE0YI9Fg8j5j1fn/EMSr/ZeDYFqDdvtvTJlPhKJJBDbpm1RD86xTbZSqqa3b/Pyo',
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    }
    response = requests.get(url=base_url, headers=headers, params=params)
    return BeautifulSoup(response.text, 'html.parser')

# soup = get_html()

# products = soup.find_all(class_="sans-serif mid-gray relative flex flex-column w-100 hide-child-opacity")

# sproduct = '<div class="sans-serif mid-gray relative flex flex-column w-100 hide-child-opacity" data-item-id="504QV2C2LBIC"><a class="absolute w-100 h-100 z-1 hide-sibling-opacity" href="https://wrd.walmart.com/track?adUid=320d25a6-7270-4543-a2a1-19b5871192c2&amp;tax=976759_9176907_4405816_3107987_3226399&amp;pltfm=desktop&amp;pgId=almond%20milk&amp;spQs=ps7tko8QHoq2v9X6M-XyY7lqJl2YCLCdmcDVCntir1JnfyApJlr8Lw0gtI_VWNB--3iJNutvYaseoIJb3_nRDNTB6_P-FGVR2QZF_ipUad0hWhq8rZSWs0IdzsWvbgfBOIRyuNyEan4U9k0eTSVqTjg_HfT4YM9Sbn7hkqRzM3cVlUQbsOVfWVkMj-fKzLW1s9GDZoll39F0AuvcT4JnEnFksG7q4UhI76U9XV5Q6Fhj9R0Q1S7yNFSTBHo7arNw&amp;storeId=3520&amp;pt=search&amp;mloc=sp-search-middle&amp;bkt=2633&amp;rdf=1&amp;plmt=sp-search-middle~desktop~&amp;eventST=click&amp;pos=1&amp;bt=1&amp;rd=https%3A%2F%2Fwww.walmart.com%2Fip%2FSilk-Almond-Milk-Original-Dairy-Free-Gluten-Free-96-FL-OZ-Bottle%2F675466777%3Fathbdg%3DL1600&amp;couponState=na&amp;athbdg=L1600" link-identifier="675466777" target=""><span class="w_iUH7">Silk Almond Milk, Original, Dairy Free, Gluten Free, 96 FL OZ Bottle<!-- --> </span></a><div class="" data-testid="list-view"><div class=""><div class="h2 relative mb2"><span class="w_VbBP w_mFV6 w_awtt absolute tag-leading-badge">Best seller</span></div><div class="relative"><div class="relative overflow-hidden" style="max-width:290px;height:0;padding-bottom:min(392px, 135.17241379310346%);align-self:center;width:min(290px, 100%)"><img alt="Silk Almond Milk, Original, Dairy Free, Gluten Free, 96 FL OZ Bottle" class="absolute top-0 left-0" data-testid="productTileImage" height="" loading="eager" src="https://i5.walmartimages.com/asr/3d8266cf-fba1-4b66-ab13-1b7f99d75485.f72ec152fdbdfe7573ba0f5aeb92deb8.jpeg?odnHeight=784&amp;odnWidth=580&amp;odnBg=FFFFFF" srcset="https://i5.walmartimages.com/asr/3d8266cf-fba1-4b66-ab13-1b7f99d75485.f72ec152fdbdfe7573ba0f5aeb92deb8.jpeg?odnHeight=392&amp;odnWidth=290&amp;odnBg=FFFFFF 1x, https://i5.walmartimages.com/asr/3d8266cf-fba1-4b66-ab13-1b7f99d75485.f72ec152fdbdfe7573ba0f5aeb92deb8.jpeg?odnHeight=784&amp;odnWidth=580&amp;odnBg=FFFFFF 2x" width=""/></div><div class="z-2 absolute bottom--1"><div class="relative dib"><button aria-label="Add to cart - Silk Almond Milk, Original, Dairy Free, Gluten Free, 96 FL OZ Bottle" class="w_hhLG w_8nsR w_jDfj pointer bn sans-serif b ph2 flex items-center justify-center w-auto shadow-1" data-automation-id="add-to-cart" type="button"><i class="ld ld-Plus" style="font-size:1.5rem;vertical-align:-0.25em" title="add to cart"></i><span class="mr2">Add</span></button></div></div></div><div class="mt5 mb1" data-testid="variant-504QV2C2LBIC" style="height:24px"><div class="flex items-center lh-title h2-l normal"><span class="gray f7">Sponsored</span></div></div></div><div class=""><div class="flex flex-wrap justify-start items-center lh-title mb2 mb1-m" data-automation-id="product-price"><div aria-hidden="true" class="mr1 mr2-xl b black lh-copy f5 f4-l">$5.38</div><span class="w_iUH7">current price $5.38</span><div class="f7 f6-l gray mr1">5.6 ¢/fl oz</div></div><span class="w_V_DM" style="-webkit-line-clamp:3;padding-bottom:0em;margin-bottom:-0em"><span class="normal dark-gray mb0 mt1 lh-title f6 f5-l" data-automation-id="product-title">Silk Almond Milk, Original, Dairy Free, Gluten Free, 96 FL OZ Bottle</span></span><div class="flex items-center mt2"><span class="black inline-flex mr1"><i aria-hidden="true" class="ld ld-StarFill" style="font-size:12px;vertical-align:-0.175em"></i><i aria-hidden="true" class="ld ld-StarFill" style="font-size:12px;vertical-align:-0.175em"></i><i aria-hidden="true" class="ld ld-StarFill" style="font-size:12px;vertical-align:-0.175em"></i><i aria-hidden="true" class="ld ld-Star" style="font-size:12px;vertical-align:-0.175em"></i><i aria-hidden="true" class="ld ld-Star" style="font-size:12px;vertical-align:-0.175em"></i></span><span aria-hidden="true" class="sans-serif gray f7">394</span><span class="w_iUH7">3 out of 5 Stars. 394 reviews</span></div><div class="mt2"><img alt="ebt" aria-hidden="true" class="v-mid pb1 mr2" height="20" loading="lazy" src="//i5.walmartimages.com/dfw/63fd9f59-2845/2044d79e-92d5-4c08-90a2-0480444a877f/v1/EBT-Logo.svg" width="30"/><span class="gray f6-l f5-m">EBT eligible</span></div><div class="mt2 mb2"><span class="w_VbBP w_mFV6 w_I_19 mr1 mt1 ph1">Pickup</span></div></div></div></div>'

# soup = BeautifulSoup(product, 'html.parser')





def get_product_url(node: Tag, base_url: str = "") -> str:
    a_tag = node.find('a')
    return a_tag.get('href')

def get_product_image(node: Tag) -> str:
    img_tag = node.find('img')
    return img_tag.get('src')

def get_product_title(node: Tag) -> str:
    span_tag = node.find('span', attrs={'data-automation-id': 'product-title'})
    return span_tag.text

def check_sponsored(node: Tag) -> bool:
    if node.find(string='Sponsored'):
        return True
    return False

# print(check_sponsored(soup))
# print(get_product_url(soup))
# print(get_product_image(soup))
# print(get_product_title(soup))


# item = {
#     "buy_url": product['item']['enrichment']['buy_url'],
#     "image": product['item']['enrichment']['images']['primary_image_url'],
#     'title': self.replace_char(product['item']['product_description']['title']),
#     'price': product['price']['formatted_current_price']
# }


"""
Initialize Walmart class.
Pass in search keyword.
Get response.
Parse response and create a dictionary of items according to schema.
"""

soup = mock_html_response()
# soup = get_html()


# products: list[Tag] = soup.find_all('div', class_="sans-serif mid-gray relative flex flex-column w-100 hide-child-opacity")
products: list[Tag] = soup.find_all(class_="hide-sibling-opacity")
print(products)
# for idx, product in enumerate(products):

#     print(idx)
#     print(check_sponsored(product))
#     print(get_product_url(product))
#     print(get_product_image(product))
#     print(get_product_title(product))

# container = 'flex flex-wrap w-100 flex-grow-0 flex-shrink-0 ph2 pr0-xl pl4-xl mt0-xl mt3'
# prod = soup.find('div', attrs={'data-item-id': '38813XM6RVWL'})
# print(prod)