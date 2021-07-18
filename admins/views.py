from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm, CategoryAdminForm
from users.models import User
from products.models import ProductCategory
from django.contrib.auth.decorators import user_passes_test


# Create your views here.
@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'Админ-панель'}
    return render(request, 'admins/index.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users(request):
    context = {'title': 'Пользователи',
               'users': User.objects.all()}
    return render(request, 'admins/admin-users-read.html', context=context)


@user_passes_test(lambda u: u.is_staff)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegistrationForm()
    context = {'title': 'Админ-панель - регистрация',
               'form': form}
    return render(request, 'admins/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_staff)
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


@user_passes_test(lambda u: u.is_staff)
def admin_users_delete(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))


@user_passes_test(lambda u: u.is_staff)
def admin_category(request):
    context = {'title': 'Категории',
               'categories': ProductCategory.objects.all()}
    return render(request, 'admins/admin-category-read.html', context=context)


@user_passes_test(lambda u: u.is_staff)
def admin_category_create(request):
    if request.method == 'POST':
        form = CategoryAdminForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_category'))
    else:
        form = CategoryAdminForm()
    context = {'title': 'Админ-панель - создание категории',
               'form': form}
    return render(request, 'admins/admin-category-create.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_category_update(request, id):
    selected_category = ProductCategory.objects.get(id=id)
    if request.method == 'POST':
        form = CategoryAdminForm(instance=selected_category, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_category'))
    else:
        form = CategoryAdminForm(instance=selected_category)
    context = {'title': 'Админ-панель - редактирование категории',
               'form': form,
               'selected_category': selected_category}
    return render(request, 'admins/admin-category-update-delete.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users_delete(request, id):
    category = ProductCategory.objects.get(id=id)
    category.delete()
    return HttpResponseRedirect(reverse('admins:admin_category'))
