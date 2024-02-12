from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Post

# Create your views here.


# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class View_Post(DetailView):
    model = Post
    template_name = 'view.html'

class AddPost(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'

class UpdatePost(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'title_tag', 'body']