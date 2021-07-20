from django.urls import path
import admins.views as vs

app_name = 'admins'

urlpatterns = [
    path('', vs.index, name='index'),
    path('users/', vs.admin_users, name='admin_users'),
    path('users/create/', vs.admin_users_create, name='admin_users_create'),
    path('users/update/<int:id>/', vs.admin_users_update, name='admin_users_update'),
    path('users/remove/<int:id>/', vs.admin_users_delete, name='admin_users_delete'),

    path('category/', vs.admin_category, name='admin_category'),
    path('category/create/', vs.admin_category_create, name='admin_category_create'),
    path('category/update/<int:id>/', vs.admin_category_update, name='admin_category_update'),
    # path('category/remove/<int:id>/', vs.admin_users_delete, name='admin_users_delete'),
]
