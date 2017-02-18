from django.db import models
from django.contrib.auth.models import User 
class Subject(models.Model):
	title = models.CharField(max_length=30)
	slug = models.SlugField(max_length=60)

	def __str__(self):
		return '{}'.format(self.title)

class Course(models.Model):
	subject = models.ForeignKey(Subject, related_name='courses')
	alumni = models.ManyToManyField(User, related_name = 'courses')
		
	def __str__(self):
		return '{}'.format(self.subject)
