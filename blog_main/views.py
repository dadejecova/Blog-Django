from django.http import HttpResponse ### delete this line
from django.shortcuts import render
from blogs.models import Category


def home(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    print(categories)  # Debugging line to check categories
    return render(request, 'home.html', context)
