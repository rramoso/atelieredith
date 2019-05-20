from django.conf import settings
from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    descripcion = models.CharField(max_length=200)
    type = models.CharField(max_length=10)
    available = models.BooleanField()
    stock = models.IntegerField()



    def addToStock(self, num):
        self.stock += num


class ProductImage(models.Model):

    id = models.AutoField(primary_key = True)
    product = models.ForeignKey('Product', on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'img/product-img/', blank=True, null=True)
