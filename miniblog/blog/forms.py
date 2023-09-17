from django import forms
# this will import built in django froms that will helup us to create a froms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField

#this will import user class from models 
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from .models import post
# this signup form is creaked by manually using buil-in Usercreation form 
class signUpform(UserCreationForm):

   # these both password1 and password to are here used to change label and 
   #and widget used to add 'form-control' class and to make passwordInput hidden 
   password1 = forms.CharField(label='Password',
               widget = forms.PasswordInput(attrs={'class':'form-control my-1'}))
   password2 = forms.CharField(label='Confirm Password',
               widget = forms.PasswordInput(attrs={'class':'form-control my-1'}))
   
   class Meta:
      model = User
      # fields add extra fields to our in-built form 
      fields = ['username','first_name','last_name','email']

      #labels used to change the labels of forms fields
      labels = {'first_name':'First Name','last_name':'Last Name','email':'Email'}


# widget will help us to add class 'form-control' attribute to fields of form
#  form-control is a class of bootstrap whihc will modify the signupform
      widgets = {
      'username':forms.TextInput(attrs={'class':'form-control mb-1'}),
      'first_name':forms.TextInput(attrs={'class':'form-control my-1'}),
      'last_name':forms.TextInput(attrs={'class':'form-control my-1'}),
      'email':forms.TextInput(attrs={'class':'form-control my-1'})
      }

# login form authentication using widget to use the botstrap classes anf 
# built in 'authenticathinForm' from django form

class loginForm(AuthenticationForm):
   username = UsernameField(widget= forms.TextInput(attrs={'autofocus':True,
                                    'class':'form-control'}))
   
   password = forms.CharField(label='Password',strip=False,widget=
               forms.PasswordInput(attrs={'autocomplete':'current-password',
                                 'class':'form-control'}))


# creating form for updating or editing the posts using models post here

class postForm(forms.ModelForm):
   class Meta:
      model = post
      fields = ['title','description']
      labels = {'title':'Title','description':'Description'}
      widgets = {"title": forms.TextInput(attrs={'class':"form-control"}),
                 'description': forms.Textarea(attrs={'class':'form-control'})}