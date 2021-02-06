from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='upload'),
    path('upload/', views.upload_file_view, name='upload'),
    path('show_products/', views.products, name='product'),
    path('products/', views.get_product, name='get_products'),
    path('products/<int:id>/', views.get_product, name='product'),
    path('products/<str:title>/<str:description>/<str:image>/', views.get_product, name='post_product'),
] 