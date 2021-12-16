from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from location_field.models.plain import PlainLocationField
# Create your models here.
class Contact(models.Model):
    class Meta:
          verbose_name = 'Contact'
          verbose_name_plural = 'Contacts'
    user = models.ForeignKey(get_user_model(),on_delete=models.SET_NULL,related_name='contacts',null=True)
    name = models.CharField(max_length=500,null = True)
    email = models.CharField(max_length=500,null = True)
    phonenumber = models.IntegerField(null=True)
    location = models.CharField(max_length=500,null = True)
    def __str__(self):
          return self.name