from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    in_stock = models.BooleanField(default=False)

    def __str__(self):
        return self.title
