from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    food_type = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Menu(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Item(models.Model):
    menu = models.ForeignKey(Menu)
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Ingrediant(models.Model):
    item = models.ForeignKey(Item)
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):              # __unicode__ on Python 2
        return self.name
