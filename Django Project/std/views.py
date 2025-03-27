from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login as log,logout as log_out
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect, HttpResponse
from .models import details,cs_data,ds_data
from .form import group

def a(request):
    return redirect('home')

def edit(request, pk):
    page = 'edit'
    roll = details.objects.get(id=pk)
    form = group(instance=roll)
    if request.method == 'POST':
        form = group(request.POST, instance=roll)
        if form.is_valid():
            form.save()
        return redirect('search')
    context = {'form': form, 'page':page}
    return render(request, 'std/forms.html', context)

def home(request):
    return render(request, 'std/index.html')

def login_home(request):
    return render(request,'std/index.html')

def login(request):
    page = 'login'
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            log(request,user)
            msg = 'msg_success'
            context = {'msg':msg}
            return redirect('home')
        else:
            msg_invaild = messages.error(request, "Invaild Details")
            context = {'msg':msg_invaild}
    context = {'page':page}
    return render(request, 'std/Login.html', context)
    


def signup(request):
    if request.method == "POST":
        uemail = request.POST.get('email')
        uname = request.POST.get('username')
        roll = request.POST.get('roll')
        upass = request.POST.get('pass')
        
        data = User.objects.create_user(email=uemail,username=uname,password=upass)
        data.save()
        messages.success(request, "Account Succefully Created")
        return redirect('login')
    else:
        return render(request,'std/login.html')

def logout(request):
    log_out(request)
    return redirect('')


def display(request):

    display = details.objects.all()
    a = {'display':display}
    return render(request, 'std/display.html', a)

def search(request):
    roll = details.objects.all()
    q = request.GET.get('q')
    if q is not None:
        roll = details.objects.filter(Name__icontains=q)
    context = {'data':roll}
    return render(request, 'std/search.html', context)

def cs_data_search(request):
    roll = cs_data.objects.all()
    q = request.GET.get('q')
    if q is not None:
        roll = cs_data.objects.filter(Name__icontains=q)
    context = {'data':roll}
    return render(request, 'std/search.html', context)

def ds_data_search(request):
    roll = ds_data.objects.all()
    q = request.GET.get('q')
    if q is not None:
        roll = ds_data.objects.filter(Name__icontains=q)
    context = {'data':roll}
    return render(request, 'std/search.html', context)


def add(request):
    add = group()
    if request.method == "POST":
        form = group(request.POST)
        if form.is_valid():
            form.save()
            return redirect('search')
    context = {'add': add}
    return render(request,'std/forms.html',context)

def delete(request, pk):
    roll = details.objects.get(id=pk)
    context = {'roll':roll}
    if request.method == "POST":
        roll.delete()
        return redirect('search')
    return render(request, 'std/delete.html', context)

def cse(request):
    page = 'cse'
    context = {'page': page}
    return render(request,'std/displayContent.html', context)

def cs(request):
    page = 'cs'
    context = {'page': page}
    return render(request,'std/displayContent.html', context)

def ds(request):
    page = 'ds'
    context = {'page': page}
    return render(request,'std/displayContent.html', context)

def aiml(request):
    page = 'aiml'
    context = {'page': page}
    return render(request,'std/displayContent.html', context)