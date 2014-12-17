'''django syndication for questions/answer pages'''
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from hello.models import Question

class LatestQuestions(Feed):
    '''
    Feed of questions in reverse time
    '''
    title = "Open Source Tools"
    link = "/all_questions/"
    description = "Latest Questions."

    def items(self):
        '''list of objects'''
        return Question.objects.order_by("-createtime")
    def item_link(self, item):
        return reverse("question", args=[item.id])
        
    def item_title(self, item):
        #title of each item
        return item.text
    def item_description(self, item):
        #description of each item
        return item.author
    

class LatestAnswers(Feed):
    '''
    Feed of answers to a specific question id
    '''
    title = "Open Source Tools"
    link = "/all_questions/"
    description = "Latest Answers."
    
    def get_object(self, request, question_id):
        return get_object_or_404(Question, pk=question_id)
    
    def items(self, item):
        #list of objects
        return item.answer_set.order_by("-createtime")
    def item_link(self, item):
        return reverse("question", args=[item.question.id])
        
    def item_title(self, item):
        #title of each item
        return item.text
    def item_description(self, item):
        #description of each item
        return item.author