from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from admins.forms import UserAdminRegistratinonForm, UserAdminProfileForm
from users.models import User


# Create your views here.

def index(request):
    context = {'title': 'Админ-панель'}
    return render(request, 'admins/index.html', context)


def admin_users(request):
    context = {'title': 'Пользователи',
               'users': User.objects.all()}
    return render(request, 'admins/admin-users-read.html', context=context)


def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistratinonForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegistratinonForm()
    context = {'title': 'Админ-панель - регистрация',
               'form': form}
    return render(request, 'admins/admin-users-create.html', context)


def admin_users_update(request, id):
    selected_user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=selected_user)
    context = {'title': 'Админ-панель - редактирование пользователя',
               'form': form,
               'selected_user': selected_user}
    return render(request, 'admins/admin-users-update-delete.html', context)


def admin_users_delete(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))
