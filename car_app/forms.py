from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from car_app.models import comment


class signup(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name =  forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        
        
class user_change_form(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['name','email','body']