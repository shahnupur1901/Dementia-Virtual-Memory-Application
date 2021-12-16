from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
class Note(models.Model):
    class Meta:
          verbose_name = 'Note'
          verbose_name_plural = 'Note'
    uid = models.AutoField(primary_key=True)
    user = models.ForeignKey(get_user_model(),on_delete=models.SET_NULL,related_name='notes',null=True)
    description = models.TextField(null=True)
    def __str__(self):
          return self.description