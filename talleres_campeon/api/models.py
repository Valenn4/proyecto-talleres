import datetime
from django.db import models

# Create your models here.
class Category(models.Model):
    id_category = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class New(models.Model):
    title = models.CharField(max_length=100, blank=False)
    sub_title = models.TextField(max_length=200, blank=False)
    description = models.TextField(max_length=200, blank=False)
    other_description = models.TextField(max_length=200, blank=False)
    image = models.TextField(max_length=200, blank=False)
    date = models.DateTimeField(blank=False, default=datetime.datetime.now)
    category = models.ForeignKey(Category, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Match(models.Model):
    tournament = models.CharField(max_length=50, blank=False)
    instance = models.CharField(max_length=50, blank=False, default='')
    stadium = models.CharField(max_length=50, blank=False)
    one_team = models.TextField(max_length=200, blank=False)
    name_one_team = models.CharField(max_length=50, blank=False)
    two_team = models.TextField(max_length=200, blank=False)
    name_two_team = models.CharField(max_length=50, blank=False)
    date = models.DateField(blank=False)
    time = models.TimeField(blank=False)
    
    def __str__(self):
        return self.name_one_team+" - " +self.name_two_team
    
class Video(models.Model):
    url = models.TextField(max_length=250, blank=False)

    def __str__(self):
        return self.url