from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Student

# Create your views here.
def index(request):
    template_name = 'index.html'
    context = {'form' : 'form'}
    return render(request, template_name, context)

def loguser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            print('User verified')
            print(request.user.username)
            return redirect("subject")
        else:
            messages.error(request, 'Input correct username and password')
            print('No such user')
    template_name = 'login.html'
    context = {'form' : 'form'}
    return render(request, template_name, context)

def logoutUser(request):
    logout(request)
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        test = User.objects.create(
            username = email,
            email = email,
        )
        test.set_password(request.POST.get('password'))
        test.save()
        fname = request.POST.get('fname')
        br = request.POST.get('branch')
        yr = request.POST.get('yr')
        clg = request.POST.get('clg')
        pw = request.POST.get('password')
        conf_pw = request.POST.get('confirmpassword')
        obj1 = Student.objects.create(
            fullName = fname,
            email = email,
            year = yr,
            college = clg,
            branch = br,
            password = pw,
            confirmPassword = conf_pw,
        )
        obj1.save()
    template_name = 'signup.html'
    context = {'form' : 'form'}
    return render(request, template_name, context)

def resetPasswordQuestions(request):
    template_name = 'resetPasswordQuestions.html'
    context = {'form' : 'form'}
    return render(request, template_name, context)

def resetPassword(request):
    template_name = 'resetPassword.html'
    context = {'form' : 'form'}
    return render(request, template_name, context)

@login_required
def subject(request):
    template_name = 'subject.html'
    context = {'form' : 'form'}
    return render(request, template_name, context)

@login_required
def document(request):
    template_name = 'document.html'
    context = {'form' : 'form'}
    return render(request, template_name, context)