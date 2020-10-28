from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_lista, name='post_lista'),
    path('publicacion/<int:pk>/', views.post_detalle, name='post_detalle'),
    path('post/nuevo', views.post_nuevo, name='post_nuevo'),
    path('post/<int:pk>/editar/', views.post_editar, name='post_editar'),
]
