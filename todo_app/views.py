from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Q
# Create your views here.
@login_required(login_url='login')
def home(request):
    all_data = TaskModel.objects.filter(Q(user = request.user) & Q(is_delete = False) & Q(is_completed = False))
    # print(all_data)
    return render(request,'home.html',{'data':all_data})

@login_required(login_url='login')
def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        
        TaskModel.objects.create(
            title = title,
            desc = desc,
            user = request.user,

        )
        return redirect('home')

    return render(request,'add.html')

@login_required(login_url='login')
def complete(request):
    all_data = TaskModel.objects.filter(Q(user = request.user) & Q(is_delete = False) & Q(is_completed = True))
    return render(request,'complete.html',{'data':all_data})

@login_required(login_url='login')
def trash(request):
    all_data = TaskModel.objects.filter(Q(user = request.user) & Q(is_delete = True))
    return render(request,'trash.html',{'data':all_data})


@login_required(login_url='login')
def about(request):
    return render(request,'about.html')


def completed(request,id):
    c = TaskModel.objects.get(id=id)
    c.is_completed = True
    c.save()
    return redirect(request.META.get('HTTP_REFERER','home'))

def delete(request,id):
    d = TaskModel.objects.get(id=id)
    d.is_delete = True
    d.save()
    return redirect(request.META.get('HTTP_REFERER','home'))

def restore(request,id):
    d = TaskModel.objects.get(id = id)
    d.is_delete = False
    d.save()
    return redirect(request.META.get('HTTP_REFERER','home'))


def complete_all(request):
    all_data = TaskModel.objects.filter(Q(user = request.user) & Q(is_completed = False) & Q(is_delete = False))
    for i in all_data:
        i.is_completed = True
        i.save()
    return redirect('complete')

def delete_all(request):
    all_data = TaskModel.objects.filter(Q(user = request.user) & Q(is_delete = False) & Q(is_completed = False))
    for i in all_data:
        i.is_delete = True
        i.save()
    return redirect('trash')

