from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.board, name='board'),
    path('<int:pk>/', views.board_view, name='board_view'),
    path('new/', views.board_create, name='board_create'),
    path('update/<int:pk>/', views.board_update, name='board_update'),
    path('delete/<int:pk>/', views.board_delete, name='board_delete'),
    path('search/', views.board_search, name='board_search'),
    path('check/', views.check_password, name='check_password'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
