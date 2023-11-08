from django import forms
from .models import CandidateProfile

class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        fields = ['name', 'last_name', 'phone',
                  'country', 'city', 'street', 
                  'postal_code', 'cv']