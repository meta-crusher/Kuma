from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import User
from homepage.views import home

def signup(request):
    try:
        print(request.session['semail'])
        return redirect('/')
    except:
        if(request.method == 'POST'):

            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            password = request.POST.get('password')

            #entering data into model....
            p = User.objects.create(mName = name, mEmail = email, mPhone = phone, mPassword = password)
            p.save()
            return redirect('/login/')
        else:
            return render(request, 'register/signup.html')

def login(request):

    try:
        print(request.session['semail'])
        return redirect('/')
    except:
        if(request.method == 'POST'):
            Email = request.POST.get('Email')
            Pass = request.POST.get('Password')

            a = User.objects.get(mEmail = Email)
            if(a.mPassword == Pass):
                request.session['semail'] = Email
                request.session['spass'] = Pass
                return redirect('/')
        else:
            return render(request, 'register/login.html')

