#   Django
from django.shortcuts import render

#   Models
from blog.models import Post, Category

# Create your views here.

def posts_view(request):
    posts = Post.objects.all()
    return render(request, "blog.html", {"posts":posts})

def category_view(request, category_id):
    all_categories = Post.objects.all()
    category = Category.objects.get(id=category_id)
    posts = Post.objects.filter(category = category)
    return render(request, "category.html", {"posts":posts, "all_categories":all_categories})