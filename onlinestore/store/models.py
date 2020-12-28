from django.db import models

class Item(models.Model):
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    image = models.ImageField(default='../media/placeholder.png')
    class Meta:
        permissions = [
            ('manager', 'Can Manage Items')
        ]

    def __str__(self):
        return self.description
