'''
Base URL Routing
'''

from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

import hello.views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^db', hello.views.db, name='db'),

	(r'^hello/', include('hello.urls')),
	
	url(r'^accounts/$',                  'gettingstarted.views.current_user'),
	url(r'^accounts/login/$',            'gettingstarted.views.login'),
	url(r'^accounts/logout/$',           'gettingstarted.views.logout'),
	url(r'^accounts/loggedin/$',         'gettingstarted.views.loggedin'),
	url(r'^accounts/auth/$',             'gettingstarted.views.auth_view'),
	url(r'^accounts/invalid/$',          'gettingstarted.views.invalid_login'),
	url(r'^accounts/register/$',         'gettingstarted.views.register_user'),
	url(r'^accounts/register_success/$', 'gettingstarted.views.register_success'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
	)