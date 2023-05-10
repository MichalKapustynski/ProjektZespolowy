from django.db import models
from sorl.thumbnail import ImageField

class Person(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    #birth_date = models.CharField(max_length=50,default='')
    phone_number = models.CharField(max_length=50)
    mail = models.EmailField()
    address = models.CharField(max_length=150)
    photo = models.ImageField()
    

class Experience(models.Model):
    time = models.CharField(max_length=30)
    exp = models.CharField(max_length=200)

class Education(models.Model):
    school_time = models.CharField(max_length=200)
    school = models.CharField(max_length=200)


    