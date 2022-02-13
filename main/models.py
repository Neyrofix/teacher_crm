from django.db import models
from django.contrib.auth.models import AbstractUser


class Student(models.Model):

    first_name = models.CharField(max_length=20, verbose_name='First name')
    last_name = models.CharField(max_length=20, verbose_name='Last name')
    lvl = models.CharField(max_length=20, verbose_name='Personal LVL')
    age = models.IntegerField(default=0, verbose_name='Age')
    email = models.EmailField(verbose_name='Email')
    phone_number = models.IntegerField(null=7, verbose_name='Phone_number')
    confirm_lesson = models.BooleanField(default=False)

    group = models.ForeignKey('Group', on_delete=models.CASCADE)

    profile_img = models.ImageField(blank=True, null=True)
    special_files = models.FileField(blank=True, null=True)


class Group(models.Model):
    name = models.CharField(max_length=50)
    group_lvl = models.CharField(max_length=20, verbose_name='Group LVL')
