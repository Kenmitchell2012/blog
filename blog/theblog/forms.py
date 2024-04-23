from django import forms
from .models import Post, Category, Comment


choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for i in choices:
    choice_list.append(i)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'header_image', 'title_tag', 'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'header_image': forms.FileInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'author', 'type': 'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag','header_image','body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'header_image': forms.FileInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }

# add post from profile page postform
class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)
        
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }
