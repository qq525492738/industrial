from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from . import models


# class SearchView(generic.View):
#     def extra_context(self):  # 重载extra_context来添加额外的context内容
#         context = super(SearchView, self).extra_context()
#         side_list = models.Article.objects.filter(kind='major').order_by('create_time')[:8]
#         context['side_list'] = side_list
#         return context


class IndexView(generic.ListView):
    template_name = 'article/news.html'
    context_object_name = 'articles'

    # return models.Article.objects.all()
    def get_queryset(self):
        self.category_name = self.request.GET.get('category_name', False)
        if self.category_name:
            return models.Article.objects.filter(category__name=self.category_name)
                # {'information':models.Article.objects.filter(category__name="资讯中心"),
                #     'regulation':models.Article.objects.filter(category__name="政策法规")
                #     }.get(self.category_name, [])

        return models.Article.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hot_information_list'] = models.Article.objects.filter(category__name="资讯中心").order_by('visits')[:5]
        context['related_list'] = models.Article.objects.filter(category__name="专题")[:5]
        context['about_list'] = models.Article.objects.filter(category__name="关于协会")[:5]
        if self.category_name:
            context['articles_category'] = models.Category.objects.filter(name=self.category_name)
            context['articles_category_name']=self.category_name

        return context


class ArticleListView(generic.ListView):
    template_name = 'article/news.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return models.Article.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hot_information_list'] = models.Article.objects.filter(category__name="热门资讯")[:5]
        context['related_list'] = models.Article.objects.filter(category__name="专题")[:5]
        context['about_list'] = models.Article.objects.filter(category__name="关于协会")[:5]
        return context
    # def get_queryset(self):
    #     category = self.request.GET.get('category',None)
    #     if category:
    #         if category == 'information':
    #             models.Article.objects.filter(category__name="资讯中心")
    #         elif category == 'regulation':
    #             models.Article.objects.filter(category__name="政策法规")

    # def dispatch(self, request, *args, **kwargs):
    #     self.year = kwargs.get('category')


class ArticleView(generic.DetailView):
    template_name = 'article/news_n.html'
    model = models.Article


class CategoryListView(generic.ListView):
    template_name = 'article/news.html'
    model = models.Category


class CategoryView(generic.DetailView):
    template_name = 'article/news_n.html'
    model = models.Category
