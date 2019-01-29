from django.db import models

# Create your models here.


class Menu(models.Model):
    num = models.IntegerField(default=0)
    text = models.CharField(max_length=50)
    pid = models.IntegerField()
    url = models.CharField(max_length=50, default='')
