from django.contrib import admin
from .models import Product, Price, Merchant, Scraper
from .utils import set_product_data
from .parser import Parser

class CustomProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'category', 'merchant', 'get_other_merchants')
    list_filter = ('brand', 'category',)
    search_fields = ('name', 'brand', 'category', 'merchant')

    def get_other_merchants(self, obj):
        return ',\n'.join([str(merchant) for merchant in obj.other_merchants.all()])


class CustomScraperAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        parser = Parser(obj.url)
        obj.response = parser.text
        set_product_data(parser)
        super().save_model(request, obj, form, change)


admin.site.register(Product, CustomProductAdmin)
admin.site.register(Price)
admin.site.register(Merchant)
admin.site.register(Scraper, CustomScraperAdmin)
