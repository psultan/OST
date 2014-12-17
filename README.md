## Final Project
Author: Paul Sultan

[https://secure-beach-3517.herokuapp.com/hello/all_questions/](https://secure-beach-3517.herokuapp.com/hello/all_questions/)


Heroku

 - python-getting-started(project)

Django

 - gettingstarted(project)
 - hello(app)

### Requirements

 1. Multi-User Support
	 1. Register /accounts/register
		 1. Test User: username:test, password:test
	 2. Login /accounts/login
	 3. Logout /accounts/logout
 2. Editing 
	 1. Authors of posts can edit/delete their Questions/Answers
	 2. Users can vote once per Question/Answer
 3. Pagination
	 1. 10 Questions are listed on the main view /hello/all_questions
	 2. Next/Previous buttons are located on the bottom of the page
 4. Answer Order
	 1. Answers are sorted from largest differance to smallest
 5. Tags
	 1. Questions can have tags (django manytomany relationship)
	 2. When defining a question seperate tags with a comma.
	 3. clicking a tag will show only questions with matching tag
 6. Inline links
	 1. If a answer contains a url to a website or image it will be displayed inline.  (django smarturlize)
 7. Image Upload
	 1. Images can be uploaded /hello/upload
	 2. All uploads can be viewed at /hello/all_uploads
 8. 500 Character Cap
	 1. When viewing all questions, the question title is capped at 500 (django truncatechars)
	 2. Each question has a permalink based on question_id
 9. Timestamps
	 1. Questions/Answers have modtime and createtime attributes.
	 2. modtime is affected when a question/answer is edited
 10. RSS (django syndication)
	 1. feed for all questions /hello/feed
	 2. feed for a question's answers /hello/feed/<question_id>
 11. (Additional Requirement). Branch/Tag
	 1. active branch: rssoff branch
	 2. active branch: docs
	 2. merged branch: recaptcha
	 3. tag: r1

### Bonus
 1. Captcha
	 1. /accounts/register uses google's new reCaptcha validation
 2. Github hosting
	 1. [https://github.com/psultan/OST](https://github.com/psultan/OST)
 3. Documentation using Sphinx + Read The Docs
	 1. [http://ost.readthedocs.org/en/latest/](http://ost.readthedocs.org/en/latest/)
