from email import message
from django.db import models

 #reate your models here.
class user(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Subject=models.TextField(max_length=200)
    Message=models.TextField(max_length=200)
