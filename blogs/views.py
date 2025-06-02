from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from blogs.models import Blog, Category

# Create your views here.
def posts_by_category(request, category_id):
    # Fetch posts by category_id
    posts = Blog.objects.filter(status='Published', category = category_id)
    # use try-except to handle the case where category_id does not exist
#    try:
#        category = Category.objects.get(pk=category_id)
#    except:
        # redirect user to home page if category not found
#        return redirect('home')
    category = get_object_or_404(Category, pk=category_id)
    # Render the posts in the template
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request,'posts_by_category.html', context)


def blogs(request, slug):
    return render(request, 'blogs.html')