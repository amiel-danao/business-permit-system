from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from system.views import BusinessPermitListView, BusinessPermitCreateView
from django.urls import re_path

app_name = 'system'

urlpatterns = [
    path('', BusinessPermitListView.as_view(), name='index'),
    # re_path(r'^permit/create/(?:page-(?P<page_number>[0-9]+)/)?$', BusinessPermitCreateView.as_view(), name='create'),
    path('permit/create/', BusinessPermitCreateView.as_view(), name='create')
]
