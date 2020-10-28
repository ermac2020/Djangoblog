from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.shortcuts import redirect
from .forms import PostForm

def post_lista(request):
    publicaciones = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_lista.html', {'publicaciones': publicaciones})

def post_detalle(request, pk):
    publicaciones = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detalle.html', {'publicaciones': publicaciones})

def post_nuevo(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detalle', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_editar.html', {'form': form})

def post_editar(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detalle', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_editar.html', {'form': form})
