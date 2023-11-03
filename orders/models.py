from django.db import models
from account.models import CustomUser
from products.models import Product

# Create your models here.
    

class StorePlace(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    def __str__(self):
        return str(self.name)
    


class Order(models.Model):
    ordering_date= models.DateTimeField(auto_now_add=True)
    ordered_by = models.ForeignKey(CustomUser,related_name='orders',on_delete=models.SET_NULL,null=True,blank=True)
    shipping_place = models.ForeignKey(StorePlace,related_name='orders',on_delete=models.SET_NULL,null=True,blank=True)
    status = models.IntegerField(default=0)
    def __str__(self):
        return str(self.ordering_date)
    

class OrderItem(models.Model):
    price = models.IntegerField( null=True, blank=True)
    quantity = models.IntegerField( null=True, blank=True)
    order = models.ForeignKey(Order,related_name='order_items', on_delete=models.SET_NULL,null=True,blank=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return str(self.pk)