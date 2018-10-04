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

