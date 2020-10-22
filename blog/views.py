from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_lista(request):
    publicaciones = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_lista.html', {'publicaciones': publicaciones})

def post_detalle(request, pk):
    publicaciones = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detalle.html', {'publicaciones': publicaciones})
