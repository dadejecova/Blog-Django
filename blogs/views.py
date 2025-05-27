from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import Blog, Category

# Create your views here.
def posts_by_category(request, category_id):
    # Fetch posts by category_id
    posts = Blog.objects.filter(status='Published', category = category_id)
    context = {
        'posts': posts,
    }
    return render(request,'posts_by_category.html', context)