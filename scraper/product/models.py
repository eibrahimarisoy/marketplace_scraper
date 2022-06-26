import uuid

from django.db import models
from scraper.product.enums import BaseModelStatus


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
    merchant = models.OneToOneField(
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


class ProductPrice(BaseModel):
    selling = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Product Price'
        verbose_name_plural = 'Product Prices'

    def __str__(self):
        return f'{self.product.name} - {self.price}'



class Merchant(BaseModel):
    name = models.CharField(max_length=255)
    city_name = models.CharField(max_length=255)
    seller_score = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Merchant'
        verbose_name_plural = 'Merchants'

    def __str__(self):
        return self.name
