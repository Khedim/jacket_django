from django.urls import path
from . import views

urlpatterns = [
    path('latest-products', views.ProductsListAPI.as_view())
]

