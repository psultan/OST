from django import forms
from models import Test, Question, Answer

import sys

class TestForm(forms.ModelForm):
	class Meta:
		model = Test
		fields = ("thumbnail",)
		
class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ('text',)
	
	def __init__(self, *args, **kwargs):
		tags = kwargs.pop('tags', "")
		super(QuestionForm, self).__init__(*args, **kwargs)
		if tags:
			self.fields['tags'].initial=tags

	tags = forms.CharField(label='Tags', max_length=100)
		
class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ('text',)
		