from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
#from .models import Student

# Create your views here.
def index(request):
    template_name = 'index.html'
    context = {'form' : 'form'}
    return render(request, template_name, context)

def login(request):
    template_name = 'login.html'
    context = {'form' : 'form'}
    return render(request, template_name, context)

def signup(request):
    template_name = 'signup.html'
    context = {'form' : 'form'}
    return render(request, template_name, context)

def reset_password_questions(request):
    template_name = 'reset_password_questions.html'
    context = {'form' : 'form'}
    return render(request, template_name, context)

def reset_password(request):
    template_name = 'reset_password.html'
    context = {'form' : 'form'}
    return render(request, template_name, context)

def subject(request):
    template_name = 'subject.html'
    context = {'form' : 'form'}
    return render(request, template_name, context)

def document(request):
    template_name = 'document.html'
    context = {'form' : 'form'}
    return render(request, template_name, context)