from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.
class Category(models.Model):
     class Meta:
          verbose_name = 'Category'
          verbose_name_plural = 'Categories'
     user = models.ForeignKey(get_user_model(),on_delete=models.SET_NULL,related_name='categories',null=True)
     categoryName = models.CharField(max_length=500,null = True)
     def __str__(self):
          return self.categoryName 

class Memory(models.Model):
     class Meta:
          verbose_name = 'Memory'
          verbose_name_plural = 'Memories'
     title = models.CharField(max_length = 100,null = True)
     description = models.TextField(null=True)
     location = models.CharField(max_length=100,null = True)
     datePublished = models.DateTimeField('date published',null = True)
     dateOfOccurence = models.DateField('date of occurence',null = True)
     image = models.ImageField(null = True)
     category = models.ForeignKey(Category,on_delete = models.SET_NULL, null=True)
     def __str__(self):
          return self.title
          


