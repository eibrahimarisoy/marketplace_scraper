import uuid

from django.db import models
from product.enums import BaseModelStatus


class BaseModel(models.Model):
    status = models.SmallIntegerField(
        default=BaseModelStatus.ACTIVE,
        choices=BaseModelStatus.choices,
    )

    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(BaseModel):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)

    price = models.OneToOneField(
        'product.Price',
        on_delete=models.CASCADE,
        related_name='product',
    )
    category = models.CharField(max_length=255)
    merchant = models.ForeignKey(
        'product.Merchant',
        on_delete=models.CASCADE,
    )
    other_merchants = models.ManyToManyField(
        'product.Merchant',
        related_name='other_merchants',
        blank=True,
    )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class Price(BaseModel):
    selling = models.DecimalField(max_digits=10, decimal_places=2)
    discounted = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)

    class Meta:
        verbose_name = 'Product Price'
        verbose_name_plural = 'Product Prices'

    def __str__(self):
        return f'Selling: {self.selling} - Discount: {self.discounted}'


class Merchant(BaseModel):
    name = models.CharField(max_length=255)
    city_name = models.CharField(max_length=255)
    seller_score = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Merchant'
        verbose_name_plural = 'Merchants'

    def __str__(self):
        return f"{self.name} - {self.city_name} - {self.seller_score}"


class Scraper(BaseModel):
    url = models.URLField()
    response = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Scraper'
        verbose_name_plural = 'Scrapers'

    def __str__(self):
        return self.url
