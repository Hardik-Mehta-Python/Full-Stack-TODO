from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from todo_app.models import *
from django.db.models import Q

# Create your views here.
def login_(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user_authenticate = authenticate(username=username,password=password)
        
        if user_authenticate:
            login(request,user_authenticate)
            return redirect('home')
        else:
            return render(request,'login.html',{
                'error':'Invalid Credentials!'
            })


    return render(request,'login.html')



def register(request):

    if request.method == "POST":

        fname = request.POST['first_name']
        lname = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            return render(request,'register.html',{
                'error':'Passwords do not match'
            })

        if User.objects.filter(username=username).exists():
            return render(request,'register.html',{
                'error':'Username already exists'
            })

        if User.objects.filter(email=email).exists():
            return render(request,'register.html',{
                'error':'Email already registered'
            })

        user = User.objects.create(
            first_name=fname,
            last_name=lname,
            username=username,
            email=email
        )

        user.set_password(password)
        user.save()

        return redirect('login')

    return render(request,'register.html')

@login_required(login_url='login')
def profile(request):
    all_tasks = TaskModel.objects.filter(user = request.user).count()
    completed_task  = TaskModel.objects.filter(Q(user = request.user) & Q(is_completed = True)).count()
    pending_task = TaskModel.objects.filter(Q(user = request.user) & Q(is_completed = False)).count()

    if all_tasks>0:
        completion_percentage = (completed_task / all_tasks) * 100
    else:
        completion_percentage = 0

    data = {
        "all_tasks" : all_tasks,
        'completed_task' : completed_task,
        'pending_task' : pending_task,
        'completion_percentage' : completion_percentage

    }
    print(completion_percentage)    

    return render(request,'profile.html',data)

@login_required(login_url='login')
def logout_(request):
    logout(request)

    return redirect('login')

def reset_password(request):
    user = request.user
    if request.method == "POST":
        cPasw = request.POST['cPasw']
        nPasw = request.POST['nPasw']
        confirmPasw = request.POST['confirmPasw']
        
        if user.check_password(cPasw):
            if nPasw == confirmPasw:
                user.set_password(nPasw) 
                user.save()
                return redirect('login') 
            else: return render(request,'reset_password.html',{'error':'Password Not Match'}) 
        else:
            return render(request,'reset_password.html',{'error':'Password Incorrect'})
    return render(request,'reset_password.html')

def forgot(request):
    return render(request,'forgot.html')
