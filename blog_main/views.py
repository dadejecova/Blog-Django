from django.http import HttpResponse ### delete this line
from django.shortcuts import redirect, render
from assignment.models import About
from blog_main.forms import RegistrationForm
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


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally, you can redirect to a success page or login page
            return redirect('register')  # Redirect to home after registration
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)