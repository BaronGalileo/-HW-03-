from django.db import models

# Create your models here.

class MyText(models.Model):
    text = models.TextField(null=False, blank=False)
    count = models.TextField(null=True, blank=True)
    wordcount = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.count

