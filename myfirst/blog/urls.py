from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list),
    path('home/', views.home),
    path('new/', views.post_create),
    path('<int:id>/', views.post_detail),
    # path('<int:id>/edit/', views.post_edit),
    # path('<int:id>/delete/', views.post_delete),
    path('products/', views.product_list, name='product_list'),
    path('cart/', views.cart_view, name='cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart')
]