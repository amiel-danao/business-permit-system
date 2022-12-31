from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from system.views import BusinessPermitListView, BusinessPermitCreateView, BusinessPermitDetailView
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
    # path('permit_download/<int:pk>/', DownloadView.as_view(), name='permit-download')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
