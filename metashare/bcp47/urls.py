from django.conf.urls import url
from metashare.bcp47 import xhr

urlpatterns = [
    url(r'^xhr/update_lang_variants/$', xhr.update_lang_variants),
    url(r'^xhr/update_var_variants/$', xhr.update_var_variants),
    url(r'^xhr/update_lang_variants_with_script/$', xhr.update_lang_variants_with_script),
]
