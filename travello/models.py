from django.db import models
from django.urls import reverse

# Create your models here.

class Destination(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})
