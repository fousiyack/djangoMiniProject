from django.contrib.auth.models import User
from django import forms

class UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']
        labels ={
            'firs_tname':'first name',
            'last_name': 'last name',
            'username':'username',
            'email':'email',
        }       