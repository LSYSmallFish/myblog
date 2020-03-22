"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import IndexView, TagView,CategoryView,TagDetailView,CategoryDetailView,BlogDetailView
from comment.views import AddCommet
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('tags/', TagView.as_view(), name='tags'),
    path('category/', CategoryView.as_view(), name='category'),
    path('tags/<tagDetail>', TagDetailView.as_view(), name='tagDetail'),
    path('category/<categoryDetail>', CategoryDetailView.as_view(), name='categoryDetail'),
    path('blog/<blogDetail>', BlogDetailView.as_view(), name='blogDetail'),
    path('add_comment/<add_comment>', AddCommet.as_view(), name='add_comment'),
]
