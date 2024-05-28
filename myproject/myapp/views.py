from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm, PostModelForm, UserRegistrationForm
from .models import Post

# Create your views here.
def home(request):
    context = {'message': 'Welcome to Django Templates!'}
    return render(request, 'myapp/home.html', context)

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'myapp/post_list.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostModelForm()

    return render(request, 'myapp/create_post.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'myapp/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'myapp/profile.html')