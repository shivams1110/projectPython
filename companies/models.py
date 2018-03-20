from django.db import models

class Stock(models.Model):
    ticker = models.CharField(max_length=10)
    open = models.FloatField()
    close = models.FloatField()
    vloume = models.IntegerField()

    def __str__(self):
        return self.ticker


class File(models.Model):
    file = models.FileField(blank=False, null=False)
    userId = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.file
