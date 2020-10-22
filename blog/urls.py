from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_lista, name='post_lista'),
    path('publicacion/<int:pk>/', views.post_detalle, name='post_detalle'),
]
