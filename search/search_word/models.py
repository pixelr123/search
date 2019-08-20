from django.db import models


class Word(models.Model):
    name = models.CharField(max_length=200, primary_key = True)
    frequency = models.BigIntegerField()

    def __str__(self):
        return self.name