from django.db import models
from candidates.models import CandidateProfile
from job_offers.models import JobOffer

class JobApplication(models.Model):
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE)
    job_offer = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    linkedin_profile = models.URLField(blank=True, null=True)
    portfolio = models.URLField(blank=True, null=True)
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Submitted')
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.candidate.user.email} - {self.job_offer.job_title}"
