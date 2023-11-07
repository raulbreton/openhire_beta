from django.db import models
from users.models import CustomUser
from django.db.models.signals import post_save

class CandidateProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, default=None)
    resumen = models.TextField()
    experiencia = models.TextField()
    educacion = models.TextField()
    habilidades = models.TextField()  # Almacena como texto JSON
    idiomas = models.TextField()      # Almacena como texto JSON
    certificaciones = models.TextField()  # Almacena como texto JSON

    def __str__(self):
        return self.user.email
    
def created_profile(sender, instance, created, **kwargs):
    if created  and instance.is_candidate:
        user_profile = CandidateProfile(user=instance)
        user_profile.save()

post_save.connect(created_profile, sender=CustomUser)