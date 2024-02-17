from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Post, Category
from .forms import PostForm, EditForm

from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.



# def home(request):
#     return render(request, 'home.html', {})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post', args=[str(pk)]))




class HomeView(ListView):
    model = Post

    template_name = 'home.html'
    cats = Category.objects.all()

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
    
    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')
    
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'category_posts': category_posts, 'cats': cats.replace('-', ' ').title()})

def CategoryListView(request, cats):
    cat_menu_list = Category.objects.all()
    return render(request, 'categories_list.html', {'cat_menu_list': cat_menu_list})

# fix like function
class View_Post(DetailView):
    model = Post
    template_name = 'view.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(View_Post, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

    # def get_context_data(self, *args, **kwargs):
    #     stuff = get_object_or_404(Post, id=self.kwargs['pk'])
    #     total_likes = stuff.total_likes()
    #     context["total_likes"] = total_likes
    #     return context


class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('home')
    # fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPost, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    success_messgae = 'Post updated successfully'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UpdatePost, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DeletePost, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

    