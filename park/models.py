from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django.utils.dateparse import parse_time


class ParkClassify(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, blank=True)
    name = models.CharField(max_length=20, verbose_name='园区地区')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '园区地区'
        verbose_name_plural = verbose_name


class ParkCategory(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, blank=True)
    name = models.CharField(max_length=20, verbose_name='分类')
    classify = models.ForeignKey(ParkClassify, on_delete=models.CASCADE, verbose_name='地区')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '园区分类'
        verbose_name_plural = verbose_name


class Park(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, blank=True)
    modify_time = models.DateTimeField(auto_now_add=True, blank=True)
    category = models.ForeignKey(ParkCategory, verbose_name='分类', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, verbose_name='名字')
    title = models.CharField(max_length=100, blank=True, verbose_name='标题')
    logo = models.ImageField(upload_to='parklogo/upload/'+timezone.now().strftime('%Y/%m/%d'), verbose_name='logo')
    introduction = RichTextUploadingField(verbose_name='介绍')
    email = models.EmailField(null=True, blank=True, verbose_name='邮箱')
    # region = models.CharField(max_length=255, null=True, blank=True, verbose_name='所属区')
    area = models.IntegerField(null=True, blank=True, verbose_name='面积')
    region = models.CharField(max_length=255, null=True, blank=True, verbose_name='地区')
    zip_code = models.IntegerField(null=True, blank=True, verbose_name='邮编')
    fax = models.CharField(max_length=13, null=True, blank=True, verbose_name='传真')
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='电话号码')
    web_url = models.CharField(max_length=255,null=True, blank=True, verbose_name='官网')
    addr = models.CharField(max_length=255, blank=True, verbose_name='详细地址')
    favorable = models.CharField(max_length=255, blank=True, verbose_name='优惠政策')
    priority = models.SmallIntegerField(null=True, default=0, blank=True, verbose_name='优先级')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '园区'
        verbose_name_plural = verbose_name


class ParkPlan(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    title = models.CharField(max_length=20,null=True,blank=True)
    park = models.ForeignKey(Park, on_delete=models.CASCADE, blank=True, verbose_name='所属园区')
    picture = models.ImageField(verbose_name='图片',upload_to='parkplan/upload/'+timezone.now().strftime('%Y/%m/%d'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '园区展示图片'
        verbose_name_plural = verbose_name

class Investment(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    name = models.CharField(max_length=255, verbose_name='招商名')
    master = models.CharField(max_length=255, verbose_name='主办方')
    introduction = models.CharField(max_length=255, verbose_name='简介')
    content = RichTextUploadingField(verbose_name='内容')
    addr = models.CharField(max_length=255, blank=True, verbose_name='详细地址')
    park = models.ForeignKey(Park, on_delete=models.CASCADE, verbose_name='园区')
    industry = models.CharField(max_length=255, verbose_name='行业')
    logo = models.ImageField(upload_to='investmentlogo/upload/' + timezone.now().strftime('%Y/%m/%d'), verbose_name='logo')
    area = models.IntegerField(null=True, blank=True, verbose_name='面积')
    email = models.EmailField(null=True, blank=True, verbose_name='邮箱')
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='电话号码')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '招商项目'
        verbose_name_plural = verbose_name


class Factory(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, blank=True)
    modify_time = models.DateTimeField(auto_now_add=True, blank=True)
    park = models.ForeignKey(Park, on_delete=models.CASCADE, verbose_name='所属园区')
    name = models.CharField(max_length=100, blank=True, verbose_name='名字')
    logo = models.ImageField(upload_to='factorylogo/upload/'+timezone.now().strftime('%Y/%m/%d'), verbose_name='logo')
    intention = models.CharField(max_length=100, null=True, blank=True, verbose_name='意向')
    category = models.CharField(max_length=100, null=True, blank=True, verbose_name='类型')
    email = models.EmailField(null=True, blank=True, verbose_name='邮箱')
    region = models.CharField(max_length=255, null=True, blank=True, verbose_name='地区')
    addr = models.CharField(max_length=255, blank=True, verbose_name='详细地址')
    area = models.IntegerField(null=True,blank=True,verbose_name='面积')
    fax = models.CharField(max_length=13, blank=True, verbose_name='传真')
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='电话')
    web_url = models.CharField(max_length=255, blank=True, verbose_name='官网')
    introduction = RichTextUploadingField(verbose_name='介绍')
    price = models.IntegerField(verbose_name='单价',null=True,blank=True)
    unit_value = models.IntegerField(verbose_name='单位值',null=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '厂房'
        verbose_name_plural = verbose_name

class FactoryPlan(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    title = models.CharField(max_length=20,null=True,blank=True)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, blank=True, verbose_name='所属厂房')
    picture = models.ImageField(verbose_name='图片',upload_to='parkplan/upload/'+timezone.now().strftime('%Y/%m/%d'))
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '厂房展示图片'
        verbose_name_plural = verbose_name

2
class FactoryRelease(models.Model):
    id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField(auto_now_add=True, blank=True)
    modify_time = models.DateTimeField(auto_now=True, blank=True)

    title = models.CharField(max_length=100, blank=True, verbose_name='标题')
    content = models.TextField(blank=True, verbose_name="内容")
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, verbose_name='厂房')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '厂房动态'
        verbose_name_plural = verbose_name
