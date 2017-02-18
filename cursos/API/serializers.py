from rest_framework import serializers
from ..models import *
from django.contrib.auth.models import User 

class SubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subject
		fields = ('id', 'title', 'slug')

class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = ('id', 'subject', 'alumni')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username')		

class CursoSerializer(serializers.ModelSerializer):
	subject = SubjectSerializer(many=False, read_only=True)
	alumni = UserSerializer(many=True, read_only=True)

	class Meta:
		model = Course
		fields = ('id', 'subject', 'alumni')