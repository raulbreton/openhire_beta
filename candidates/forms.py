from django import forms
from .models import CandidateProfile

class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        #fields = ['resumen', 'experiencia', 'description']