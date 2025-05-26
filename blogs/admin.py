from django.contrib import admin
from .models import Category, Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)} # Automatically generate slug from title
    list_display = ('title', 'category', 'author', 'status', 'is_featured', 'created_at')
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable = ('is_featured', 'status')
 
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
