from django.shortcuts import render
from .models import Blog, Category, Tag
from django.views.generic.base import View
from pure_pagination import PageNotAnInteger, Paginator


# Create your views here.
class IndexView(View):
    def get(self, request):
        res = dict()
        all_blog = Blog.objects.all().order_by('-ctime')

        # 对博客进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_blog, 1, request=request)
        blogs = p.page(page)
        res['all_blog'] = blogs
        return render(request, 'index.html', res)


class TagView(View):
    def get(self, request):
        all_tag = Tag.objects.all()
        tags_num = Tag.objects.all().count()
        res = dict()
        res['all_tag'] = all_tag
        res['tags_num'] = tags_num
        return render(request, 'blog/tags.html', res)


class CategoryView(View):
    def get(self, request):
        all_category = Category.objects.all()
        category_num = Category.objects.all().count()
        res = dict()
        res['all_category'] = all_category
        res['category_num'] = category_num
        return render(request, 'blog/category.html', res)
