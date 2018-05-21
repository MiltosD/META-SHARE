from django.conf.urls import url
from metashare.settings import DJANGO_BASE
from metashare.accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'create/$', accounts_views.create, name='create'),
    url(r'confirm/(?P<uuid>[0-9a-f]{32})/$', accounts_views.confirm, name='confirm'),
    url(r'contact/$', accounts_views.contact, name='contact'),
    url(r'reset/(?:(?P<uuid>[0-9a-f]{32})/)?$', accounts_views.reset, name='reset'),
    url(r'profile/$', accounts_views.edit_profile, name='edit_profile'),
    url(r'editor_group_application/$', accounts_views.editor_group_application,
        name='editor_group_application'),
    url(r'organization_application/$', accounts_views.organization_application,
        name='organization_application'),
    url(r'update_default_editor_groups/$', accounts_views.update_default_editor_groups,
        name='update_default_editor_groups'),
]

urlpatterns += [
    url(r'^profile/change_password/$', auth_views.password_change,
        {'post_change_redirect': '/{0}accounts/profile/change_password/done/'.format(DJANGO_BASE),
         'template_name': 'accounts/change_password.html'}, name='password_change'),
    url(r'^profile/change_password/done/$', auth_views.password_change_done,
        {'template_name': 'accounts/change_password_done.html'}, name='password_change_done'),
]
