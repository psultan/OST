from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

import hello.views

urlpatterns = patterns('',
	url(r'^$', 					hello.views.index, name='index'),
    url(r'^all/$',              'hello.views.all'),
	url(r'^create/$',           'hello.views.create'),
)