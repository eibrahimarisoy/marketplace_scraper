import json
import requests
import re

# resp = requests.get("https://www.trendyol.com/atari/retro-mini-620-mario-oyunlu-av-retro-mini-oyun-konsolu-scart-basliksiz-p-36587919?boutiqueId=609036&merchantId=206709")
# text = resp.text
# print('window.__PRODUCT_DETAIL_APP_INITIAL_STATE__=' in text)


# m = re.search(r'window.__PRODUCT_DETAIL_APP_INITIAL_STATE__=(.+?);window.TYPageName', text)
# if m:
#     json_text = m.group(1)
#     json_data = json.loads(json_text)

#     print(json_data)


class Parser:
    url = None
    text = None
    json_data = None

    def __init__(self, url):
        self.url = url
        self.text = self.get_text()
        self.get_json()
    
    def get_text(self):
        return requests.get(self.url).text

    def get_json(self):
        m = re.search(r'window.__PRODUCT_DETAIL_APP_INITIAL_STATE__=(.+?);window.TYPageName', self.text)
        if m:
            json_text = m.group(1)
            self.json_data = json.loads(json_text)

    def get_product_name(self):
        return self.json_data['product']['name']

    def get_product_brand(self):
        return self.json_data['product']['brand']['name']

    def get_product_discounted_price(self):
        return self.json_data['product']['price']['dicountedPrice']['value']
    
    # Price
    def get_product_selling_price(self):
        return self.json_data['product']['price']['sellingPrice']['value']
    
    def get_product_price_currency(self):
        return self.json_data['product']['price']['currency']

    # Category
    def get_product_category(self):
        return self.json_data['product']['category']['hierarchy']

    # Merchant
    def get_product_merchant_name(self):
        return self.json_data['product']['merchant']['name']
    
    def get_product_merchant_city_name(self):
        return self.json_data['product']['merchant']['cityName']
    
    def get_product_merchant_seller_score(self):
        return self.json_data['product']['merchant']['sellerScore']

    # Other Merchants
    def get_product_other_merchants(self):
        resp = []
        for merchant in self.json_data['product']['otherMerchants']:
            resp.append({
                'name': merchant['name'],
                'city_name': merchant['cityName'],
                'seller_score': merchant['sellerScore'],
            })

        return resp