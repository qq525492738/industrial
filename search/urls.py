import haystack
from django.urls import path, include
from . import models, views


urlpatterns = [
    path('', include('haystack.urls'), name='haystack_search'),

]




