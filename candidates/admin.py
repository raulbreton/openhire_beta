from django.contrib import admin
from .models import CandidateProfile

class UserAdmin(admin.ModelAdmin):
    model = CandidateProfile
    #Fields to display
    fields = ["user","resumen","experiencia", "educacion","habilidades","idiomas","certificaciones"]

admin.site.register(CandidateProfile, UserAdmin)