from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from industrial import settings
from . import models
from django.db.models import Q

class ParkListView(ListView):
    template_name = 'park/park.html'

    def get_queryset(self):
        self.region = self.request.GET.get('region', '')
        self.category = self.request.GET.get('category', '')
        filter_data = {}
        if self.category:
            filter_data['category__name'] = self.category
        if self.region:
            filter_data['category__classify__name'] = self.region

        self.search = self.request.GET.get('q', False)
        args = ()
        if self.search:
            args = Q(name__contains=self.search) | Q(introduction__contains=self.search),

        self.paginator = Paginator(models.Park.objects.filter(*args, **filter_data), settings.ARTICLE_LIST_NUMBER_OF_EACH_PAGE)

        self.page = self.paginator.get_page(self.request.GET.get('page', 1))

        return self.page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.paginator.count
        context['addr'] = {'region': self.region, 'category': self.category, 'q':self.search}
        context['region_list'] = models.ParkClassify.objects.all()
        context['category_list'] = models.ParkCategory.objects.all()
        current_page_num = self.page.number
        page_range = list(range(max(current_page_num-2, 1), current_page_num)) + \
                     list(range(current_page_num, min(current_page_num + 2, self.paginator.num_pages)+1))

        if page_range[0] >= 3:
            page_range.insert('...')
        if page_range[-1] <= self.paginator.num_pages-3:
            page_range.append('...')

        if page_range[0] != 1:
            page_range.insert(0, 1)
        if page_range[-1] != self.paginator.num_pages:
            page_range.append(self.paginator.num_pages)
        context['page_range'] = page_range
        return context


class InvestmentListView(ListView):
    template_name = 'park/investment.html'

    def get_queryset(self):
        self.region = self.request.GET.get('region', '')
        self.park = self.request.GET.get('park', '')
        # self.park = self.request.GET.get('park','')
        self.area_s = self.request.GET.get('area_s', '')
        self.area_e = self.request.GET.get('area_e', '')
        self.industry = self.request.GET.get('industry', '')
        filter_data = {}
        if self.park:
            filter_data['park__category__name'] = self.park
        if self.region:
            filter_data['park__category__classify__name'] = self.region
        if self.area_s or self.area_e:
            if self.area_e != '0':
                filter_data['area__range'] = (self.area_s, self.area_e)
            elif self.area_e == '0':
                filter_data['area__gte'] = self.area_s
        self.search = self.request.GET.get('q', False)
        args = ()
        if self.search:
            args = Q(name__contains=self.search) | Q(content__contains=self.search),


        if self.industry:
            filter_data['industry'] = self.industry
        self.paginator = Paginator(models.Investment.objects.filter(*args, **filter_data), settings.PARK_LIST_NUMBER_OF_EACH_PAGE)
        self.page = self.paginator.get_page(self.request.GET.get('page', 1))
        return self.page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['count'] = models.Park.objects.count()
        context['addr'] = {'region': self.region, 'park': self.park, 'area_s': self.area_s, 'area_e': self.area_e,
                           'industry': self.industry,'q':self.search}
        context['region_list'] = models.ParkClassify.objects.all()
        context['category_list'] = models.ParkCategory.objects.all().values().distinct()
        context['area'] = [(0, 500), (500, 1000), (1000, 2000), (2000, 3000), (3000, 0)]
        context['industry_list'] = models.Investment.objects.all()  # .values('id').distinct('id')
        current_page_num = self.page.number
        page_range = list(range(max(current_page_num-2, 1), current_page_num)) + \
                     list(range(current_page_num, min(current_page_num + 2, self.paginator.num_pages)+1))
        if page_range[0] >= 3:
            page_range.insert('...')
        if page_range[-1] <= self.paginator.num_pages-3:
            page_range.append('...')

        if page_range[0] != 1:
            page_range.insert(0, 1)
        if page_range[-1] != self.paginator.num_pages:
            page_range.append(self.paginator.num_pages)
        context['page_range'] = page_range
        return context


class FactoryListView(ListView):
    template_name = 'park/factory.html'

    def get_queryset(self):
        self.region = self.request.GET.get('region', '')
        self.park = self.request.GET.get('park', '')
        # self.park = self.request.GET.get('park','')
        self.area_s = self.request.GET.get('area_s', '')
        self.area_e = self.request.GET.get('area_e', '')
        self.intention = self.request.GET.get('intention', '')
        self.category = self.request.GET.get('category', '')
        filter_data = {}
        if self.park:
            filter_data['park__category__name'] = self.park
        if self.region:
            filter_data['park__category__classify__name'] = self.region
        if self.area_s or self.area_e:
            if self.area_e != '0':
                filter_data['area__range'] = (self.area_s, self.area_e)
            elif self.area_e == '0':
                filter_data['area__gte'] = self.area_s

        if self.intention:
            filter_data['intention'] = self.intention
        if self.category:
            filter_data['category'] = self.category
        self.search = self.request.GET.get('q', False)

        args = ()
        if self.search:
            args = Q(name__contains=self.search) | Q(introduction__contains=self.search),

        self.paginator = Paginator(models.Factory.objects.filter(*args, **filter_data), settings.FACTORY_LIST_NUMBER_OF_EACH_PAGE)
        self.page = self.paginator.get_page(self.request.GET.get('page', 1))
        return self.page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['count'] = models.Park.objects.count()
        context['addr'] = {'region': self.region, 'park': self.park, 'area_s': self.area_s, 'area_e': self.area_e,
                           'intention': self.intention, 'category': self.category, 'q':self.search}
        context['region_list'] = models.ParkClassify.objects.all()
        context['category_list'] = models.ParkCategory.objects.all().values().distinct()
        context['area'] = [(0, 500), (500, 1000), (1000, 2000), (2000, 3000), (3000, 0)]
        context['industry_list'] = models.Investment.objects.all()  # .values('id').distinct('id')
        current_page_num = self.page.number
        page_range = list(range(max(current_page_num-2, 1), current_page_num)) + \
                     list(range(current_page_num, min(current_page_num + 2, self.paginator.num_pages)+1))
        if page_range[0] >= 3:
            page_range.insert('...')
        if page_range[-1] <= self.paginator.num_pages-3:
            page_range.append('...')

        if page_range[0] != 1:
            page_range.insert(0, 1)
        if page_range[-1] != self.paginator.num_pages:
            page_range.append(self.paginator.num_pages)
        context['page_range'] = page_range
        return context


class ParkView(DetailView):
    template_name = 'park/park_detail.html'
    model = models.Park


class InvestmentView(DetailView):
    template_name = 'park/investment_detail.html'
    model = models.Investment


class FactoryView(DetailView):
    template_name = 'park/factory_detail.html'
    model = models.Factory





