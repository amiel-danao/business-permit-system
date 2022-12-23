from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

urlpatterns = [
    # path('', LoginView.as_view(
    #     redirect_authenticated_user=True),
    #     name='home'),
    # path('home/', LogoutView.as_view(), name='logout'),
]
