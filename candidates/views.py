from django.shortcuts import render

def candidates_home(request):
    return render( request, "candidates_home.html", {})

"""
def candidates_profile(request, pk):
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
    """