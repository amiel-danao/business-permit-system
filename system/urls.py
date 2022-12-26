from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from system.views import index

app_name = 'system'

urlpatterns = [
    path('', index, name='index')
]
