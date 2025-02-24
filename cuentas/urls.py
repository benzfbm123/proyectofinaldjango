

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_personalizado, name='login'),
    path('logout/', views.logout_personalizado, name='logout'),
   
]