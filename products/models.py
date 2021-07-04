from django.db import models


# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'products'
        managed = True


class Product(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='products_images', blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    class Meta:
        app_label = 'products'
        managed = True
