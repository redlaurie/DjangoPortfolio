from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class meta:
        model = User
        fields = ['username','email','password1','password2','CV']


class DiaryAdditionForm(forms.ModelForm):

    class Meta:
        model = DiaryItem
        fields = ['name', 'diary']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(DiaryAdditionForm, self).__init__(*args, **kwargs)
        self.fields['diary'].queryset = Diary.objects.filter(Profile=user)