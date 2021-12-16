from django.urls import path, include
from . import views
from django.urls import path

from . import views
urlpatterns = [
    path('',views.index, name = 'index'),
    path('contacts',views.contacts, name='contacts'),
    path('send_msg',views.send_msg, name = 'send_msg'),
    path('send',views.send, name = 'send'),
    path('joke',views.joke, name = 'joke'),
    path('del/<str:name>',views.delContact, name = 'delContact'),
     path('submitContact',views.submitContact, name='submitContact'),
]