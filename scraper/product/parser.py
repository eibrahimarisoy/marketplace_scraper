import json
import re

import requests
from django.core.exceptions import ValidationError


class Parser:
    url = None
    text = None
    json_data = None

    def __init__(self, url):
        self.url = url
        self.get_json()
    
    def get_text(self):
        try:
            return requests.get(self.url).text
        except Exception as e:
            raise ValidationError(f'Something went wrong. When trying to get text from url. {e}')

    def get_json(self):
        self.text = self.get_text()
        m = re.search(r'window.__PRODUCT_DETAIL_APP_INITIAL_STATE__=(.+?);window.TYPageName', self.text)
        if m:
            json_text = m.group(1)
            try:
                self.json_data = json.loads(json_text)
            except Exception as e:
                raise ValidationError(f'Something went wrong. When trying to parse json. {e}')
            return
        
        raise ValidationError('Something went wrong. JSON data not found')

    def get_product_name(self):
        return self.json_data['product']['name']

    def get_product_brand(self):
        return self.json_data['product']['brand']['name']

    def get_product_discounted_price(self):
        return self.json_data['product']['price']['discountedPrice']['value']
    
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
        return self.json_data['product']['merchant'].get('sellerScore', 0)

    # Other Merchants
    def get_product_other_merchants(self):
        resp = []
        for merchant in self.json_data['product']['otherMerchants']:
            resp.append({
                'name': merchant['merchant']['name'],
                'city_name': merchant['merchant']['cityName'],
                'seller_score': merchant['merchant'].get('sellerScore', 0),
            })

        return resp
