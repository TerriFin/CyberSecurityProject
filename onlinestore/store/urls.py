from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('',     views.rediredToIndex, name='redirect'),
    path('<int:page>/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('manager/', views.manager, name='manager'),
    path('upload/', views.uploadItem, name='upload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
