from django.db import models
from django.dispatch import receiver
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    """
    文章的分类
    """
    name = models.CharField(verbose_name='文章类别', max_length=20)
    number=models.IntegerField(verbose_name='类别数量',default=0)
    class Meta:
        verbose_name = '文章类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    文章标签
    """
    name = models.CharField(verbose_name='文章标签', max_length=20)
    number = models.IntegerField(verbose_name='标签数量', default=0)
    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Blog(models.Model):
    """
    博客
    """
    title = models.CharField(verbose_name='博客标题', max_length=128)
    content = models.TextField(verbose_name='博客正文', default='')
    click_num = models.IntegerField(verbose_name='点击率', default=0)
    ctime = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    mtime = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name='标签', related_name='tag')

    class Meta:
        verbose_name = '我的博客'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
