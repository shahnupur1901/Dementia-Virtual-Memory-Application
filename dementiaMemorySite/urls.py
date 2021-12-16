from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('memory/', include("memoryApp.urls")),
    path('aboutMe/', include("aboutMeApp.urls")),
    path('',include("accounts.urls")),
    path('emergency/',include("emergencyApp.urls")),
     path('ToDoApp/',include("ToDoApp.urls"))
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
