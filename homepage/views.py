from django.shortcuts import render
from django.http import HttpResponse

from register.models import User

def home(request):

    if(request.method == 'POST'):
        Email = request.POST.get('Email')
        Pass = request.POST.get('Password')

        a = User.objects.get(mEmail = Email)
        if(a.mPassword == Pass):
            request.session['semail'] = Email
            request.session['spass'] = Pass
            return HttpResponse("logged in")
        else:
            return HttpResponse("enter password correctly")

    try:
        del request.session['semail']
        del request.session['spass']
        return HttpResponse("Welcome again")
    except:
        return HttpResponse("Welcome to the jungle")
        
