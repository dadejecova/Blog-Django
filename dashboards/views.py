from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required

from dashboards.forms import BlogPostForm, CategoryForm

@login_required(login_url='login')
# Create your views here.
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    context = {
        'category_count': category_count,
        'blogs_count': blogs_count,
    }
    return render(request, 'dashboard/dashboard.html', context)

def categories(request):
    return render(request, 'dashboard/categories.html')


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')

    form = CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_category.html', context)

def edit_category(request, pk):
    # Fetch the category by primary key
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance = category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance = category)
    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'dashboard/edit_category.html', context)

def delete_category(request, pk):
    # Fetch the database object by primary key
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')

def posts(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'dashboard/posts.html', context)

def add_post(request):
    form = BlogPostForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_post.html', context)
# This view handles the dashboard, categories, and posts management.