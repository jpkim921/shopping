import urllib.parse
import requests

import http.client  
from bs4 import BeautifulSoup
from bs4.element import Tag

# increase header count size. CVS servers probably not setup well
http.client._MAXHEADERS = 1000 


# reference
# url = "https://www.cvs.com/search?searchTerm=almond%20milk&refinements%5B0%5D%5Bvalue%5D=Grocery"


class Cvs:

    def __init__(self):
        pass

    def get_url(self, keyword: str) -> str:
            # page = f"%2Fs%2F{keyword}"
            return f"https://www.cvs.com/search?searchTerm={keyword}&refinements%5B0%5D%5Bvalue%5D=Grocery"

    def convert_to_keyword(self, search_keyword: str) -> str:
        return urllib.parse.quote(search_keyword)
            # return "+".join(search_keyword.split(" "))

    def get_search(self, search_keyword: str) -> list[dict]:
        keyword = self.convert_to_keyword(search_keyword)
        url = self.get_url(keyword)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        products_soup = self.get_products(soup)
        products = self.format_data(products_soup)
        return products
        
    def get_products(self, soup, selector: str = "css-1dbjc4n r-18u37iz r-tzz3ar"):
        products = soup.find_all('div', selector)
        return products

    def get_product_image(self, node: Tag) -> str:
        img_tag = node.find('img')
        return img_tag.get('src')

    def get_product_url(self, node: Tag, base_url: str = "") -> str:
        a_tag = node.find('a')
        return base_url + a_tag.get('href')

    def get_product_title(self, node: Tag) -> str:    
        div_tag = node.find('div', class_='css-901oao css-cens5h r-1khnkhu r-1jn44m2 r-ubezar r-29m4ib r-rjixqe r-kc8jnq r-fdjqy7 r-13qz1uu')
        return div_tag.text

    def get_product_price(self, node: Tag) -> str:    
        div_tag = node.find('div', class_='css-901oao r-1jn44m2 r-evnaw r-b88u0q r-135wba7')
        return div_tag.text


    def format_data(self, products_data):
        products = []
        for product in products_data:           
            item = {
                "buy_url": self.get_product_url(product, base_url="https://www.cvs.com"),
                "image": self.get_product_image(product),
                'title': self.get_product_title(product),
                'price': self.get_product_price(product)[1:],
            }
            products.append(item)
        return products

    def get_mock_html(self):
        with open('stores/mocks/cvs_mock.html', 'r') as f:
            data = f.read()
            return data

    def mock_search(self, keyword=''):
        resp = self.get_mock_html()
        soup = BeautifulSoup(resp, 'html.parser')
        products_soup = self.get_products(soup)
        products = self.format_data(products_soup)
        return products


# cvs = Cvs()
# print(cvs.mock_search())