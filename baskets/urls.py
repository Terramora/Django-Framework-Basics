from django.urls import path
from baskets.views import basket_add, basket_remove

app_name = 'baskets'

urlpatterns = [
    path('add/<int:product_id>/', basket_add, name='basket_add'),
    path('delete/<int:id>/', basket_remove, name='basket_remove')
]
