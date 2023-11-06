from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    release_date = models.DateField()
    genre = models.CharField(max_length=50)
    platform = models.CharField(max_length=50)

    def __str__(self):
        return self.title
