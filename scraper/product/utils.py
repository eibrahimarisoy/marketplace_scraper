from django.db.transaction import atomic

from product.models import Merchant, Price, Product


def get_merchant(merchant):
    """
    Get or create Merchant instance.
    """
    new_merchant, created = Merchant.objects.get_or_create(
        name=merchant['name'],
        city_name=merchant['city_name'],
    )
    new_merchant.seller_score = merchant["seller_score"]
    new_merchant.save()
    return new_merchant


@atomic
def set_product_data(parser):
    price = Price.objects.create(
        selling=parser.get_product_selling_price(),
        discounted=parser.get_product_discounted_price(),
    )
    merchant = {
        'name': parser.get_product_merchant_name(),
        'city_name': parser.get_product_merchant_city_name(),
        'seller_score': parser.get_product_merchant_seller_score(),
    }

    product = Product.objects.create(
        name=parser.get_product_name(),
        brand=parser.get_product_brand(),
        price=price,
        category=parser.get_product_category(),
        merchant=get_merchant(merchant),
    )

    for merchant in parser.get_product_other_merchants():
        product.other_merchants.add(get_merchant(merchant))
