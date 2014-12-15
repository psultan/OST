from django.db import models
from time import time

def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s"%(str(time()).replace(".","_"),filename)

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Test(models.Model):
	thumbnail = models.FileField(upload_to=get_upload_file_name)