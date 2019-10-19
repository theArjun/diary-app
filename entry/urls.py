from django.urls import path
from . import views

urlpatterns = [
    path('', views.entry, name='entry'),
    path('show', views.show, name='show'),
]