from django.urls import path

from users.views import login, registrations, logout

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registrations/', registrations, name='registrations'),
    path('logout/', logout, name='logout')
]
