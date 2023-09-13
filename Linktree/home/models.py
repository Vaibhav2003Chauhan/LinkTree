from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userinformation(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=1000,null=True)
    mail=models.CharField(max_length=1000,null=True)
    role=models.CharField(max_length=1000,null=True)
    description=models.TextField(max_length=1000,null=True)
    phone=models.CharField(max_length=20,null=True)
    github=models.CharField(max_length=600,null=True)
    hackerrank=models.CharField(max_length=600,null=True)
    portfolio=models.CharField(max_length=600,null=True)
    LeetCode=models.CharField(max_length=600,null=True)
    GFG=models.CharField(max_length=600,null=True)
    insta=models.CharField(max_length=600,null=True)
    Linkedin=models.CharField(max_length=600,null=True)
    twitter=models.CharField(max_length=600,null=True)
    facebook=models.CharField(max_length=600,null=True)
    Resume=models.CharField(max_length=600,null=True)
    codepen=models.CharField(max_length=600,null=True)
    profile_pic=models.ImageField(default='profile.jpg',null=True,blank=True)
    website=models.CharField(max_length=600,null=True)
    codechef=models.CharField(max_length=600,null=True)

    
    def __str__(self):
        return self.mail
