from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def base(request):
    return render(request, 'base.html')

def ktpl(request):
    return render(request, 'ktpl.html')

def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == "" or password == "":
            messages.error(request, "All fields are required")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        User.objects.create_user(username=username, password=password)
        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, 'signup.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')   # ✅ after login success
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')       # ✅ stay on login page

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def led_control(request):

    status = "OFF"

    # Check button click
    if request.method == "POST":

        led = request.POST.get("led")

        # LED ON
        if led == "on":
            status = "ON"

        # LED OFF
        elif led == "off":
            status = "OFF"

    return render(request, "led.html", {"status": status})
"""
import serial
from django.shortcuts import render

pico = None

try:
    pico = serial.Serial('COM8', 115200)
except:
    print("Pico not connected")

def led_control(request):

    status = "OFF"

    if request.method == "POST":

        led = request.POST.get("led")

        if pico:

            if led == "on":
                pico.write(b'ON\n')
                status = "ON"

            elif led == "off":
                pico.write(b'OFF\n')
                status = "OFF"

    return render(request, "led.html", {"status": status})"""