

# Create your views here
from django.shortcuts import render ,HttpResponse ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout



def homepage(request):
    return render(request,'index.html') 

def login(request):
     if request.method=='POST':
       usern=request.POST.get('username')
       passw=request.POST.get('password')
       user=authenticate(request,username=usern,password=passw)
       if user is not None:
  
           return redirect(homepage)
       else:
           return HttpResponse('not correct') 
     return render(request,'login.html')



def signup(request):
    if request.method=='POST':
       username=request.POST.get('email')
       password1=request.POST.get('pass1')
       password2=request.POST.get('pass2')
       print(username,password1,password2)
       my_user=User.objects.create_user(username,password1,password2)
       my_user.save()
       return redirect(login)
  

                           
    return render(request,'signup.html')


def logoutpage(request):
    logout(request)
    return redirect(login)







