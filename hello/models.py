from django.db import models

# Create your models here.

class Person(models.Model):
    first_name_ganti = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Child(models.Model):
    name = models.CharField(max_length=30)
    father = models.ForeignKey(Person)
