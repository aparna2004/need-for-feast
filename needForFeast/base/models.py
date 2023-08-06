from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class Items(models.Model):
    name = models.CharField(max_length=  40)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    description = models.TextField(max_length=  200,null = True)
    veg = models.CharField(max_length= 7, default='Veg')
    image = models.ImageField(upload_to='images/')
    quantity = models.PositiveIntegerField(null=True)

    def __str__(self) -> str:
        return self.name
    
class Order(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(Items,related_name='placed',blank=True)
    amount = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self) -> str:
        return f"{self.created_on}+ {self.price}"
    