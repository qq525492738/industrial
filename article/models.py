from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Classify(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, blank=True)
    name = models.CharField(max_length=20, verbose_name='分类名')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '总分类'
        verbose_name_plural = verbose_name


class Category(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, blank=True)
    name = models.CharField(max_length=20, verbose_name='分类名')

    classify = models.ForeignKey(Classify, on_delete=models.CASCADE, verbose_name='总分类')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name


class Article(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, blank=True)
    modify_time = models.DateTimeField(auto_now_add=True, blank=True)
    category = models.ManyToManyField(Category, verbose_name='分类')
    title = models.CharField(max_length=100, blank=True, verbose_name='标题')
    content = RichTextUploadingField(verbose_name='内容')
    visits = models.IntegerField(blank=True, default=0)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

