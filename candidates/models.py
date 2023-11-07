from django.db import models
from users.models import CustomUser
from django.db.models.signals import post_save

class CandidateProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    street = models.CharField(max_length=255, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    cv = models.FileField(upload_to='cv/', blank=True, null=True)

    def __str__(self):
        return self.user.email

def created_profile(sender, instance, created, **kwargs):
    if created and instance.is_candidate:
        user_profile = CandidateProfile(user=instance)
        user_profile.save()

post_save.connect(created_profile, sender=CustomUser)
