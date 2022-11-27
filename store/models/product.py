from django.db import models
from .category import Category
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200,default=0)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    

    @staticmethod
    def get_all_products():
            return Product.objects.all()

    def __str__(self):
        return self.name   