from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    userRandomNumber = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=128)
    userAge = models.CharField(max_length=32)
    userSex = models.CharField(max_length=32)
    HearLoss = models.CharField(max_length=32)
    userLEar = models.CharField(max_length=32)
    userLEarAid = models.CharField(max_length=32)
    userREar = models.CharField(max_length=32)
    userREarAid = models.CharField(max_length=32)


class UserListen(models.Model):
    userRandomNumber = models.AutoField(primary_key=True)
    userListenSex = models.CharField(max_length=32)
    userListenAge = models.CharField(max_length=32)
    gaussianNoise = models.CharField(max_length=32)


class UploadFileModel(models.Model):
    name = models.CharField(max_length=64)
    path = models.FileField(upload_to='files/')
