from django.shortcuts import render, redirect, HttpResponse
from .models import User, UserManager
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'djangoLogin_app/index.html')

def process(request):
    if request.POST['login_or_registry'] == 'register':
        errors = User.objects.basic_validator(request.POST)
        if errors:
            for tag, error in errors:
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
        else:
            return redirect('/success')
        
    elif request.POST['login_or_registry'] =='login':
        email = User.objects.get(email= request.POST['email'])
        password = User.objects.get(password= request.POST['password'])
        if email and password:
            logged_in = User.objects.get(email= request.POST['email'])
            request.session['first_name'] = logged_in.first_name
            return redirect('/success')
        else:
            return redirect('/')

    

def success(request):
    return render(request, 'djangoLogin_app/success.html')
