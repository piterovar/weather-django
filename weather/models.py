from django.db import models


class City(models.Model):
    name = models.CharField(max_length=30, verbose_name='City name')

    def __str__(self):
        return self.name
