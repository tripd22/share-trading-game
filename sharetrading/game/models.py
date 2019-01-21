from django.db import models

class Session(models.Model):
    name = models.CharField(max_length=200)
    score = models.IntegerField(default=77)
