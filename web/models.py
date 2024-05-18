from django.db import models

class UserInfo(models.Model):
    username = models.CharField(verbose_name="姓名",max_length=32)
    password = models.CharField(verbose_name="密码",max_length=32)
    email = models.EmailField(verbose_name="邮箱",max_length=32)

class List(models.Model):
    id = models.AutoField(primary_key=True)###
    pass

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)


    