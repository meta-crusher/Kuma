from django.shortcuts import render, redirect
from django.http import HttpResponse

from register.models import User

def home(request):

    try:
        request.session['username']

        print("logged in")
        context = {
            'in':'none',
            'out':'block',
        }
        if request.method == 'GET':
            if ((request.GET.get('songText') is not None) and (request.GET.get('songText').strip() != '')):
                context['songname'] = request.GET.get('songText')
                context['visual'] = 'block'
            else:
                context['visual'] = 'none'

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
            'valname':'Change',
        }
        if 'Save' == request.POST.get('submit'):
            context['value'] = 'readonly'
            context['valname'] = 'Change'
            p = User.objects.get(mUsername = m)
            if request.POST.get('name').strip() != '':
                p.mName = request.POST.get('name')
                p.save()
                context['name'] = p.mName
            if request.POST.get('email').strip() != '':
                p.mEmail = request.POST.get('email')
                p.save()
                context['email'] = p.mEmail
            if request.POST.get('phone').strip() != '':
                p.mPhone = request.POST.get('phone')
                p.save()
                context['phone'] = p.mPhone

        elif request.POST.get('submit'):
            context['value'] = ''
            context['valname'] = 'Save'
        return render(request, 'homepage/home.html', context)
    except:
        return redirect('/')

