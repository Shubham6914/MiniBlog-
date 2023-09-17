from django.shortcuts import render,HttpResponseRedirect
from .forms import signUpform,loginForm,postForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages # used to show messages 
from .models import post
# this group class will help us seperate user and admin in differen groups 
from django.contrib.auth.models import Group 
# Home view

def home(request):
   posts = post.objects.all()
   return render(request, 'blog/home.html',{'posts':posts})

# About view 
def about(request):
   return render(request, 'blog/about.html')

# Contact view 
def contact(request):
   return render(request, 'blog/contact.html')

#Dashboard view
def dashboard(request):
   # this is to check if user is not logged in and trying to access dashboard 
   # then this authentication function will not allow him to access
   if request.user.is_authenticated:
      posts = post.objects.all()
      user = request.user # this is for dsiplaying the individual profile 
      # "get_full_name()" this function will acces the full name of individual user
      full_name = user.get_full_name()
      #this "groups.all()" function will help us to access that which user belongs to which group
      gps = user.groups.all()
      return render(request, 'blog/dashboard.html',{'posts':posts,
                     'full_name':full_name,'groups':gps})
   else:
      return HttpResponseRedirect('/login/')

# Logout view
def user_logout(request):
   logout(request)
   return HttpResponseRedirect('/')

#Signup view
def user_signup(request):
   if request.method == "POST":
      form = signUpform(request.POST)
      if form.is_valid(): #this is used to validate the data durin POST request
         messages.success(request,"Congratulations!! You have become an Author.")
         user = form.save()
         #this Group function will help us to seperate and admin and user to different 
         #group and accordin to their group we have define the rightd to them that what user
         #can do in our site and same for admin 
         group = Group.objects.get(name='Author')
         #this "groups.add()" function help to add users to different groups and accroding
         #to their they can perfom their action 
         user.groups.add(group)
   else:
      form = signUpform()
   return render(request, 'blog/signup.html',{'form':form})

#login view
def user_login(request):
   # this request.user.is_authenticated is used to check that user is already signed 
   # in or no if signed in then return to dashbboard else do the following process 
   if not request.user.is_authenticated:   
      if request.method == "POST":
         form = loginForm(request=request, data = request.POST)
         if form.is_valid():
            uname = form.cleaned_data['username'] #validating login field
            upass = form.cleaned_data['password']
            #authenticate function use to authenticate the data with previous data 
            user = authenticate(username =uname, password = upass) 
            if user is not None:
               login(request, user)
               messages.success(request, 'Logged in Successfully.!!')
               return HttpResponseRedirect('/dashboard/')
      else:
         form = loginForm()
      return render(request, 'blog/login.html',{'form':form})
   return HttpResponseRedirect('/dashboard/')


#Add post view

def add_post(request):
   if request.user.is_authenticated:
      if request.method == 'POST':
         form = postForm(request.POST)
         if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['description']
            pst = post(title = title, description = desc)
            messages.success(request,"Congratulations your Post is Added ")
            pst.save()
            form = postForm()
      else:
         form = postForm()
      return render(request, 'blog/addpost.html',{'form':form})
   else:
      return HttpResponseRedirect('/login/')
   
#update post view
   
def update_post(request,id):
   if request.user.is_authenticated:
      if request.method == 'POST':
         pi = post.objects.get(pk= id) #this used to get a data of individual
         form = postForm(request.POST, instance=pi)
         if form.is_valid():
            form.save()
      else:
         pi = post.objects.get(pk =id)
         form = postForm(instance=pi)
      return render(request, 'blog/updatepost.html',{'form':form})
   else:
      return HttpResponseRedirect('/login/')
   
# delete post view 

def delete_post(request,id):
   if request.user.is_authenticated:
      if request.method == 'POST':
         pi = post.objects.get(pk =id )
         pi.delete()
      return HttpResponseRedirect('/dashboard/')
   else:
      return HttpResponseRedirect('/login/')