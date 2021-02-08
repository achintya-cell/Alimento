from django.db import models

# Create your models here.

class QuickOrder(models.Model):
    city = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)

    def __str__(self):
        return self.name