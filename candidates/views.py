from django.shortcuts import render, redirect
from .forms import CandidateProfile
from users.models import CustomUser
from django.contrib.auth import login
from .forms import CandidateProfileForm

def candidates_home(request):
    return render( request, "candidates_home.html", {})

def candidates_profile(request, pk):
    #Create instance
    if request.user.is_authenticated :
        profile = CandidateProfile.objects.get(user_id=pk)
        #Verify Sistem User owns the profile
        if request.user.id == profile.user_id:
            current_user = CustomUser.objects.get(id=request.user.id)
            #Get data for instance
            if request.method == 'POST':
                form = CandidateProfileForm(request.POST, instance=profile)
                if form.is_valid():
                    #Get CV File
                    cv_file = request.FILES.get('cv')
                    if cv_file:
                        profile.cv = cv_file
                        profile.save()

                    form.save()
                    login(request, current_user)
                    #messages.success(request, "Profile updated successfully.")
                    return redirect('candidates_home')
            else:
                form = CandidateProfileForm(instance=profile)
            
            return render(request, "candidates_profile.html", {"form": form})
        else:
            #messages.error(request, "You need to be logged in to access this page.")
            return redirect('candidates_home')
    else:
        #messages.error(request, "You need to be logged in to access this page.")
        return redirect('candidates_home')