from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.

class Menu(models.Model):
    CATEGORY_CHOICES = [
        ('starter','Starter'),
        ('main food','Mainfood'),
        ('specials','Specials'),
        ('dessert','Dessert'),
        ('drinks','Drinks'),
    ]
    name = models.CharField(max_length = 100)
    price = models.FloatField()
    category = models.CharField(max_length = 100,choices=CATEGORY_CHOICES)
    description = RichTextField()
    image = models.ImageField(upload_to='menu/')
    
    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    items = models.ManyToManyField(Menu)
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer.username