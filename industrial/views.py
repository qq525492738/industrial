from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import View, DetailView, TemplateView
import park.models, article.models


class Home(TemplateView):
    template_name = 'industrial/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test'] = 'test'
        context['news'] = article.models.Article.objects.all()[:5]

        return context


def test(request):

    classify, err = article.models.Classify.objects.get_or_create(name='云南省工业园区', defaults={'name': '云南工业园区'})

    category_list = ['资讯中心', '政策法规', '领导调研', '通知公告', '园区动态', '园区交流', '经验交流', '投融资', '产业聚集', '专题研讨', '园区风采','专题','协会简介','协会章程','业务范围','入会申请','联系协会']

    for each in category_list:
        category,err = article.models.Category.objects.get_or_create(name=each, defaults={'name': each, 'classify':classify})


        for n in range(0,10):
            a=article.models.Article.objects.create(title=each+str(n), content=each)
            a.category.add(category)

    park_classify,err = park.models.ParkClassify.objects.get_or_create(name='云南省', defaults= {'name':'云南省'})



    park_category_list = ['省级','国家级','州市级','其他']

    for each in park_category_list:
        park_category,err =park.category=park.models.ParkCategory.objects.get_or_create(name=each, defaults={'name':each, 'classify':park_classify})

        for p in range(0,10):
            park_obj,err = park.models.Park.objects.get_or_create(name=each+str(p),defaults={'category':park_category,'name':each+str(p), 'logo':'upload/'})


    return JsonResponse({'err':'ok'})