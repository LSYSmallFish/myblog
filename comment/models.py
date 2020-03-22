from django.db import models
from blog.models import Blog
from ckeditor.fields import RichTextField


# Create your models here.
class Comment(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=20, default='佚名')
    content = RichTextField()
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    blog = models.ForeignKey(Blog, verbose_name='博客', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content[:10]
