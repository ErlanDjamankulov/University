my_list=['University','Professor','Student','UserProfile','Courses','Kabinet','Raspisanie','Zapic','DZ','Sdacha'
]
print(f'# автоматическое заполнение serializers')
print(f'from rest_framework import serializers' )
print(f'from .models import *')
for name in my_list:
    print(f"class {name}Serializer(serializers.ModelSerializer):\n\tclass Meta:\n\t\tmodel={name}\n\t\tfields='__all__'")
print(f'# автоматическое заполнение views')
print(f'''from rest_framework import viewsets
from .serializers import *
from apps.fastfood.utils  import *
from rest_framework import permissions''' )
for name in my_list:
    print(f"class {name}ViewSets(viewsets.ModelViewSet):\n\tqueryset = {name}.objects.all()\n\tserializer_class = {name}Serializer")
print(f'# автоматическое заполнение urls')
print(f'''from django.urls import path,include,re_path
from .views import *''' )
print('urlpatterns = [')
for name in my_list:
    print(f"\t path('{name.lower()}/', {name}ViewSets.as_view({{'get': 'list', 'post': 'create'}}),\n\t\tname='{name.lower()}_list'),")
    print(f"\t path('{name.lower()}/<int:pk>/', {name}ViewSets.as_view({{'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}}),\n\t\tname='{name.lower()}_detail'),")
print(']')
print(f'# автоматическое заполнение admin')
print(f'''from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from apps.fastfood.models import Category''' )
for name in my_list:
    print(f"@admin.register({name})")
    print(f"class {name}Admin(admin.ModelAdmin):")
    print(f"\t list_display = ('title',)")
    print(f"\t search_fields = ('title',)")
print('''admin.site.site_header = _("Name")
admin.site.site_title = _("Name")''')