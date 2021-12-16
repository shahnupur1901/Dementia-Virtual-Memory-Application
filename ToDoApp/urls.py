from django.urls import path, include
from . import views
from django.urls import path

from . import views
urlpatterns = [
    path("addnote", views.addnote,name="addnote"),
    path("delnote/<str:uid>", views.delnote,name="delnote"),
    path("", views.toDoApp,name="ToDoApp")
]