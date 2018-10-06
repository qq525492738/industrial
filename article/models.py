from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone

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
    modify_time = models.DateTimeField(auto_now=True, blank=True)
    category = models.ManyToManyField(Category, verbose_name='分类')
    title = models.CharField(max_length=100, blank=True, verbose_name='标题')
    content = RichTextUploadingField(verbose_name='内容')
    visits = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def viewed(self):
        self.visits += 1
        self.save(update_fields=['visits'])

    def next_article(self):
        return Article.objects.filter(id__gt=self.id).order_by('id').first()

    def previous_article(self):
        return Article.objects.filter(id__lt=self.id).order_by('-id').first()

    def get_absolute_url(self):
        return "/article/%s" % self.id

class Adverticement(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    img = models.ImageField(upload_to='ad_img/upload/'+timezone.now().strftime('%Y/%m/%d'), verbose_name='广告图')
    callback_url = models.URLField(blank=True, null=True)
    public_date = models.DateTimeField(auto_now_add=True, blank=True)
    priority = models.IntegerField(default=0, blank=True)
    expire = models.DateTimeField(null=True, blank=True)