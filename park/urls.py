from django.urls import path
from . import views


urlpatterns =[
    path('', views.ParkListView.as_view(), name='parks'),
    path('factory', views.FactoryListView.as_view(), name='factory'),
    path('investment', views.InvestmentListView.as_view(), name='investment'),

    path('<int:pk>', views.ParkView.as_view(), name='park_detail'),
    path('factory/<int:pk>', views.FactoryView.as_view(), name='factory_detail'),
    path('investment/<int:pk>', views.InvestmentView.as_view(), name='investment_detail'),
]