from datetime import timezone
from django.shortcuts import redirect, render
from .forms import JobOfferForm
from .models import JobOffer
from employers.models import EmployerProfile

def post_offer(request):
    if not request.user.is_employer:
        return redirect('login')  # Redirect to login if the user is not an employer
    
    company_name = None

    if request.method == 'POST':
        form = JobOfferForm(request.POST)
        employer_profile = EmployerProfile.objects.get(user=request.user) #Retrieve company name from employer's profile
        company_name = employer_profile.company_name
        if form.is_valid():
            job_offer = form.save(commit=False)
            #job_offer.created_at = timezone.now()
            job_offer.company_name = company_name
            job_offer.employer_profile = request.user.employerprofile  # Assuming you have a one-to-one relationship between User and EmployerProfile
            job_offer.save()
            return redirect('employers_home')  # Redirect to the job offers page after successful submission
    else:
        form = JobOfferForm()
        company_name = EmployerProfile.objects.get(user=request.user).company_name  # Retrieve company name from employer's profile

    return render(request, "post_offer.html", {"form":form, 'company_name': company_name})