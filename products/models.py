from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.name
    

class Product(models.Model):
    image = models.ImageField(upload_to='product-images', null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    city= models.ForeignKey(City,related_name='products',on_delete=models.CASCADE, null=True,blank=True)
    def __str__(self):
        return str(self.pk)