from django.db import models

# Create your models here.


class Menu(models.Model):
    num = models.IntegerField(default=0)
    text = models.CharField(max_length=50)
    pid = models.IntegerField()
    url = models.CharField(max_length=50, default='')


class User(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    user_key = models.CharField(max_length=50)


class GraspModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class GraspField(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    grasp_model_id = models.ForeignKey(GraspModel, on_delete=models.CASCADE)
