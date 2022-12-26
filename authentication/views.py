from django.shortcuts import render, redirect
from authentication.forms import RegisterForm
from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpResponseRedirect


def register_view(request):
    form = RegisterForm(request.POST)
    if request.method == "POST":        
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('system:index')
        else:
            password1 = form.data['password1']
            password2 = form.data['password2']
            email = form.data['email']
            for msg in form.errors.as_data():
                if msg == 'email':
                    messages.error(request, f"Declared {email} is not valid or is already taken")
                if msg == 'password2' and password1 == password2:
                    messages.error(request, f"Selected password: {password1} is not strong enough")
                elif msg == 'password2' and password1 != password2:
                    messages.error(request, f"Password: '{password1}' and Confirmation Password: '{password2}' do not match")        
    form = RegisterForm()
    return render(request=request, template_name="registration/register.html", context={"form": form})