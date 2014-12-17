hello.urls
==========

.. automodule:: hello.urls

* /all_questions/
* /tag_questions/(?P<tag_id>\d+)/
* /question/(?P<question_id>\d+)/

* /create_question/
* /edit_question/(?P<question_id>\d+)/
* /delete_question/(?P<question_id>\d+)/
* /create_answer/(?P<question_id>\d+)/
* /edit_answer/(?P<answer_id>\d+)/
* /delete_answer/(?P<answer_id>\d+)/
	
* /all_uploads/
* /upload/
	
* /vote/(?P<question_id>\d+)/(?P<answer_id>\d+)/
* /vote/(?P<question_id>\d+)/(?P<direction>-?\d+)/
	
* /feed/
* /feed/(?P<question_id>\d+)


   
   

   
   
   