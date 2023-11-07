from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def login_user(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Has iniciado sesión con éxito!"))
            return redirect('login')
        else:
            messages.error(request, ("Favor de verificar el correo o contraseña."))
            return redirect('login')

    return render(request, "login.html", {})