from django.db import models
from apps.products import models as product
# Create your models here.

class Sale(models.Model):

    id = models.AutoField(primary_key=True)
    datetime = models.DateTimeField()
    total_revenue = models.FloatField()
    total_products = models.IntegerField()


class SaleProduct(models.Model):

    id = models.AutoField(primary_key=True)
    sale = models.ForeignKey('Sale', on_delete=models.CASCADE)
    product = models.ForeignKey(product.Product, on_delete=models.CASCADE)

    quatity = models.IntegerField()
