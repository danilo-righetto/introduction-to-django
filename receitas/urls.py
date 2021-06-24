from django.urls import path

# importe todas as views desse app
from . import views

urlpatterns = [
    path('', views.index, name='index')
]
