

# Create your views here
from django.shortcuts import render ,HttpResponse ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
# this url dispatch
# in reder we pass two parameter 1.request and 2. page ka name
# jub bi yaha sa dta khi bajna ho tu assa bajana or usy{{}} is use karna hy
# data={
#     'title':'created',
#     'p':'welcome azmat back the millionare',
#      'list':['java','script','python'],
#       'dic':[
#           {'name':'azmat','phone':342148041274},
#           {'name':'ali','phone':3272812456426},
#           {'name':'ahmad','phone':3272812456426},
#           {'name':'nasir','phone':3272812456426}
#       ]      
# }


def homepage(request):
    return render(request,'index.html')  # agar template file ko excess karna ho tu render use ho ga


# def aboutdetails(request,aboutid):
#         return render(request,'index.html') 
    # return HttpResponse(aboutid)

def login(request):
     if request.method=='POST':
       usern=request.POST.get('username')
       passw=request.POST.get('password')
       user=authenticate(request,username=usern,password=passw)
       if user is not None:
        #    login(request,user)
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
    #    if password1!=password2:
    #    else:
    # my_user=user.objects.create_user(email,password1,password2)

                           
    return render(request,'signup.html')


def logoutpage(request):
    logout(request)
    return redirect(login)






# def about(request):
#     return render(request,'about.html')
# def services(request): 
#     return render(request,'services.html')

# def contact(request):
#     return render(request,'contact.html')

def contactDetails(request,contactid):      # this for daynamic urls 
    return HttpResponse(contactid)