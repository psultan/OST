from django import forms
from models import Question, Answer, Image

import sys

class ImageForm(forms.ModelForm):
	class Meta:
		model = Image
		fields = ("file",)
		
class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ('text',)
	
	def __init__(self, *args, **kwargs):
		tags = kwargs.pop('tags', "")
		super(QuestionForm, self).__init__(*args, **kwargs)
		if tags:
			self.fields['tags'].initial=tags

	tags = forms.CharField(label='Tags', max_length=100, required=False)
		
class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ('text',)
		