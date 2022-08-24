from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=100,default="")
    lastname=models.CharField(max_length=100,default="")
    image=models.ImageField(upload_to='profile_pics',default="default.jfif")
    bio=models.TextField(default='')
    def __str__(self):
        return self.user.username