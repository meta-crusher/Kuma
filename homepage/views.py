from django.shortcuts import render, redirect
from django.http import HttpResponse

from register.models import User, Message

def home(request):

    try:
        request.session['semail']
        q = User.objects.get(mEmail = request.session['semail'])
        lmn = Message.objects.filter(mEmail = q)

        context = {
            'in':'none',
            'out':'block',
            'message':lmn,
            'user': request.session['semail'],
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
        del request.session['semail']
        del request.session['spass']
    finally:
        return redirect('/')

def msg(request):
    try:
        print("I not came inside")
        request.session['semail']
        print(request.method)
        if(request.method == 'POST'):
            msg = request.POST.get('msg')
            email = request.session['semail']

            print(msg, email)

            q = User.objects.get(mEmail = email)
            print(q)
            p = Message.objects.create(mEmail = q, mMsg = msg)
            p.save()
            return redirect('/')
    finally:
        return redirect('/')