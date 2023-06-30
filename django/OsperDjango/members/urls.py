from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),#127.0.0.1:8000/members/
    path('osper', views.test, name='test'),
]

