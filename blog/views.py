from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
import requests
from django.views.generic import View

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
     if request.method == "POST":
         form = PostForm(request.POST)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             return redirect('post_detail', pk=post.pk)
     else:
         form = PostForm()
     return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
     post = get_object_or_404(Post, pk=pk)
     if request.method == "POST":
         form = PostForm(request.POST, instance=post)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
             post.published_date = timezone.now()
             post.save()
             return redirect('post_detail', pk=post.pk)
     else:
         form = PostForm(instance=post)
     return render(request, 'blog/post_edit.html', {'form': form})     

class Emprestimo(View):

    def get(self, request):
        
        if 'copia' in request.META['QUERY_STRING']:
            g_copia = request.GET['copia']
        else:
            g_copia = ''

        if 'usuario' in request.META['QUERY_STRING']:
            g_usuario = request.GET['usuario'] 
        else:    
            g_usuario = ''

        response = requests.get('http://suabi-api3.herokuapp.com/copia/?search=' + g_copia)
        copia = response.json()
        response = requests.get('http://suabi-api3.herokuapp.com/usuario/?search=' + g_usuario)
        usuario = response.json()
        return render(request, 'blog/emprestimo.html', {
            'copia': copia, 'usuario': usuario,
            'g_copia': g_copia,
            'g_usuario': g_usuario
        })

    def post(self, request):
        response = requests.post('http://suabi-api3.herokuapp.com/emprestimo/')
        emprestimo = response.json()
        return render(request, 'blog/emprestimo.html', {
            'emprestimo': emprestimo
        })   