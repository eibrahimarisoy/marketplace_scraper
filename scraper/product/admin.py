from django.contrib import admin
from .models import Product, Price, Merchant, Scraper


class CustomProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'category', 'merchant', 'get_other_merchants')
    list_filter = ('brand', 'category', 'merchant')
    search_fields = ('name', 'brand', 'category', 'merchant')

    def get_other_merchants(self, obj):
        return ',\n'.join([str(merchant) for merchant in obj.other_merchants.all()])



class CustomScraperAdmin(admin.ModelAdmin):
    list_display = ('url', 'response')
    list_filter = ('url', 'response')
    search_fields = ('url', 'response')



    def save_model(self, request, obj, form, change):
        print("obj.url")
        super().save_model(request, obj, form, change)



admin.site.register(Product, CustomProductAdmin)
admin.site.register(Price)
admin.site.register(Merchant)
admin.site.register(Scraper, CustomScraperAdmin)
