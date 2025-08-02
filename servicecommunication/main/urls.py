from django.urls import path
from . import views

urlpatterns = [
    path('get_all', views.sync_products, name='all'),
    path('get_all/<str:pk>', views.sync_products_id, name='one'),
    path('creat', views.creat_sample_product, name='one'),
]