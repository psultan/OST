from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

import hello.views

urlpatterns = patterns('',
	url(r'^$',                                    hello.views.index, name='index'),
	                                              
	url(r'^all_questions/$',                      'hello.views.all_questions'),
	url(r'^tag_questions/(?P<tag_id>\d+)/$',      'hello.views.tag_questions'),
	
	url(r'^question/(?P<question_id>\d+)/$',      'hello.views.question'),

	url(r'^create_question/$',                    'hello.views.create_question'),
	
	url(r'^create_answer/(?P<question_id>\d+)/$', 'hello.views.create_answer'),
	
	url(r'^all_images/$',                         'hello.views.all_images'),
	url(r'^upload/$',                             'hello.views.upload'),

	

)