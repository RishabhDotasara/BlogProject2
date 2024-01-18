from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
# from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login_user(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user=user)
            print("Logged_In")
            # messages.success(request,'Logged in succesfully.')
            messages.success(request,"Login successful!")
            return redirect('home')
        else:
            # messages.error(request,'Authentication Failed! Please try logging in again.')
            messages.error(request,"No such user found, please consider making account.")
            return redirect('/auth/signup')
        
    elif request.user.is_authenticated:
        logout(request=request)
        return redirect('home')
    else:
        return render(request,'login.html')
    
def signup_user(request):

    if request.method == 'POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']    
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user=user)
            messages.success(request,"Account created successfully!")
            return redirect('/profile')

    else:
        form = UserCreationForm()    
    return render(request,'signup.html',{'form':form})