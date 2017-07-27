from django.shortcuts import render, redirect
from .models import Post
from datetime import datetime

# Create your views here.
def index(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'posts/index.html', context)

def post(request):
    Post.objects.create(content = request.POST['content'], created_at = datetime.now(), updated_at = datetime.now())
    return redirect('/')

def delete(request, number):
    post = Post.objects.get(id=number)
    post.delete()
    return redirect('/')
