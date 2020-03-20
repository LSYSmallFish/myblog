from django.contrib import admin
from .models import Blog, Category, Tag

# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'click_num', 'mtime', 'ctime']


admin.site.register(Blog, BlogAdmin)
