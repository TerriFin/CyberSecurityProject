from django.db import models

from django.contrib.auth.models import User

class Item(models.Model):
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(default='../media/placeholder.png')

    def __str__(self):
        return self.description
