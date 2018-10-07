from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
import xadmin
from django.views.static import serve
from industrial import settings
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('article/', include('article.urls')),
    path('park/', include('park.urls')),
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('search/', include('search.urls')),
    re_path(r'^haystack_search/', include('haystack.urls'), name='haystack_search'),
    path('test', views.test, name='test'),
    path('t', views.TV.as_view(), name='t'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
