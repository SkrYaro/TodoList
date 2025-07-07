from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=100, blank= True,null=True, default="Noname task")
    description = models.TextField(blank=True,null = True)

    levels = (
        ("low","low priority"),
        ("midle","midle priority"),
        ("high", "high priority")
    )
    level_important = models.CharField(max_length=100,choices=levels, blank=True,null=True , default=levels[1])
    owner = models.ForeignKey(User , related_name="owner",on_delete=models.CASCADE)
    time_start = models.DateTimeField(auto_now=True)
    time_end = models.DateTimeField()

    time_add = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    name = models.OneToOneField(User, related_name="profile",on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    genders = (
        ("man","чоловік"),
        ("woman","жінка"),
        ("other","інше"),
    )
    gender = models.CharField(max_length=100,choices=genders)
    ava = models.FileField(upload_to="ava/", blank=True,null=True)

    def __str__(self):
        return self.name.username