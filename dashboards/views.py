from django.shortcuts import render

from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required

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