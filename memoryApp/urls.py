from django.urls import path

from . import views

urlpatterns = [
    path('', views.memories, name='memories'),
    path('filter/<str:cat>', views.filter, name='filter'),
    path('addCategory', views.addCategory, name='addCategory'),
    path('filter/addMemory/<str:category>', views.addMemory, name='addMemory'),
    path('filter/addMemory/add/<str:category>', views.add, name='add'),
    path('addedCategory', views.addedCategory,name="addedCategory"),
]