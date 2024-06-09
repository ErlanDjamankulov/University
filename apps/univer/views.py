from rest_framework import viewsets
from .serializers import *
class UniversityViewSets(viewsets.ModelViewSet):
	queryset = University.objects.all()
	serializer_class = UniversitySerializer
	filterset_fields = ['title',]
class ProfessorViewSets(viewsets.ModelViewSet):
	queryset = Professor.objects.all()
	serializer_class = ProfessorSerializer

class StudentViewSets(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
class UserProfileViewSets(viewsets.ModelViewSet):
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer
class CoursesViewSets(viewsets.ModelViewSet):
	queryset = Courses.objects.all()
	serializer_class = CoursesSerializer
	filterset_fields = ['professor',]
	search_fields = ['title','professor']

class KabinetViewSets(viewsets.ModelViewSet):
	queryset = Kabinet.objects.all()
	serializer_class = KabinetSerializer
class RaspisanieViewSets(viewsets.ModelViewSet):
	queryset = Raspisanie.objects.all()
	serializer_class = RaspisanieSerializer
class ZapicViewSets(viewsets.ModelViewSet):
	queryset = Zapic.objects.all()
	serializer_class = ZapicSerializer
class DZViewSets(viewsets.ModelViewSet):
	queryset = DZ.objects.all()
	serializer_class = DZSerializer
class SdachaViewSets(viewsets.ModelViewSet):
	queryset = Sdacha.objects.all()
	serializer_class = SdachaSerializer
