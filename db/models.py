from django.db import models


class ProductModel(models.Model):
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
    name = models.CharField(max_length=100)
    price = models.IntegerField()