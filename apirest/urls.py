from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='upload'),
    path('upload/', views.upload_file_view, name='upload'),
    path('products/', views.products, name='product'),
    path('products/get/', views.get_products, name='get_products'),
    path('products/get/<int:id>/', views.get_product, name='get_product'),
    path('products/get/<str:title>/<str:description>/<str:image>/', views.get_product, name='get_product'),
    path('products/del/<int:id>/', views.del_product, name='del_product'),
]