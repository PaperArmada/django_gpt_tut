from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post

class PostForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data['title']
        if "bad" in title.lower():
            raise forms.ValidationError("Title contains inappropriate content.")
        return title
    
class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if "bad" in title.lower():
            raise forms.ValidationError("Title contains inappropriate content.")
        return title
    
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if title and content:
            if "bad" in title.lower() and "bad" in content.lower():
                raise forms.ValidationError("Title and content cannot both contain inappropriate content.")
        return cleaned_data
    
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']