from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth
from django.urls import reverse


# Create your views here.

def login(request):
    if request.method == 'POST':
        if UserLoginForm(data=request.POST).is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))

        context = {
            'title': 'Авторизация',
            'form': UserLoginForm(),
            'error': 'Error'
        }
        return render(request, 'users/login.html', context)

    else:
        context = {
            'title': 'Авторизация',
            'form': UserLoginForm()
        }
        return render(request, 'users/login.html', context)


def registrations(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
        else:
            context = {'title': 'Регистрация',
                       'error': 'Invalid data',
                       'form': UserRegistrationForm()}
            return render(request, 'users/register.html', context)
    else:
        context = {'title': 'Регистрация',
                   'form': UserRegistrationForm()}
        return render(request, 'users/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
