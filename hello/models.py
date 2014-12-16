from django.db import models
from time import time
from django.db.models import Sum

from django.contrib.auth.models import User

def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s"%(str(time()).replace(".","_"),filename)

class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)
class Test(models.Model):
	thumbnail = models.FileField(upload_to=get_upload_file_name)
	

class Tag(models.Model):
	text = models.CharField(max_length=100)
	def __unicode__(self):
		return str(self.id)
class Question(models.Model):
	text       = models.TextField()
	
	modtime    = models.DateTimeField(auto_now=True, auto_now_add=False)
	createtime = models.DateTimeField(auto_now=False, auto_now_add=True)
	
	author  = models.ForeignKey(User)
	tags    = models.ManyToManyField(Tag, related_name='questions')
	
	def __unicode__(self):
		return str(self.id)
		
	def total_votes(self):
		return self.vote_question_set.aggregate(Sum('value'))['value__sum']
	
class Answer(models.Model):
	text        = models.TextField()
	
	modtime     = models.DateTimeField(auto_now=True, auto_now_add=False)
	createtime  = models.DateTimeField(auto_now=False, auto_now_add=True)

	question = models.ForeignKey(Question)
	author   = models.ForeignKey(User)
	
	def __unicode__(self):
		return str(self.id)
		
	def total_votes(self):
		return self.vote_answer_set.aggregate(Sum('value'))['value__sum']
class Vote_Answer(models.Model):
	value = models.SmallIntegerField()
	
	author = models.ForeignKey(User)
	answer = models.ForeignKey(Answer)
	
	def __unicode__(self):
		return str(self.id)
class Vote_Question(models.Model):
	value = models.SmallIntegerField()
	
	author = models.ForeignKey(User)
	question = models.ForeignKey(Question)
	def __unicode__(self):
		return str(self.id)
class Image(models.Model):
	file = models.FileField(upload_to=get_upload_file_name)
'''
class User():
	username
	first_name
	last_name
	email
	password
	is_staff
	is_active
	is_superuser
	last_login
	date_joined
'''