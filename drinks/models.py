from django.db import models

# Create your models here.

class Drinks(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=1000)