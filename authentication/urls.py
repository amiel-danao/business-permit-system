from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from authentication.views import register_view
from authentication.forms import LoginForm

app_name = 'authentication'

urlpatterns = [
    path('authentication/login/', LoginView.as_view(redirect_authenticated_user=True, authentication_form=LoginForm),
        name='login'),
    path('authentication/logout/', LogoutView.as_view(), name='logout'),
    path('authentication/register/', register_view, name='register'),
]
