from django.forms import fields
from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class updateform(forms.ModelForm):
        class Meta:
           model = Blog
           fields = '__all__' 

"""  widgets = {
                'title':forms.TextInput(attrs={'class':'form-control'}),
                'body':forms.Textarea(attrs={'class':'form-control'}),
                'author':forms.TextInput(attrs={'class':'form-control'})} """

class EditForm(forms.ModelForm):
     class Meta:
         model = Blog
         fields = ['title', 'body']

class Createuserform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
