from django.shortcuts import render

def post_lista(request):
    return render(request, 'blog/post_lista.html', {})
