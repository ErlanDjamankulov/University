from rest_framework import serializers
from .models import *
class UniversitySerializer(serializers.ModelSerializer):
	class Meta:
		model=University
		fields='__all__'
class ProfessorSerializer(serializers.ModelSerializer):
	class Meta:
		model=Professor
		fields='__all__'
class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model=Student
		fields='__all__'
class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model=UserProfile
		fields='__all__'
class CoursesSerializer(serializers.ModelSerializer):
	class Meta:
		model=Courses
		fields='__all__'
class KabinetSerializer(serializers.ModelSerializer):
	class Meta:
		model=Kabinet
		fields='__all__'
class RaspisanieSerializer(serializers.ModelSerializer):
	class Meta:
		model=Raspisanie
		fields='__all__'
class ZapicSerializer(serializers.ModelSerializer):
	class Meta:
		model=Zapic
		fields='__all__'
class DZSerializer(serializers.ModelSerializer):
	class Meta:
		model=DZ
		fields='__all__'
class SdachaSerializer(serializers.ModelSerializer):
	class Meta:
		model=Sdacha
		fields='__all__'