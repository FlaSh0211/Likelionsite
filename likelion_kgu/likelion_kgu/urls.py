from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static# 2 미디어 static 사용
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('festival/', include('festival.urls')),
    path('album/', include('album.urls')),
    path('board/', include('board.urls')),
    path('', include('likelion.urls')),
    
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
