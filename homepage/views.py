from django.shortcuts import render, redirect
from django.http import HttpResponse

from register.models import User

def home(request):

    try:
        request.session['username']

        context = {
            'in':'none',
            'out':'block',
        }
        return render(request, 'homepage/home.html',context)
    except:
        context = {
            'in':'block',
            'out':'none',
        }
        return render(request, 'homepage/home.html',context)
        
def logout(request):
    try:
        del request.session['username']
    finally:
        return redirect('/')

def profile(request):
    try:
        m = request.session['username']
        p = User.objects.get(mUsername = m)
        print(p.mName)
        name = p.mName
        username = p.mUsername
        email = p.mEmail
        phone = p.mPhone
        context = {
            'name': name,
            'username': username,
            'email': email,
            'phone': phone,
            'value': 'readonly',
            'allow': True,
            'in': 'none',
            'out': 'block',
        }
        return render(request, 'homepage/home.html', context)
    except:
        return redirect('/')
