from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from . models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.contrib import messages

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required


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
    context_object_name = 'post'

    def get_context_data(self, *args, **kwargs):
        context = super(View_Post, self).get_context_data(*args, **kwargs)
        cat_menu = Category.objects.all()
        post = context['post']  # since this is a DetailView, 'post' is already included in context
        comments = post.comments.order_by('-date_added')

        comments = post.comments.all()

        total_likes = post.total_likes()
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Include the comment form in the context
        comment_form = CommentForm()
        context.update({
            'cat_menu': cat_menu,
            'total_likes': total_likes,
            'liked': liked,
            'comments': comments,
            'comment_form': comment_form
        })
        return context

    def post(self, request, *args, **kwargs):
        # This method handles the submission of the comment form
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            self.object = self.get_object()  # Get the post object
            new_comment = comment_form.save(commit=False)
            new_comment.post = self.object
            new_comment.author = request.user
            new_comment.save()
            return redirect('post', self.kwargs['pk'])
        return self.get(request, *args, **kwargs)  # handle failed form validation




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
    

def new_post_from_profile(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user  # Set the author to the current user
            new_post.save()
            return redirect('profile_page_url_name')  # Redirect back to the profile page
    else:
        form = PostForm()
    # If GET request or form is not valid, you might redirect or show the form again
    return redirect('profile_page_url_name')

class AddCommentView(CreateView):
    model = Comment
    # form_class = PostForm
    # template_name = 'add_post.html'

    success_url = reverse_lazy('home')
    fields = 'body'


@login_required
def DeleteCommentView(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    
    # Check if the request user is the owner of the comment or an admin
    if request.user == comment.author or request.user.is_superuser:
        comment.delete()
        # Redirect to the same page where the request came from
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('home')))
    else:
        # Optionally, return an error message or an HTTP forbidden response
        return HttpResponseRedirect(reverse('error_view_name'))





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

    
# add friend
