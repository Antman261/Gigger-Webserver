from django.contrib import admin
from .models import Author, BlogPost

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url_slug": ("title",)}

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Author)
