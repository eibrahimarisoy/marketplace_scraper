# Generated by Django 3.2.13 on 2022-06-26 12:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('status', models.SmallIntegerField(choices=[(1, 'Active'), (0, 'Suspended'), (-1, 'Deleted')], default=1)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('city_name', models.CharField(max_length=255)),
                ('seller_score', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
            options={
                'verbose_name': 'Merchant',
                'verbose_name_plural': 'Merchants',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('status', models.SmallIntegerField(choices=[(1, 'Active'), (0, 'Suspended'), (-1, 'Deleted')], default=1)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('selling', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discounted', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(max_length=3)),
            ],
            options={
                'verbose_name': 'Product Price',
                'verbose_name_plural': 'Product Prices',
            },
        ),
        migrations.CreateModel(
            name='Scraper',
            fields=[
                ('status', models.SmallIntegerField(choices=[(1, 'Active'), (0, 'Suspended'), (-1, 'Deleted')], default=1)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('url', models.URLField()),
                ('response', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Scraper',
                'verbose_name_plural': 'Scrapers',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('status', models.SmallIntegerField(choices=[(1, 'Active'), (0, 'Suspended'), (-1, 'Deleted')], default=1)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.merchant')),
                ('other_merchants', models.ManyToManyField(blank=True, related_name='other_merchants', to='product.Merchant')),
                ('price', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.price')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
