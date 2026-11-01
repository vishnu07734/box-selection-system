from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("products/", views.product_list, name="product_list"),
    path("products/<int:pk>/delete/", views.product_delete, name="product_delete"),
    path("boxes/", views.box_list, name="box_list"),
    path("boxes/<int:pk>/delete/", views.box_delete, name="box_delete"),
    path("orders/new/", views.order_create, name="order_create"),
    path("orders/<int:pk>/", views.order_detail, name="order_detail"),
]
