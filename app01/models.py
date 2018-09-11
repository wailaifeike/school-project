from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)


class UserToken(models.Model):
    user = models.ForeignKey(to="UserInfo",on_delete=models.CASCADE)
    token = models.CharField(max_length=128)

class Notice(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField(null=True,blank=True)
    user = models.ForeignKey(to="UserInfo",on_delete=models.CASCADE,default=1)
    ctime = models.DateTimeField(auto_created=True)
    choices = (("1","未审核"),
              ("2","审核中"),
              ("3","已发布"))
    status = models.CharField(choices=choices,default="1",max_length=4)
