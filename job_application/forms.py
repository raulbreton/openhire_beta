from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            'cover_letter',
            'resume',
            'linkedin_profile',
            'portfolio',
        ]

    def __init__(self, *args, **kwargs):
        super(JobApplicationForm, self).__init__(*args, **kwargs)
        # Customize form labels, help_texts, or widgets if needed
        self.fields['cover_letter'].widget = forms.Textarea(attrs={'rows': 5})
        self.fields['resume'].widget.attrs['accept'] = 'application/pdf, application/msword, application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        self.fields['linkedin_profile'].widget.attrs['placeholder'] = 'https://www.linkedin.com/in/your-profile'
        self.fields['portfolio'].widget.attrs['placeholder'] = 'https://www.your-portfolio.com'

    # You can add custom validation methods if needed
    # def clean_some_field(self):
    #     # Custom validation logic
    #     value = self.cleaned_data['some_field']
    #     if not some_condition:
    #         raise forms.ValidationError("Validation error message.")
    #     return value
