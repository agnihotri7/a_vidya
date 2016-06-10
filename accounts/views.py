from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from forms import UserRegisterForm

def login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/')
            else:
                return render(request, 'accounts/login.html', {'msg': 'Your account is disabled.' }, context)
        else:
            return render(request, 'accounts/login.html', {'msg': 'Invalid login details supplied.' }, context)

    return render(request, 'accounts/login.html', context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login/')
        else:
            return render(request, 'accounts/register.html',
                {'form': form}, context)
    else:
        form = UserRegisterForm()

    return render(request, 'accounts/register.html',
            {'form': form}, context)
