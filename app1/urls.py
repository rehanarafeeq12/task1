from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login_view', views.login_view, name='login_view'),
    path('home/', views.home, name='home'),
]
