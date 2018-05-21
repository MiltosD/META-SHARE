from django.conf.urls import url
from metashare.stats import views

urlpatterns = [
    url(r'top/$', views.topstats),
    url(r'mystats/$', views.mystats),
    url(r'usage/$', views.usagestats),
    url(r'days', views.statdays),
    url(r'get.*', views.getstats),
    url(r'portalstats/$', views.portalstats),
]
