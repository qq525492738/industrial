from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import *
from django.views.decorators.cache import cache_page
from django.core.cache import cache

# Create your views here.
