from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('social_media')
    if request.method == 'POST':
        un = request.POST.get('un')
        em = request.POST.get('em')
        pw1 = request.POST.get('pw1')
        pw2 = request.POST.get('pw2')
        if un and em and pw1 and pw2 :
            if pw1 == pw2:
                if not User.objects.filter(username=un).exists():
                    User.objects.create_user(
                        username=un,
                        email=em,
                        password=pw1
                    )
                    return redirect('login')
                else:
                    return render(request, 'signup.html', {'msg': 'Username already exists!'})
            else:
                return render(request, 'signup.html', {'msg': 'Passwords do not match!'})
        else:
            return render(request, 'signup.html', {'msg': 'No Null value accepted!'})   
    return render(request, 'signup.html')

def user_login(request):
    if request.user.is_authenticated:
        return redirect('social_media')
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        user = authenticate(request, username=un, password=pw)
        if user is not None:
            auth_login(request, user)
            return redirect('social_media')
        else:
            return render(request, 'login.html', {'msg': 'Invalid Credentials!!'})
    return render(request, 'login.html')

def user_logout(request):
    auth_logout(request)
    return redirect('login')