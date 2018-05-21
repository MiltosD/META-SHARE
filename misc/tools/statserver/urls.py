from django.conf.urls import patterns, url
from django.conf import settings
from statserver.stats import views
from django import views as dj_views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^$', views.browse),
    url(r'^stats/addnode$', views.addnode),
    url(r'^media/(?P<path>.*)$', dj_views.static.serve, {'document_root': settings.MEDIA_ROOT}),
]
