from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LogView, name='log'),
    path('register/', views.registerPage, name='register'),
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('new/', views.newroom, name= 'newroom'),
    path('update/<str:pk>/', views.updateRoom, name='update'),
    path('delete/<str:pk>/', views.delete, name='delete'),
    path('logout/', views.logoutUser, name='logout')
]
