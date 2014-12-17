from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

import hello.views
from hello.feeds import LatestQuestions, LatestAnswers

urlpatterns = patterns('',
	url(r'^$',                                      hello.views.index, name='index'),
	                                              
	url(r'^all_questions/$',                        'hello.views.all_questions'),
	url(r'^tag_questions/(?P<tag_id>\d+)/$',        'hello.views.tag_questions'),
	url(r'^question/(?P<question_id>\d+)/$',        'hello.views.question',         name="question"),

	url(r'^create_question/$',                      'hello.views.create_question'),
	url(r'^edit_question/(?P<question_id>\d+)/$',   'hello.views.create_question'),
	url(r'^delete_question/(?P<question_id>\d+)/$', 'hello.views.delete_answer'),
	url(r'^create_answer/(?P<question_id>\d+)/$',   'hello.views.create_answer'),
	url(r'^edit_answer/(?P<answer_id>\d+)/$',       'hello.views.create_answer'),
	url(r'^delete_answer/(?P<answer_id>\d+)/$',     'hello.views.delete_answer'),
	
	url(r'^all_uploads/$',                          'hello.views.all_uploads'),
	url(r'^upload/$',                               'hello.views.upload'),
	
	url(r'^vote/(?P<question_id>\d+)/(?P<answer_id>\d+)/(?P<direction>-?\d+)/$',      'hello.views.vote'),
	url(r'^vote/(?P<question_id>\d+)/(?P<direction>-?\d+)/$',                         'hello.views.vote'),
	
	url(r'^feed/$',								 LatestQuestions()),
	url(r'^feed/(?P<question_id>\d+)/$', 		 LatestAnswers())
)