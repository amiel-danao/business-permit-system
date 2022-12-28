from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from system.views import BusinessPermitListView, BusinessPermitCreateView

app_name = 'system'

urlpatterns = [
    path('', BusinessPermitListView.as_view(), name='index'),
    path('permit/create/', BusinessPermitCreateView.as_view(), name='create')
]
