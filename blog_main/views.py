from django.http import HttpResponse ### delete this line
from django.shortcuts import render
from blogs.models import Blog, Category


def home(request):
    categories = Category.objects.all()
    features_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('-updated_at')
    
    posts = Blog.objects.filter(is_featured=False, status='Published')
    
    
    context = {
        'categories': categories,
        'featured_posts': features_posts,
        'posts': posts,
    }
    print(categories)  # Debugging line to check categories
    return render(request, 'home.html', context)
