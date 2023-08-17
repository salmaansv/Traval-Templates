from django.db import models
from django.contrib.auth.models import AbstractUser
class place(models.Model):
    name=models.CharField(max_length=30)
    desc=models.CharField(max_length=100)
    cover=models.ImageField(upload_to='app1/image',null=True,blank=True)


class self(models.Model):
    name=models.CharField(max_length=30)
    desc=models.CharField(max_length=30)
    cover=models.ImageField(upload_to='app1/image',null=True,blank=True)




class myuser(AbstractUser):
    place=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)

