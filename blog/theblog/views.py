from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Post
from .forms import PostForm, EditForm

from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.


# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    
    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')


class View_Post(DetailView):
    model = Post
    template_name = 'view.html'

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'

class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    success_messgae = 'Post updated successfully'

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    