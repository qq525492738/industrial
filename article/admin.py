from django.contrib import admin
from article.models import Article, Category, Classify
import xadmin
# Register your models here.

xadmin.site.register(Classify)
xadmin.site.register(Category)
xadmin.site.register(Article)


admin.site.register(Classify)
admin.site.register(Category)
admin.site.register(Article)