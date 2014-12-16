from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

import requests
import os
import sys

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
def create_question(request, question_id=None):
	user = request.user
	if request.POST:
		#save form
		question=None
		question_id = request.POST["question_id"]
		if question_id:
			#editing
			question=Question.objects.get(id=question_id)
		form = QuestionForm(request.POST, instance=question)
		if form.is_valid():
			author  = user.username
			question=form.save(commit=False)
			question.author = user
			question.save()
			
			currentTags=question.tags.all()
			for eachTag in currentTags:
				question.tags.remove(eachTag)
			
			tags=request.POST['tags']
			if tags:
				tags=tags.split(",")
				print >>sys.stderr, repr(tags)
				for eachTag in tags:
					thisTag=Tag.objects.filter(text=eachTag)
					if not thisTag:
						#new tag
						tag = Tag(text=eachTag.strip())
						tag.save()
					else:
						#old tag
						tag=thisTag[0]
					question.tags.add(tag)
			return HttpResponseRedirect('/hello/question/%s'%question.id)
	else:
		#show form
		args={}
		question=None
		tags=""
		if question_id:
			#editing current
			question=Question.objects.get(id=question_id)
			args["question_id"]=question_id
			tags=",".join(question.tags.values_list("text", flat=True))
			
		form = QuestionForm(tags=tags, instance=question)
		args['form'] = form
		
		return render_to_response("create_question.html", args, context_instance=RequestContext(request))
@login_required
def create_answer(request, question_id=None, answer_id=None):
	user = request.user
	if request.POST:
		#save form
		answer=None
		answer_id=request.POST["answer_id"]
		if answer_id:
			#editing
			answer=Answer.objects.get(id=answer_id)
		form = AnswerForm(request.POST, instance=answer)
		if form.is_valid():
			author  = user.username
			answer=form.save(commit=False)
			answer.author = user
			answer.question = Question.objects.get(pk=question_id)
			answer.save()
			
			return HttpResponseRedirect('/hello/question/%s'%question_id)
	else:
		args={}
		answer=None
		if answer_id:
			#edit current
			answer=Answer.objects.get(id=answer_id)
			args['question_id']=answer.question.id
			args['answer_id']=answer
		else:
			#show new form
			args['question_id']=question_id
		form = AnswerForm(instance=answer)
		args['form'] = form
		
		return render_to_response("create_answer.html", args, context_instance=RequestContext(request))
@login_required
def delete_answer(request, answer_id=None):
	answer=Answer.objects.get(id=answer_id)
	question=answer.question
	answer.delete()
	return HttpResponseRedirect('/hello/question/%s'%question.id)
@login_required
def delete_answer(request, question_id=None):
	question=Question.objects.get(id=question_id)
	question.delete()
	return HttpResponseRedirect('/hello/all_questions')
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

	
	