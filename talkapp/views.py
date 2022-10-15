from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
# Create your views here.

def index(request):
    return render(request,'index.html')

def loginpage(request):
    return render(request,'loginpage.html')

def handle_login(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['username']
        loginpassword = request.POST['password']

        user = authenticate(request,username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("userpage")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("loginpage")

    return HttpResponse("404- Not found")

def userpage(request):
    if request.user.is_authenticated:
        ls=[]

        datas = data.objects.all().order_by('-id')

        for item in datas:
            print(item.id)
            message= item.message[:50]
            ls.append(message)
        zipped=zip(datas,ls)
        context={'data':datas,'zipped':zipped}
        return render(request, 'userpage.html', context)

def handle_logout(request):

    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('loginpage')

def message(request,id):
     if request.user.is_authenticated:
        content=data.objects.filter(id=id).first()

        context={'content':content}
        return render(request,'message.html',context)

     else:
        return HttpResponse("404 not allowed")

def send(request):
    if request.user.is_authenticated:

        return render(request,'send.html')
    else:
        return HttpResponse("404 not allowed")

import pytz
def make_entry(request):
    if request.user.is_authenticated:


        if request.method == 'POST':
              try:
                   subject = request.POST['subject']
                   message = request.POST['message']
                   from datetime import timedelta
                   timezone=pytz.timezone('Asia/Kolkata')
                   now = datetime.now(tz=timezone)
                   dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
                   print("date  =", dt_string[:10])
                   print("time =", dt_string[11:])
                   dates = dt_string[:10]
                   time = dt_string[11:]
                   data.objects.create(user=request.user,message=message,subject=subject,date=dates,time=time)
                   messages.success(request, "Message Sent Successfully")
                   return redirect("userpage")
              except:
                   messages.error(request,"Message did not sent please contact the administrator")
                   return redirect("userpage")
        else:
            return HttpResponse("404 not allowed")

    else:
        return HttpResponse("Please login")