from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from . forms import SignUpForm, EditProfileForm, PasswordChangingForm
from django.views.generic import DetailView
from theblog.models import Profile, Post

# Create your views here.

# class ShowProfilePageView(DetailView):
#     model = Profile
#     template_name = 'registration/user_profile.html'

#     def get_context_data(self, *args, **kwargs):
#         # users = Profile.objects.all()
#         context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

#         page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

#         # get all posts of the user
#         posts = Post.objects.filter(author=page_user)


#         context["page_user"] = page_user
#         # context["users"] = users
#         context["posts"] = posts
#         return context



class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

        # Retrieve the profile based on the provided primary key
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])

        # Pass the user's profile to the context
        context["page_user"] = profile.user

        # Filter posts authored by the user
        posts = Post.objects.filter(author=profile.user)

        # Pass the user's posts to the context
        context["posts"] = posts
        return context



class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name ='registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name ='registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
    
class PasswordsChangeView(PasswordChangeView):
    # form_class = UserChangeForm
    form_class = PasswordChangingForm
    # success_url = reverse_lazy('home')
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request,'registration/password_success.html', {}) 