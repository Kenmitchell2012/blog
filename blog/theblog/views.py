from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Post, Category, Comment
from .forms import PostForm, EditForm

from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.



# def home(request):
#     return render(request, 'home.html', {})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post', args=[str(pk)]))




# class HomeView(ListView):
#     model = Post

#     template_name = 'home.html'
#     cats = Category.objects.all()

#     def get_context_data(self, *args, **kwargs):
#         cat_menu = Category.objects.all()
#         context = super(HomeView, self).get_context_data(*args, **kwargs)

#         context["cat_menu"] = cat_menu
#         return context
    
#     def get_queryset(self):
#         return Post.objects.all().order_by('-created_at')

from django.views.generic import ListView
from .models import Post, Category

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat_menu"] = Category.objects.all()

        # Adding profile pictures to the context
        profile_pics = {}
        for post in context['post_list']:
            try:
                profile_pics[post.author.id] = post.author.profile_pic.url
            except AttributeError:
                # Profile does not exist for this user
                profile_pics[post.author.id] = None
        context["profile_pics"] = profile_pics

        return context

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')

    
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'category_posts': category_posts, 'cats': cats.replace('-', ' ').title()})

def CategoryListView(request, cats):
    cat_menu_list = Category.objects.all()
    return render(request, 'categories_list.html', {'cat_menu_list': cat_menu_list, 'cats': cats.replace('-', ' ').title()})

# fix like function
class View_Post(DetailView):
    model = Post
    template_name = 'view.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(View_Post, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
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

class AddCommentView(CreateView):
    model = Comment
    # form_class = PostForm
    # template_name = 'add_post.html'

    success_url = reverse_lazy('home')
    fields = 'body'


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

    