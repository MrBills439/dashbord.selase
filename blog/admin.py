from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'is_published', 'created_date', 'updated_date']
    list_filter = ['is_published', 'created_date', 'author']
    search_fields = ['title', 'content', 'author__username']
    list_per_page = 20
    list_editable = ['is_published']
    
    def save_model(self, request, obj, form, change):
        if not change:  # Only set author when creating new post
            obj.author = request.user
        super().save_model(request, obj, form, change)
