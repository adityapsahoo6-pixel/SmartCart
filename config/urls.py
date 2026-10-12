"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store.views import home, products, product_detail, add_to_cart, cart, remove_from_cart, update_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('products/<int:id>/', product_detail, name='product_detail'),
    path('cart/add/<int:id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
    path('cart/remove/<int:id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:id>/<str:action>/', update_cart, name='update_cart'),
]