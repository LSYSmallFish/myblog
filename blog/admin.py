from django.contrib import admin
from .models import Blog, Category, Tag


# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'click_num', 'mtime', 'ctime']

    def save_model(self, request, obj, form, change):
        obj.save()
        obj_category = obj.category
        category_num = obj_category.blog_set.count()
        obj_category.number = category_num
        print(category_num)
        obj_category.save()

        obj_tags = obj.tag.all()
        for tag in obj_tags:
            tag_num = tag.tag.count()
            tag.number = tag_num
            print(tag_num)
            tag.save()

    def delete_model(self, request, obj):
        obj_category = obj.category
        category_num = obj_category.blog_set.count()
        obj_category.number = category_num - 1
        print(123)
        obj_category.save()

        obj_tags = obj.tag.all()
        for tag in obj_tags:
            tag_num = tag.tag.count()
            tag.number = tag_num - 1
            tag.save()
        obj.delete()


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'number']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'number']


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
