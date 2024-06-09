from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from apps.univer.models import *
from modeltranslation.translator import TranslationOptions,register
from modeltranslation.admin import TranslationAdmin


@register(University)
class UniversityTranslationOptions(TranslationOptions):
	fields = ('title',)
	list_display = ('title',)
	search_fields = ('title',)

@admin.register(University)
class UniversityAdmin(TranslationAdmin):
	group_fieldsets = True
	list_display = ("title",)

	class Media:
		js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
		css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
	list_display = ('user',)
	search_fields = ('user',)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ('user',)
	search_fields = ('user',)
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user',)
	search_fields = ('user',)
@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
	list_display = ('title',)
	search_fields = ('title',)
@admin.register(Kabinet)
class KabinetAdmin(admin.ModelAdmin):
	list_display = ('number',)
	search_fields = ('number',)
@admin.register(Raspisanie)
class RaspisanieAdmin(admin.ModelAdmin):
	list_display = ('courses',)
	search_fields = ('courses',)
@admin.register(Zapic)
class ZapicAdmin(admin.ModelAdmin):
	list_display = ('student',)
	search_fields = ('student',)
@admin.register(DZ)
class DZAdmin(admin.ModelAdmin):
	list_display = ('title',)
	search_fields = ('title',)
@admin.register(Sdacha)
class SdachaAdmin(admin.ModelAdmin):
	list_display = ('assignment',)
	search_fields = ('assignment',)
admin.site.site_header = _("Univer")
admin.site.site_title = _("Univer")
