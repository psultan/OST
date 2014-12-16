from django import forms
from models import Test, Question, Answer

class TestForm(forms.ModelForm):
	class Meta:
		model = Test
		fields = ("thumbnail",)
		
class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ('text',)
		
	tags = forms.CharField(label='Tags', max_length=100)
		
class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ('text',)
		