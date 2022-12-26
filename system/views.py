from django.shortcuts import render
from django.contrib.auth.decorators import login_required as login_required

# Create your views here.

@login_required
def index(request):
    return render(request, template_name='system/home.html')