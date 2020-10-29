from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_lista, name='post_lista'),
    path('publicacion/<int:pk>/', views.post_detalle, name='post_detalle'),
    path('post/nuevo', views.post_nuevo, name='post_nuevo'),
    path('post/<int:pk>/editar/', views.post_editar, name='post_editar'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publicar/', views.post_publicar, name='post_publicar'),
    path('post/<pk>/eliminar/', views.post_eliminar, name='post_eliminar'),
]
