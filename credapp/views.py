
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages,auth

# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login (request,user)
            return redirect ('/')
        else:
            messages.info(request,'invalid')
            return redirect('login')
    return render(request,'login.html')  

def reg(request):
    if request.method=='POST':
            f_name=request.POST['first_name']
            l_name=request.POST['last_name']
            uname=request.POST['username']
            eid=request.POST['email']
            password=request.POST['password']
            cpassword=request.POST['cpassword']
            if password == cpassword:
                if User.objects.filter(username=uname).exists():
                    messages.info(request,"username already taken")
                    return redirect("reg")
                else:
                    user=User.objects.create_user(first_name=f_name,last_name=l_name,
                                          username=uname,email=eid,password=password)
                    user.save()
                    print("user created")
                    return redirect('login')
            else:
                messages.info(request,"wrong password") 
            return redirect('reg') 
    # return redirect('/')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
