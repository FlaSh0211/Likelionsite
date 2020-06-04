from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static# 2 미디어 static 사용
urlpatterns = [
    path('', views.album, name= "album"),
] 
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
