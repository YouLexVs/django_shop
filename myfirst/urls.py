from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list),
    path('home/', views.home),
    path('new/', views.post_create),
    path('<int:id>/', views.post_detail),
    path('<int:id>/edit/', views.post_edit),
    path('<int:id>/delete/', views.post_delete),
]