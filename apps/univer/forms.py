from allauth.account.forms import SignupForm
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import UserProfile,University


class MyCustomSignupForm(SignupForm):
    univer = forms.ModelChoiceField(queryset=University.objects.all(), required=True, label='Университет')
    status = forms.ChoiceField(choices=UserProfile.CHOICES_METHOD, required=True, label='Учитель или студент?')
    bio = forms.CharField(max_length=64, required=True, label='ФИО', help_text='Введите полное имя')

    def save(self, request):
        user=super(MyCustomSignupForm,self).save(request)

        univer=self.cleaned_data['univer']
        status=self.cleaned_data['status']
        bio=self.cleaned_data['bio']

        if hasattr(user,'userprofile'):
            profile=user.userprofile
        else:
            profile=UserProfile(user=user)

        profile.univer=univer
        profile.status=status
        profile.bio=bio
        profile.save()

        return user