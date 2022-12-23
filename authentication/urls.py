from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

urlpatterns = [
    path('login/', LoginView.as_view(
        # template_name='auth/login.html',
        redirect_authenticated_user=True),
        name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
