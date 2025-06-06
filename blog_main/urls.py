
from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from blogs import views as Blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('category/', include('blogs.urls')),
    # search endpoint
    path('blogs/search/', Blog_views.search, name='search'),
    path('blogs/<slug:slug>/', Blog_views.blogs, name='blogs'),
    
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


