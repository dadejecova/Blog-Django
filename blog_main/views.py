from django.http import HttpResponse ### delete this line
from django.shortcuts import render
from assignment.models import About
from blogs.models import Blog, Category


def home(request):
    
    features_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('-updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')
    
    # Fetch about us
    try:
        about = About.objects.get()
    except:
        about = None
    # Fetch all categories
    context = {

        'featured_posts': features_posts,
        'posts': posts,
        'about': about,
    }

    return render(request, 'home.html', context)
