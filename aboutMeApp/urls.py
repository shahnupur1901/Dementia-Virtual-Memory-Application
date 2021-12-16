from django.urls import path, include
from . import views
from django.urls import path

from . import views
urlpatterns = [
    path('',views.aboutMe, name = 'aboutMe'),
    path('editProfile',views.editProfile, name = 'editProfile'),
    path('submit',views.submit, name = 'submit'),
]