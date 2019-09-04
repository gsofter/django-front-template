from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50, null=True)
    description=models.CharField(max_length=500, null=True)
    category = models.CharField(max_length=50, null=True)
    image_url = models.CharField(max_length=300, null=True)
    price = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)