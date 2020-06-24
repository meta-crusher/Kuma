from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import User
from homepage.views import home

def signup(request):
    try:
        print(request.session['username'])
        return redirect('/')
    except:
        if(request.method == 'POST'):

            name = request.POST.get('name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            password = request.POST.get('password')

            #entering data into model....
            p = User.objects.create(mName = name, mUsername = username, mEmail = email, mPhone = phone, mPassword = password)
            p.save()
            return redirect('/login/')
        else:
            return render(request, 'register/signup.html')

def login(request):

    try:
        print(request.session['username'])
        return redirect('/')
    except:
        if(request.method == 'POST'):
            Username = request.POST.get('username')
            Pass = request.POST.get('pass')

            a = User.objects.get(mUsername = Username)
            if(a.mPassword == Pass):
                request.session['username'] = Username
                return redirect('/')
        else:
            return render(request, 'register/login.html')

