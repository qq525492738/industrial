from django.urls import path, include, re_path
from . import models, views

#app_name='article'

urlpatterns = [
    path('', views.IndexView.as_view(), name='articles'),
    #re_path(r'^(?P<category>.*)/$',views.ArticleListView),
    path('<int:pk>/', views.ArticleView.as_view(), name='article'),
    path('category/', views.CategoryListView.as_view(), name='category_list'),
    path('category/<int:category>/', views.CategoryView.as_view(), name='category'),
]