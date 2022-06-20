from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def homeview(request):
    template_name = 'newapp/base.html'
    context = {}
    return render(request, template_name, context)


@login_required(login_url='login')
def appointmentview(request):
    template_name = 'newapp/MakeAppointment.html'
    context = {}
    return render(request, template_name, context)


def ambulanceview(request):
    template_name = 'newapp/OurServices.html'
    context = {}
    return render(request, template_name, context)


def aboutview(request):
    template_name = 'newapp/About us.html'
    context = {}
    return render(request, template_name, context)


def ecomview(request):
    template_name = 'store/products.html'
    context = {}
    return render(request, template_name, context)


def loginview(request):
    if request.method == 'POST':
        u = request.POST.get('uname')
        p = request.POST.get('pw')
        print(f'username entered={u},password entered={p}')
        user = authenticate(username=u, password=p)

        print(user)
        if user is not None:
            login(request, user)
            return redirect('appointment')
        else:
            messages.error(request, 'Invalid Credentials')

    template_name = 'newapp/Login.html'
    context = {}
    return render(request, template_name, context)


def logoutview(request):
    logout(request)
    return redirect('login')


def registerview(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name = 'newapp/Register.html'
    context = {'form': form}
    return render(request, template_name, context)
