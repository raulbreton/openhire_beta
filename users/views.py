from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm

def login_user(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #messages.success(request, ("Has iniciado sesión con éxito!"))
            if user.is_employer == True:
                return redirect('employers_home')
            else:
                return redirect('candidates_home')
        else:
            messages.error(request, ("Favor de verificar el correo o contraseña."))
            return redirect('login')

    return render(request, "login.html", {})

def logout_user(request):
    user = request.user
    logout(request)
    #messages.success(request, ("Has cerrado sesión con éxito!"))
    
    if user.is_employer == True:
        return redirect('employers_home')
    else:
        return redirect('candidates_home')
    
def register_user(request):
    form = SignUpForm
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['is_employer'] == True and form.cleaned_data['is_candidate'] == True:
                messages.error(request, 'Selecciona solamente una de las dos opciones de tipo de perfil.')
                return render(request, "register.html", {'form':form})
            else:
                form.save()
                email = form.cleaned_data['email']
                password = form.cleaned_data['password1']
                is_employer = form.cleaned_data['is_employer']
                is_candidate = form.cleaned_data['is_candidate']
                #Log in user
                user = authenticate(username=email,password=password)
                login(request,user)
                #messages.success(request, 'Te has registrado con éxito!')
                
                if is_employer == True:
                    return redirect('employers_home')
                else:
                    return redirect('candidates_home')
            
    return render(request, "register.html", {'form':form})