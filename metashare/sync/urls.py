from django.conf.urls import url
from metashare.sync import views

urlpatterns = [
  url(r'^$', views.inventory),
  url(r'^(?P<resource_uuid>[0-9a-fA-F]{64})/metadata/$', views.full_metadata),
]
