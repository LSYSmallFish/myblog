from django.shortcuts import render, get_object_or_404
from .models import Blog, Category, Tag
from django.views.generic.base import View
from pure_pagination import PageNotAnInteger, Paginator
import markdown
from comment.forms import CommentForm
from comment.models import Comment


# Create your views here.
class IndexView(View):
    def get(self, request):
        res = dict()
        all_blog = Blog.objects.all().order_by('ctime')

        # 对博客进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_blog, 1, request=request)
        blogs = p.page(page)
        for blog in all_blog:
            blog.content = markdown.markdown(blog.content)
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


class TagDetailView(View):
    def get(self, request, tagDetail):
        res = dict()
        tag = get_object_or_404(Tag, name=tagDetail)
        tag_blogs = tag.tag.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(tag_blogs, 1, request=request)
        tag_blogs = p.page(page)
        res['tag_blogs'] = tag_blogs
        res['tag_name'] = tagDetail
        return render(request, 'blog/tagDetail.html', res)


class CategoryDetailView(View):
    def get(self, request, categoryDetail):
        res = dict()
        category = get_object_or_404(Category, name=categoryDetail)
        category_blogs = category.blog_set.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(category_blogs, 1, request=request)
        category_blogs = p.page(page)
        res['category_blogs'] = category_blogs
        res['category_name'] = categoryDetail
        return render(request, 'blog/categoryDetail.html', res)


class BlogDetailView(View):
    def get(self, request, blogDetail):
        res = dict()
        blog = Blog.objects.get(pk=blogDetail)
        res['blog'] = blog
        blog_list = Blog.objects.all().order_by('ctime')
        all_comment = Comment.objects.filter(blog_id=blog.id)
        comment_form=CommentForm()
        comment_nums = all_comment.count()
        pos = 0
        has_next = False
        has_prev = False
        blog_prev = None
        blog_next = None
        for i in blog_list:
            if i.id == int(blogDetail):
                has_next = True
                has_prev = True
                break
            pos += 1
        if pos == 0:
            has_prev = False
        if pos == len(blog_list) - 1:
            has_next = False
        if has_prev:
            blog_prev = blog_list[pos - 1]
        if has_next:
            blog_next = blog_list[pos + 1]
        blog.click_num += 1
        blog.save()
        blog.content = markdown.markdown(blog.content)

        res['has_next'] = has_next
        res['has_prev'] = has_prev
        res['blog_prev'] = blog_prev
        res['blog_next'] = blog_next
        res['all_comment'] = all_comment
        res['comment_nums']=comment_nums
        res['comment_form']=comment_form
        return render(request, 'blog/blogDetail.html', res)
