from django.urls import path
from . import views

urlpatterns = [
    path('', views.entry, name='entry'),
    path('show', views.show, name='show'),
    path('show/<int:diary_id>', views.detail, name='detail'),
    path('productivity/', views.productivity, name='productivity'),
]