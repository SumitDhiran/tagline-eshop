from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    PRODUCT_TYPE = (
        ('Available','Available'),
        ('Sold','Sold'),
    )
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='product')
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    type = models.CharField(max_length=200, choices=PRODUCT_TYPE)
    image = models.ImageField(upload_to='products/', default = 'products/default.png', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.name)


class Purchase(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    buyer = models.ForeignKey(User,on_delete=models.CASCADE)
    purchase_price = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.product)

    @property
    def seller(self):
        return str(self.product.owner)

    @property
    def product_name(self):
        return str(self)