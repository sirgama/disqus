from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('new/', views.newroom, name= 'newroom'),
    path('update/<str:pk>/', views.updateRoom, name='update')
]
