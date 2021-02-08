from django.shortcuts import render,redirect
from django.contrib import auth
# import auth from django.contrib and call methods as auth.authenticate,auth.login,auth.logout otherwise we will get an error as we would be overriding defaullt methods.
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,f'Welcome {request.user}')
            return redirect('home')
        else:
            # go in settings.py and set MESSAGE_TAGS = {constants.error:'danger'} after doing "from django.contrib.messages import constants"
            messages.error(request,'Invalid credentials')
    return render(request,'accounts/login.html',{})


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['name']
        password = request.POST['password']
        email = request.POST['email']
        # Creating User
        user = User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
        messages.success(request,'Successful Registration')
        return redirect('login')
    return render(request,'accounts/register.html')


def logout_user(request):
    messages.info(request,f'Thank you for using our service, {request.user}')
    auth.logout(request)
    return redirect('home')



# To access user in our views use "request.user" and in our templates as "user"