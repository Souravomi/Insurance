from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def Home(request):
    if 'Login' in request.POST:
        username = request.POST['Name']
        password = request.POST['Password']

        try:
            user = auth.authenticate(username=username,password=password)
           
        except:
            user = None

        if user is not None and user.is_staff:
            auth.login(request,user)
            request.session['username'] = username
            return redirect("Admin")
        elif user is not None:
            auth.login(request,user)
            request.session['username'] = username
            return redirect("Home")

        else:
            messages.success(request,'Incorrect Username or Password!')
            return render(request,'Guest/index.html')

    elif 'Register' in request.POST:
        first_name=request.POST['First']
        last_name=request.POST['Last']
        username=request.POST['Email']
        password=request.POST['Password']

        try:
            user= User.objects.get(username=username)
            messages.success(request,'Username or Email Already Taken')
            return render(request,'Guest/index.html')

        except:
            user=User.objects.create_user(username=username,password=password,email=username,first_name=first_name,last_name=last_name)
            user.save()
            messages.success(request,'User Registered Successfully ! You Can Login Now')
            return redirect('/')
    else:
        return render(request,'Guest/index.html')
