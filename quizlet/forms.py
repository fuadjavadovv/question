from dataclasses import fields
from django.forms import ModelForm
from .models import *
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password'] 
 
class addQuestionform(ModelForm):
    class Meta:
        model=Question
        fields="__all__"

class UpdateQuestionform(forms.ModelForm):
    class Meta:
        model=Question
        fields="__all__"

class addQuizform(ModelForm):
    class Meta:
        model = Quiz
        fields = "__all__"
class Reversoform(ModelForm):
    class Meta:
        model = Reverso
        fields = "__all__"