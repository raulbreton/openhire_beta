from django.shortcuts import redirect, render
from django.contrib import messages
from users.models import CustomUser
from django.contrib.auth import login
from .models import EmployerProfile
from .forms import EmployerProfileForm

def employers_home(request):
    return render( request, "employers_home.html")

def employers_profile(request, pk):
    if request.user.is_authenticated:
        profile = EmployerProfile.objects.get(user_id=pk)
        current_user = CustomUser.objects.get(id=request.user.id)
        if request.method == 'POST':
            form = EmployerProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                login(request, current_user)
                #messages.success(request, "Profile updated successfully.")
        else:
            form = EmployerProfileForm(instance=profile)
        
        return render(request, "employers_profile.html", {"form": form})
    else:
        #messages.error(request, "You need to be logged in to access this page.")
        return redirect('employers_home')