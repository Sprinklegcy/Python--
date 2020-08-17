#  @data   2020/3/21 12:49

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.my_get),
    path('', views.my_post),
    path('help/', views.app_help),
    path('download/', views.downloads),
    # path('admin/', admin.site.urls),
]
