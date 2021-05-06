from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login as loginUser


from app.forms import TODOForm


def home(request):
    form=TODOForm()
    return render(request,'index.html',context={'form':form})


def login(request):
    if request.method=="GET":
        form=AuthenticationForm()
        context={
            "form":form
        }
        return render(request,'login.html',context=context)
    else:
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            form.cleaned_data.get('username')
            form.cleaned_data.get('password')
            user=authenticate(username="username",password="password")
            if user is not None:
                loginUser(request,user)
            return redirect("home")
        else:
            context={
            "form":form
            }
            return render(request,'login.html',context=context)

   

def signup(request):
    if request.method=='GET':
        form=UserCreationForm()
        context={
        "form":form
        }
        return render(request,'signup.html', context=context)
    else:
        form=UserCreationForm(request.POST)
        context={
        "form":form
        }
        if form.is_valid():
            # return HttpResponse("Form is valid")
            user=form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
            # return HttpResponse("form is invalid")
            return render(request,'signup.html', context=context)


