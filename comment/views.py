from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View
from blog.models import Blog
from .forms import CommentForm


# Create your views here.
class AddCommet(View):
    def post(self, request, add_comment):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
        return redirect('blogDetail', add_comment)
