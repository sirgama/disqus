from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LogView, name='log'),
    path('register/', views.registerPage, name='register'),
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('user/<str:pk>/', views.userProfie, name='userprofile'),
    path('new/', views.newroom, name= 'newroom'),
    path('update/<str:pk>/', views.updateRoom, name='update'),
    path('delete/<str:pk>/', views.delete, name='delete'),
    path('deletemsg/<str:pk>/', views.deleteMessage, name='delete-txt'),
    path('logout/', views.logoutUser, name='logout')
]
