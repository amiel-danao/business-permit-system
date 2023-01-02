from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from system.views import BusinessPermitListView, BusinessPermitCreateView, BusinessPermitDetailView, reject_application, approve_application, confirm_certificate, confirm_issuance
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'system'

urlpatterns = [
    path('', BusinessPermitListView.as_view(), name='index'),
    # re_path(r'^permit/create/(?:page-(?P<page_number>[0-9]+)/)?$', BusinessPermitCreateView.as_view(), name='create'),
    path('permit/create/', BusinessPermitCreateView.as_view(), name='create'),
    # path('permit/detail/', BusinessPermitDetailView.as_view(), name='detail'),
    path('permit/detail/<int:pk>/', BusinessPermitDetailView.as_view(), name="detail"),
    path('permit/reject/<int:pk>/', reject_application, name="reject"),
    path('permit/approve/<int:pk>/', approve_application, name="approve"),
    path('permit/confirm/<int:pk>/', confirm_certificate, name="confirm-certificate"),
    path('permit/confirm_issuance/<int:pk>/', confirm_issuance, name="confirm-issuance"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
