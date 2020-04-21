from django.db import models

# Create your models here.

class products_scrape(models.Model):

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    rating = models.IntegerField()