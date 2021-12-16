from django.contrib import admin

# Register your models here.
from .models import Memory, Category, User

admin.site.register(Memory)
admin.site.register(Category)
