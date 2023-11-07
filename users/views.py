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
            if user.is_employer == True:
                return redirect('employers_home')
            else:
                return redirect('candidate_home')
        else:
            messages.error(request, ("Favor de verificar el correo o contraseña."))
            return redirect('login')

    return render(request, "login.html", {})

def logout_user(request):
    user = request.user
    logout(request)
    messages.success(request, ("Has cerrado sesión con éxito!"))
    
    if user.is_employer == True:
        return redirect('employers_home')
    else:
        return redirect('candidates_home')