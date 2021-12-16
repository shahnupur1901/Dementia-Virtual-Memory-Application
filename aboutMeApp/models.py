from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model
class PatientUser(models.Model):
    class Meta:
          verbose_name = 'Patient'
          verbose_name_plural = 'Patient'
    user = models.ForeignKey(get_user_model(),on_delete=models.SET_NULL,related_name='patients',null=True)
    name = models.CharField(max_length=500,null = True)
    profilePicture = models.ImageField(null = True)
    birthdate = models.DateField(null=True)
    description = models.TextField(null=True)
    def __str__(self):
          return self.name