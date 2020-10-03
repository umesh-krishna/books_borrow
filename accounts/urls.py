from django.contrib import admin
from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('create/', views.UserCreate.as_view(), name='create'),
    path('login/', views.LoginAPI.as_view(), name='login'),
]
