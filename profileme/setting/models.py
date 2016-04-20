from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.forms import TextInput


class Thing(models.Model):
    first_name = models.CharField(max_length=255,null=True,blank=True)
    last_name = models.CharField(max_length=255,null=True , blank=True)
    pan = models.CharField(max_length=10,unique=True)
    # phone = models.CharField(TextInput(attrs={'type': 'number'}),max_length=11,null=True)
    dob = models.CharField(max_length=10,null=True,blank=True)
    phone = models.CharField(max_length=10,null=True,blank=True)
    slug = models.SlugField(unique=True)
    # adding this line so the user can own thing
    user = models.OneToOneField(User, blank=True, null=True)
