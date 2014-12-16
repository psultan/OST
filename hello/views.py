from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

import requests
import os

from models import Greeting, Test, Tag, Question, Answer, Vote_Answer, Vote_Question
from forms import TestForm, QuestionForm, AnswerForm

def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, 'db.html', {'greetings': greetings})
def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print r.text
    return HttpResponse('<pre>' + r.text + '</pre>')

	
def all_images(request):
	return render_to_response('all_images.html', {'tests': Test.objects.all()})
def all_questions(request):
	return render_to_response('all_questions.html', {'questions': Question.objects.all()})
def tag_questions(request, tag_id):
	tag=Tag.objects.get(id=tag_id)
	questions=tag.questions.all()

	return render_to_response('all_questions.html', {'questions': questions})
def question(request, question_id=1):
	question=Question.objects.get(id=question_id)
	answers=question.answer_set.all()
	return render_to_response('question.html',
								{'question': question,
								 'answers':answers},context_instance=RequestContext(request))

@login_required
def upload(request):
	if request.POST:
		#save form
		form = TestForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/hello/all_images')
	else:
		#show form
		form = TestForm()
		args={}
		args['form'] = form
		return render_to_response("upload.html", args, context_instance=RequestContext(request))
@login_required
def create_question(request):
	user = request.user
	if request.POST:
		#save form
		author  = user.username
		form = QuestionForm(request.POST)
		if form.is_valid():
			question=form.save(commit=False)
			question.author = user
			question.save()
			
			tags=request.POST['tags'].split(",")
			for eachTag in tags:
				currentTag=Tag.objects.filter(text=eachTag)
				if not currentTag:
					tag = Tag(text=eachTag.strip())
					tag.save()
				else:
					tag=currentTag.get()
				question.tags.add(tag)
			
			return HttpResponseRedirect('/hello/all_questions/')
		return HttpResponseRedirect('/hello/all_questions/')
	else:
		#show form
		form = QuestionForm()
		args={}
		args['form'] = form
		return render_to_response("create_question.html", args, context_instance=RequestContext(request))
@login_required
def create_answer(request, question_id):
	user = request.user
	if request.POST:
		#save form
		author  = user.username
		form = AnswerForm(request.POST)
		if form.is_valid():
			answer=form.save(commit=False)
			answer.author = user
			answer.question = Question.objects.get(pk=question_id)
			answer.save()
			
			return HttpResponseRedirect('/hello/all_questions/')
	else:
		#show form
		form = AnswerForm()
		args={}
		args['form'] = form
		args['question_id']=question_id
		return render_to_response("create_answer.html", args, context_instance=RequestContext(request))
		
@login_required
def vote(request, direction, question_id=None, answer_id=None):
	user = request.user
		
	if answer_id:
		answer = Answer.objects.get(id=answer_id)
		current_vote=answer.vote_answer_set.filter(author__exact=user)
		if not current_vote:
			vote=Vote_Answer(value=direction, author=user, answer=answer)
		else:
			vote=current_vote[0]
			vote.value=direction
	else:
		question = Question.objects.get(id=question_id)
		current_vote=question.vote_question_set.filter(author__exact=user)
		if not current_vote:
			vote=Vote_Question(value=direction, author=user, question=question)
		else:
			vote=current_vote[0]
			vote.value=direction
	vote.save()
	return HttpResponseRedirect('/hello/question/%s'%question_id)

	
	